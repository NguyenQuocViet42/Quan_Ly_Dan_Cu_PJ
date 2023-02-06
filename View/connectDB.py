# import required modules
import pyodbc
import os
import Restore_Backup
from Class.SOHOKHAU import SOHOKHAU as TaoHoKhau
from Class.DangNhap import DangNhap as QL
from Class.BIENDOI import BIENDOI as TaoBienDoi
from Class.CUDAN import CUDAN as TaoCuDan
from Class.KIENNGHI import KIENNGHI as TaoKienNghi
from Class.TraLoiKienNghi import TraLoiKienNghi as TaoTraLoiKienNghi
import socket

hostname = socket.gethostname()
# create connection object
try:
    mydb = pyodbc.connect('Driver={SQL Server};'
                          'Server=%s;'
                          'Database=QLCUDAN;'
                          'Trusted_Connection=yes;' % hostname)
except:
    Restore_Backup.Restore()
    mydb = pyodbc.connect('Driver={SQL Server};'
                          'Server=%s;'
                          'Database=QLCUDAN;'
                          'Trusted_Connection=yes;' % hostname)
# create cursor object
cursor = mydb.cursor()
QuanLy = QL('captren08', 'vietdeptrai', 'Nguyễn Quốc Việt')


# Check thông tin đăng nhập
def CheckThongTinDangNhap(IDQuanLy, MatKhau):
    query = " select * from DANGNHAP where IDQuanLy = ? and MatKhau = ?"
    values = (IDQuanLy, MatKhau)
    cursor.execute(query, values)
    return cursor.fetchall()[0]


def SetQuanLy(quanly):
    global QuanLy
    QuanLy = quanly


def getAllHoKhau():
    query = "SELECT * FROM SOHOKHAU"
    cursor.execute(query)
    return cursor.fetchall()

# Thêm nhân khẩu mới


def insertCUDAN(values):
    query = "INSERT INTO CUDAN (CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, MaSo, QuanHe, NgayDangKyThuongTru, DiaChiCu, NgayChuyenDi, NoiChuyenDi, GhiChu) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, values)
    mydb.commit()

# Lấy thông tin cư dân


def getCUDAN(ID):
    query = "select CUDAN.* from CUDAN where CUDAN.ID = ?"
    val = (ID,)
    # biến truyền vào dưới dạng 1 mảng
    cursor.execute(query, val)
    return cursor.fetchall()


def getTenCUDAN(ID):
    arr = getCUDAN(ID)[0]
    name = arr[2]
    return name

# Lấy mã hộ khẩu từ tên và cccd


def LayMaHoKhauTuTenCCCD(HoTen, CCCD):
    query = " select MaSo from CUDAN where upper(HoTen) = ? and CCCD = ? "
    values = (HoTen.upper(), CCCD)
    cursor.execute(query, values)
    return cursor.fetchall()[0][0]

# Lấy thông tin hộ khẩu


def getHoKhau(hostId):
    query = "SELECT * FROM SOHOKHAU WHERE  MaSo = ?"
    val = (hostId,)
    cursor.execute(query, val)
    MaSo, SoThanhVien, SoNha, Phuong, Huyen, Tinh, IDChuHo = cursor.fetchall()[
        0]
    hokhau = TaoHoKhau(MaSo, SoThanhVien, SoNha, Phuong, Huyen, Tinh, IDChuHo)
    return hokhau

# Lấy danh sách ID cư dân thuộc hộ khẩu


def getListCuDanFromHoKhau(MaSo):
    query = "select ID from CUDAN where MaSo = ?"
    val = (MaSo,)
    cursor.execute(query, val)
    return cursor.fetchall()
# Thêm vào bảng Biến Đổi


def insertBienDoi(BienDoi: TaoBienDoi):
    query = "insert into BIENDOI values (getdate(), ?, ?, ?,?)"
    val = (BienDoi.KieuBienDoi, BienDoi.NoiDungBienDoi,
           BienDoi.MaSo, BienDoi.IDQuanLy)
    cursor.execute(query, val)
    mydb.commit()

# Thay đổi thông tin cư dân


