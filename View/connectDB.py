# import required modules
import pyodbc

# create connection object
mydb = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-EP0NASK;'  # DESKTOP-EP0NASK
                      'Database=QLCUDAN;'
                      'Trusted_Connection=yes;')

# create cursor object
cursor = mydb.cursor()


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
    return cursor.fetchall()

# Lấy danh sách ID cư dân thuộc hộ khẩu


def getListCuDanFromHoKhau(MaSo):
    query = "select ID from CUDAN where MaSo = ?"
    val = (MaSo,)
    cursor.execute(query, val)
    return cursor.fetchall()
# Thêm vào bảng Biến Đổi


def insertBienDoi(KieuBienDoi, NoiDungBienDoi, MaSo):
    query = "insert into BIENDOI values (getdate(), ?, ?, ?)"
    val = (KieuBienDoi, NoiDungBienDoi, MaSo)
    cursor.execute(query, val)
    mydb.commit()

# Khi có Nhân khẩu chuyển đi


def updateCUDAN_ChuyenDi(ID, NgayChuyenDi, NoiChuyenDi, GhiChu):
    values = (NgayChuyenDi, NoiChuyenDi, GhiChu, ID)
    query = "UPDATE CUDAN SET NgayChuyenDi = ?, NoiChuyenDi = ?, GhiChu = ? WHERE ID =?"
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
        query = "update CUDAN set QuanHe = ?, MaSo = ?  where ID = ? "
        values = (quanhe, MaSo, id)
        cursor.execute(query, values)
        mydb.commit()
    query = " insert into SOHOKHAU values (?,?,?,?,?,?,?) "
    values = (MaSo, SoThanhVien, SoNha, Phuong, Quan, Tinh, IDChuHo)
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


def InsertTamVang(HoTen, CCCD, NoiTamVang, Tu, Den, LyDo, NgayLamDon):
    values = (HoTen, CCCD, NoiTamVang, Tu, Den, LyDo, NgayLamDon)
    query = "insert into TAMVANG values(?,?,?,?,?,?,?)"
    cursor.execute(query, values)
    mydb.commit()
# Xem giấy tạm vắng


def getTamVang(HoTen, CCCD):
    query = " select * from TAMVANG where upper(HoTen) = ? and CCCD = ?"
    values = (HoTen.upper(), CCCD)
    cursor.execute(query, values)
    return cursor.fetchall()

# Thêm giấy tạm trú


def InsertTamTru(HoTen, CCCD, QueQuan, DiaChiThuongTru, Tu, Den, LyDo, NgayLamDon):
    values = (HoTen, CCCD, QueQuan, DiaChiThuongTru, Tu, Den, LyDo, NgayLamDon)
    query = "insert into TAMTRU values(?,?,?,?,?,?,?,?)"
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
