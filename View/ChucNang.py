import connectDB
import random
import datetime

""" Xem thông tin hộ khẩu | Trả về 2 list, list đầu tiên là thông tin hộ khẩu, list tiếp theo là thông tin các cư dân """
def XemSoHoKhau(MaSo):
    error_code = 0
    # Thông tin hộ khẩu: 
    # MaSo, CCCDChuHo, SoThanhVien, SoNha/TenDuong, Phuong/Xa, Quan/Huyen,Tinh
    try:
        HoKhau = connectDB.getHoKhau(MaSo)[0]
    except:
        error_code = 1
        return error_code, 1, 1
    ListCCCD = connectDB.getListCuDanFromHoKhau(HoKhau[0])
    ListCuDan = []
    # Thông tin nhân khẩu:
    # ID ,CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú
    for i in range(len(ListCCCD)):
        thongtincudan = connectDB.getCUDAN(ListCCCD[i][0])[0]
        ListCuDan.append(tuple(thongtincudan))
    return error_code, HoKhau, ListCuDan

""" Thêm nhân khẩu mới gia đình sinh thêm con thì sẽ thêm mới thông tin nhân khẩu như trên, bỏ trống các chi tiết về nghề nghiệp, CMND và nơi
 thường trú chuyển đến sẽ ghi là “mới sinh” """
# Thông tin nhân khẩu:
# CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ
def ThemNhanKhauMoi(CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, MaSo , QuanHe, NgayDangKyThuongTru, DiaChiCu):
    CCCD = 'Mới Sinh'
    DiaChiCu = 'Mới Sinh'
    NgheNghiep = None
    val = (CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, MaSo , QuanHe, NgayDangKyThuongTru, DiaChiCu, None, None, None)
    # Thêm vào data base
    connectDB.insertCUDAN(val)
    NoiDung = 'Thêm nhân khẩu ' + Hoten + ' '  + CCCD + ' vào hộ khẩu ' + MaSo 
    connectDB.insertBienDoi(KieuBienDoi='Thêm nhân khẩu mới', NoiDungBienDoi = NoiDung, MaSo = MaSo)
    
""" Thay đổi nhân khẩu: nếu có một nhân khẩu chuyển đi nơi khác thì sẽ thêm các chi tiết như sau: ngày chuyển đi, nơi chuyển, ghi chú. Trường hợp 
nhân khẩu qua đời thì phần ghi chú là “Đã qua đời” """
def ThayDoiNhanKhau(NgayChuyenDi, NoiChuyenDi, GhiChu, HoTen, CCCD, MaSo):
    ID = connectDB.TimIDTuMaSoCCCDHoTen(MaSo, CCCD, HoTen)
    NgayChuyenDi = str(NgayChuyenDi)
    NgayChuyenDi = NgayChuyenDi.split(' ')[0]
    connectDB.updateCUDAN_ChuyenDi(ID, NgayChuyenDi, NoiChuyenDi, GhiChu)
    if GhiChu == 'Đã qua đời':
        NoiDung = 'Thành viên ' + HoTen + ' '  + CCCD + ' của Hộ Khẩu ' + MaSo + ' đã qua đời vào ngày ' + str(NgayChuyenDi)
    else:
        NoiDung = 'Thành viên ' + HoTen + ' '  + CCCD + ' của Hộ Khẩu ' + MaSo + ' chuyển đi ' + NoiChuyenDi + ' vào ngày ' + str(NgayChuyenDi) 
    connectDB.insertBienDoi(KieuBienDoi='Thay đổi nhân khẩu', NoiDungBienDoi = NoiDung, MaSo = MaSo)
    
""" Những thay đổi liên quan cả hộ (ví dụ như thay đổi chủ hộ) cần ghi nhận các chi tiết như nội dung thay đổi, ngày thay đổi """
def ThayDoiChuHo(DanhSachIDThanhVien, DanhSachQuanHe, MaSo):
    for i in range(len(DanhSachIDThanhVien)):
        connectDB.ThayDoiQuanHe(ID=DanhSachIDThanhVien[i], QuanHeMoi=DanhSachQuanHe[i])
    NoiDung = 'Hộ khẩu ' + MaSo +  'thay đổi chủ hộ'
    connectDB.insertBienDoi(KieuBienDoi='Thay đổi chủ hộ', NoiDungBienDoi = NoiDung, MaSo = MaSo)
    