def updateCUDAN(ID, CCCD, HoTen, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, MaSo, QuanHe, NgayDangKyThuongTru, DiaChiCu, NgayChuyenDi, NoiChuyenDi, GhiChu):
    values = (CCCD, HoTen, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh,
              MaSo, QuanHe, NgayDangKyThuongTru, DiaChiCu, NgayChuyenDi, NoiChuyenDi, GhiChu, ID)
    query = "UPDATE CUDAN  set CCCD = ?, HoTen = ?, GioiTinh = ?, NgaySinh = ?, DanToc = ?, QuocTich = ?, NgheNghiep = ?, QueQuan = ?, BiDanh = ?, MaSo = ?, QuanHe = ?, NgayDangKyThuongTru = ?, DiaChiCu = ?, NgayChuyenDi = ?, NoiChuyenDi = ?, GhiChu = ? where ID = ?"
    cursor.execute(query, values)
    mydb.commit()

# Thay đổi quan hệ trong hộ khẩu


def ThayDoiQuanHe(ID, QuanHeMoi):
    values = (QuanHeMoi, ID)
    query = "UPDATE CUDAN SET QuanHe = ? WHERE ID =?"
    cursor.execute(query, values)
    mydb.commit()

# Xóa một hộ khẩu


def DeleteSoHoKhau(MaSo):
    query = " delete from SOHOKHAU where MaSo = ? "
    val = (MaSo,)
    cursor.execute(query, val)
    mydb.commit()

# Thêm một hộ khẩu


def InsertSoHoKhau(MaSo, DanhSachNhanKhau, SoNha, Phuong, Quan, Tinh):
    IDChuHo = None
    SoThanhVien = len(DanhSachNhanKhau)
    for i in DanhSachNhanKhau:
        id, quanhe = i[0], i[1]
        if quanhe.upper() == 'Chủ hộ'.upper():
            IDChuHo = id
            query = " insert into SOHOKHAU values (?,?,?,?,?,?,?) "
            values = (MaSo, SoThanhVien, SoNha, Phuong, Quan, Tinh, IDChuHo)
            cursor.execute(query, values)
            mydb.commit()
    for i in DanhSachNhanKhau:
        id, quanhe = i[0], i[1]
        query = "update CUDAN set QuanHe = ?, MaSo = ?  where ID = ? "
        values = (quanhe, MaSo, id)
        cursor.execute(query, values)
        mydb.commit()


def UpdateThanhVien(MaSo, DanhSachNhanKhau):
    for i in DanhSachNhanKhau:
        id, quanhe = i[0], i[1]
        if quanhe.upper() == 'Chủ hộ'.upper():
            IDChuHo = id
        query = "update CUDAN set QuanHe = ?, MaSo = ?  where ID = ? "
        values = (quanhe, MaSo, id)
        cursor.execute(query, values)
        mydb.commit()
    query = "update SOHOKHAU set SoThanhVien = ?, IDChuHo = ?"
    values = (len(DanhSachNhanKhau), IDChuHo)
    cursor.execute(query, values)
    mydb.commit()

# Lấy danh sách Mã hộ khẩu


def LayDanhSachMaHoKhau():
    query = " select MaSo from SOHOKHAU "
    cursor.execute(query)
    arr = []
    tmp = cursor.fetchall()
    for i in tmp:
        arr.append(i[0])
    return arr

# Thêm giấy tạm vắng


def InsertTamVang(ID, HoTen, CCCD, NoiTamVang, Tu, Den, LyDo, NgayLamDon):
    values = (ID, HoTen, CCCD, NoiTamVang, Tu, Den, LyDo, NgayLamDon)
    query = "insert into TAMVANG values(?,?,?,?,?,?,?,?)"
    cursor.execute(query, values)
    mydb.commit()
# Xem giấy tạm vắng


def getTamVang(HoTen, CCCD):
    query = " select * from TAMVANG where upper(HoTen) = ? and CCCD = ?"
    values = (HoTen.upper(), CCCD)
    cursor.execute(query, values)
    return cursor.fetchall()

# Thêm giấy tạm trú


def InsertTamTru(ID, HoTen, CCCD, QueQuan, DiaChiThuongTru, Tu, Den, LyDo, NgayLamDon):
    values = (ID, HoTen, CCCD, QueQuan, DiaChiThuongTru,
              Tu, Den, LyDo, NgayLamDon)
    query = "insert into TAMTRU values(?,?,?,?,?,?,?,?,?)"
    cursor.execute(query, values)
    mydb.commit()
# Xem giấy tạm trú


def getTamTru(HoTen, CCCD):
    query = " select * from TAMTRU where upper(HoTen) = ? and CCCD = ?"
    values = (HoTen.upper(), CCCD)
    cursor.execute(query, values)
    return cursor.fetchall()

# Tìm ID dựa trên MaSo, CCCD, HoTen


def TimIDTuMaSoCCCDHoTen(MaSo, CCCD, HoTen):
    query = " select ID from CUDAN where MaSo = ? and CCCD = ? and upper(HoTen) = ? "
    values = (MaSo, CCCD, HoTen.upper())
    cursor.execute(query, values)
    return cursor.fetchall()[0][0]

# Hàm trả về danh sách tất cả Thay đổi nhân khẩu


def GetDanhSachThayDoiNhanKhau():
    query = "select * from BienDoi"
    cursor.execute(query)
    return cursor.fetchall()

# Hàm trả về danh sách tất cả Thay đổi nhân khẩu của một Hộ khẩu


def XemDanhSachThayDoiNhanKhau(MaSo):
    query = "select * from BienDoi where MaSo = ?"
    val = (MaSo,)
    cursor.execute(query, val)
    return cursor.fetchall()

# Hàm trả về số lượng giới tính nam và nữ trong tổ dân phố


def LaySoLuongGioiTinh():
    query = " select count(ID) from CUDAN"
    cursor.execute(query)
    SoLuongCuDan = cursor.fetchall()[0][0]
    query = " select count(ID) from CUDAN where upper(GioiTinh) = upper('Nam')"
    cursor.execute(query)
    SoLuongNam = cursor.fetchall()[0][0]
    SoLuongNu = SoLuongCuDan - SoLuongNam
    return SoLuongNam, SoLuongNu

# Hàm trả về danh sách tuổi của tất cả Cư dân


def LayDanhSachTuoi():
    query = " select ( year(getdate()) - year(NgaySinh)) from CUDAN "
    cursor.execute(query)
    DuLieuTuoi = cursor.fetchall()
    DanhSachTuoi = []
    for i in DuLieuTuoi:
        DanhSachTuoi.append(i[0])
    return DanhSachTuoi

# Hàm trả về số lượng tạm trú, số lượng tạm vắng


def LaySoLuongTamVang():
    try:
        query = " select count(MaGiayTamVang) from TamVang"
        cursor.execute(query)
        return cursor.fetchall()[0][0]
    except:
        return 0


def LaySoLuongTamTru():
    try:
        query = " select count(MaGiayTamTru) from TamTru"
        cursor.execute(query)
        return cursor.fetchall()[0][0]
    except:
        return 0

# Thêm đơn kiến nghị vào DB


def InsertDonKienNghi(DonKienNghi: TaoKienNghi):
    # Check CCCD
    query = " select ID from CUDAN where CCCD = ? "
    val = (DonKienNghi.CCCD,)
    cursor.execute(query, val)
    i = cursor.fetchall()
    if len(i) == 0:
        return 1
    query = " insert into KIENNGHI values(?,?,?,?,?,?) "
    values = tuple(DonKienNghi.__dict__.values())[1:]
    cursor.execute(query, values)
    mydb.commit()
    return 0


def TimCUDANTuHoTenCCCD(HoTen, CCCD):
    query = " select * from CUDAN where upper(HoTen) = ? and CCCD = ? "
    val = (HoTen.upper(), CCCD)
    cursor.execute(query, val)
    thongtincudan = cursor.fetchall()[0]
    cudan = TaoCuDan.init_values(values=thongtincudan)
    return cudan