""" Khi tách hộ từ một hộ khẩu đã có thì một sổ hộ khẩu mới sẽ được tạo ra với các nhân khẩu được chọn """
# HoKhau_1 và HoKhau_2 có dạng: [ MaSo, [ [ID, QuanHe], [ID, QuanHe],... ], SoNha, Phuong, Quan, Tinh]
def TachHoKhau(HoKhau_1, HoKhau_2):
    MaSo_1, DanhSachNhanKhau, SoNha, Phuong, Quan, Tinh = HoKhau_1[0], HoKhau_1[1], HoKhau_1[2], HoKhau_1[3], HoKhau_1[4], HoKhau_1[5]
    connectDB.DeleteSoHoKhau(MaSo_1)
    connectDB.InsertSoHoKhau(MaSo_1, DanhSachNhanKhau, SoNha, Phuong, Quan, Tinh)
    MaSo_2, DanhSachNhanKhau, SoNha, Phuong, Quan, Tinh = HoKhau_2[0], HoKhau_2[1], HoKhau_2[2], HoKhau_2[3], HoKhau_2[4], HoKhau_2[5]
    MaSo_2 = random.randint(240000002, 259999999)
    DanhSachMaHoKhau = connectDB.LayDanhSachMaHoKhau()
    while MaSo_2 in DanhSachMaHoKhau:
        MaSo_2 = random.randint(100000002, 999999999)
    connectDB.InsertSoHoKhau(MaSo_2, DanhSachNhanKhau, SoNha, Phuong, Quan, Tinh)
    NoiDung = 'Sổ hộ khẩu ' + str(MaSo_1) + ' được tách thành 2 sổ hộ khẩu mới là: ' + str(MaSo_1) +' và ' + str(MaSo_2)
    connectDB.insertBienDoi(KieuBienDoi='Tách hộ khẩu', NoiDungBienDoi = NoiDung, MaSo = MaSo_1)
    
""" Khi hộ gia đình có ai đó đi xa dài ngày thì phải đến gặp tổ trưởng thông báo và xin cấp giấy tạm vắng có thời hạn. Ngược lại nếu có nhân khẩu từ địa
phương khác đến cư trú tạm thời trong một khoảng thời gian thì phải khai báo để được cấp giấy tạm trú """
def CapGiayTamVang(HoTen , CCCD, NoiTamVang ,NgayBatDau: datetime.datetime, NgayKetThuc: datetime.datetime, LyDo, NgayLamDon: datetime.datetime):
    error_code = 0
    try:
        MaSo = connectDB.LayMaHoKhauTuTenCCCD(HoTen, CCCD)
    except:
        error_code = 1
        return error_code
    connectDB.InsertTamVang(HoTen, CCCD, NoiTamVang, NgayBatDau, NgayKetThuc, LyDo, NgayLamDon)
    NoiDung = 'Cấp giấy tạm vắng cho cư dân ' + HoTen + ', số căn cước ' + CCCD + ' từ ngày ' + str(NgayBatDau).split(' ')[0] + ' đến ngày ' + str(NgayKetThuc).split(' ')[0]
    connectDB.insertBienDoi(KieuBienDoi='Cấp giấy tạm vắng', NoiDungBienDoi = NoiDung, MaSo = MaSo)
    return error_code

# Thông tin giấy tạm vắng bao gồm:
# MaGiayTamVang, HoTen, CCCD, NoiTamVang ,Tu, Den, LyDo, NgayLamDon
def XemGiayTamVang(HoTen, CCCD):
    ThongTinGiayTamVang = connectDB.getTamVang(HoTen, CCCD)[0]
    return ThongTinGiayTamVang

#----------------------------------------------------------------
def CapGiayTamTru(HoTen , CCCD, QueQuan, DiaChiThuongTru, NgayBatDau: datetime.datetime, NgayKetThuc: datetime.datetime, LyDo, NgayLamDon: datetime.datetime):
    error_code = 0
    try:
        MaSo = connectDB.LayMaHoKhauTuTenCCCD(HoTen, CCCD)
    except:
        error_code = 1
        return error_code
    connectDB.InsertTamTru(HoTen, CCCD, QueQuan, DiaChiThuongTru, NgayBatDau, NgayKetThuc, LyDo, NgayLamDon)
    NoiDung = 'Cấp giấy tạm trú cho cư dân ' + HoTen + ', số căn cước ' + CCCD + ' từ ngày ' + str(NgayBatDau).split(' ')[0] + ' đến ngày ' + str(NgayKetThuc).split(' ')[0] + ' tại ' + DiaChiThuongTru
    connectDB.insertBienDoi(KieuBienDoi='Cấp giấy tạm trú', NoiDungBienDoi = NoiDung, MaSo = MaSo)
    return error_code

# Thông tin giấy tạm vắng bao gồm:
# MaGiayTamVang, HoTen, CCCD, Tu, Den, LyDo, NgayLamDon
def XemGiayTamTru(HoTen, CCCD):
    ThongTinGiayTamTru = connectDB.getTamTru(HoTen, CCCD)[0]
    return ThongTinGiayTamTru

""" Xem lịch sử biến đổi nhân khẩu """
# Hàm trả về danh sách tất cả Thay đổi nhân khẩu
# Thông tin một bảng thay đổi: MaBienDoi, Ngay, KieuBienDoi, NoiDungBienDoi, MaSo
def LayLichSuBienDoiNhanKhau(MaSo):
    return connectDB.GetDanhSachThayDoiNhanKhau()

# Hàm trả thông tin của các bản thay đổi nhân khẩu của một Sổ Hộ Khẩu
def XemLichSuBienDoiNhanKhau(MaSo):
    return connectDB.XemDanhSachThayDoiNhanKhau(MaSo)