def TimDonKienNghi(CuDan: TaoCuDan):
    query = " select * from KIENNGHI where ID = ? "
    val = (CuDan.ID,)
    cursor.execute(query, val)
    list = cursor.fetchall()
    return list


def TimToanBoDonKienNghi():
    query = "select * from KIENNGHI order by NgayKN desc"
    cursor.execute(query)
    list = cursor.fetchall()
    return list

def TimToanBoDonKienNghiTheoTrangThai(TrangThai):
    query = "select * from KIENNGHI where TrangThai = ? order by NgayKN desc"
    val = (TrangThai,)
    cursor.execute(query,val)
    list = cursor.fetchall()
    return list

def InsertTraLoiKienNghi(ThuTraLoi: TaoTraLoiKienNghi):
    query = " insert into TraLoiKienNghi values(?,?, getdate(), N'Đã xử lý', ?, ?) "
    values = (ThuTraLoi.MaKienNghi, ThuTraLoi.NoiDung,
              ThuTraLoi.TenNguoiTraLoi, ThuTraLoi.IDQuanLy)
    cursor.execute(query, values)
    mydb.commit()
    query = " update KIENNGHI set TrangThai = N'Đã xử lý' where MaKienNghi = ?"
    val = (ThuTraLoi.MaKienNghi,)
    cursor.execute(query, val)
    mydb.commit()


def ThongBao():
    query = " select * from TraLoiKienNghi  where TrangThai = N'Đã xử lý' order by NgayTraLoi desc"
    cursor.execute(query)
    DanhSachTraLoi = cursor.fetchall()
    if len(DanhSachTraLoi) == 0:
        return 1, 1
    else:
        listTraLoi = []
        for i in DanhSachTraLoi:
            listTraLoi.append(TaoTraLoiKienNghi.init_values(i))
    query = " select * from KIENNGHI  where TrangThai = N'Đã xử lý' "
    cursor.execute(query)
    DanhSachKienNghi = cursor.fetchall()
    listKienNghi = []
    for i in DanhSachKienNghi:
        listKienNghi.append(TaoKienNghi.init_values(i))
    return listKienNghi, listTraLoi


def updateTrangThai(MaKienNghi, TrangThai):
    query = " update KIENNGHI set TrangThai = ? where MaKienNghi = ?"
    values = (TrangThai, MaKienNghi)
    cursor.execute(query, values)
    mydb.commit()
    query = " update TraLoiKienNghi set TrangThai = ? where MaKienNghi = ?"
    values = (TrangThai, MaKienNghi)
    cursor.execute(query, values)
    mydb.commit()


def CountKienNghi():
    ListTT = ['Mới ghi nhận', 'Chưa xử lý', 'Đã xử lý', 'Đã thông báo']
    ThongKe = []
    for TrangThai in ListTT:
        query = " select count(MaKienNghi) from KIENNGHI  where upper(TrangThai) = ? "
        val = (TrangThai.upper(),)
        cursor.execute(query, val)
        SoLuong = cursor.fetchall()[0][0]
        ThongKe.append(SoLuong)
    return ThongKe

def XoaKienNghi(ID):
    query = 'delete from KIENNGHI where MaKienNghi = ?'
    values = (ID,)
    cursor.execute(query, values)
    mydb.commit()
    
def GopKienNGhi(MaKienNghi, DanhSachHoTen, DanhSachCCCD, SoLuong):
    query = 'insert into BangGopKienNghi values(?,?,?,?)'
    values = (MaKienNghi, DanhSachHoTen, DanhSachCCCD, SoLuong)
    cursor.execute(query, values)
    mydb.commit()
    
def TimToanBoBangGop():
    query = 'select * from BangGopKienNghi'
    cursor.execute(query)
    list = cursor.fetchall()
    ListMaKienNghi = []
    ListDanhSachHoTen = []
    ListCCCD = []
    ListSoLuong = []
    for i in list:
        ListMaKienNghi.append(i[0])
        ListDanhSachHoTen.append(i[1])
        ListCCCD.append(i[2])
        ListSoLuong.append(i[3])
    return ListMaKienNghi, ListDanhSachHoTen, ListCCCD, ListSoLuong