import connectDB
import random
import datetime
from Class.DangNhap import DangNhap as QL
from Class.CUDAN import CUDAN as TaoCuDan
from Class.BIENDOI import BIENDOI as TaoBienDoi
from Class.SOHOKHAU import SOHOKHAU as TaoHoKhau
from Class.KIENNGHI import KIENNGHI as TaoKienNghi
from Class.TraLoiKienNghi import TraLoiKienNghi as TaoTraLoiKienNghi

QuanLy = QL('captren08','vietdeptrai','Nguyễn Quốc Việt')
""" Đăng nhập """
# Nếu đăng nhập thành công, trả về đối tượng đăng nhập
# Trả về 0 là lỗi đăng nhập, trả về 1 là Tổ trưởng hoặc Cấp dưới, trả về 2 là Cấp trên
def DangNhap(IDQuanLy, MatKhau):
    try:
        ThongTin = connectDB.CheckThongTinDangNhap(IDQuanLy, MatKhau)
        quanly = QL(ThongTin[0], ThongTin[1], ThongTin[2])
        global QuanLy
        QuanLy = quanly
        connectDB.SetQuanLy(quanly)
        if quanly.IDQuanLy[0:7] == "captren":
            return 2
        else:
            return 1
    except:
        return 0

""" Xem thông tin hộ khẩu | Trả về 2 list, list đầu tiên là thông tin hộ khẩu, list tiếp theo là thông tin các cư dân """
def XemSoHoKhau(MaSo):
    error_code = 0
    # Thông tin hộ khẩu:
    # MaSo, CCCDChuHo, SoThanhVien, SoNha/TenDuong, Phuong/Xa, Quan/Huyen,Tinh
    try:
        HoKhau = connectDB.getHoKhau(MaSo)
    except:
        error_code = 1
        return error_code, 1, 1
    ListCCCD = connectDB.getListCuDanFromHoKhau(HoKhau.MaSo)
    ListCuDan = []
    # Thông tin nhân khẩu:
    # ID ,CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú
    for i in range(len(ListCCCD)):
        thongtincudan = connectDB.getCUDAN(ListCCCD[i][0])[0]
        ListCuDan.append(list(thongtincudan))
    for i in range(len(ListCuDan)):
        if ListCuDan[i][11].upper() == 'Chủ Hộ'.upper():
            tmp = ListCuDan[0]
            ListCuDan[0] = ListCuDan[i]
            ListCuDan[i] = tmp
            break
    return error_code, HoKhau, ListCuDan


""" Thêm nhân khẩu mới gia đình sinh thêm con thì sẽ thêm mới thông tin nhân khẩu như trên, bỏ trống các chi tiết về nghề nghiệp, CMND và nơi
 thường trú chuyển đến sẽ ghi là “mới sinh” """
# Thông tin nhân khẩu:
# CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú


def ThemNhanKhauMoi(CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, MaSo, QuanHe, NgayDangKyThuongTru, DiaChiCu):
    val = (CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan,
           BiDanh, MaSo, QuanHe, NgayDangKyThuongTru, DiaChiCu, None, None, None)
    # Thêm vào data base
    connectDB.insertCUDAN(val)
    NoiDung = 'Thêm nhân khẩu ' + Hoten + ' ' + CCCD + ' vào hộ khẩu ' + str(MaSo)
    biendoi = TaoBienDoi(1, 1,KieuBienDoi='Thêm nhân khẩu mới', NoiDungBienDoi=NoiDung, MaSo=MaSo, IDQuanLy = QuanLy.IDQuanLy)
    connectDB.insertBienDoi(biendoi)


""" Thay đổi nhân khẩu: nếu có một nhân khẩu chuyển đi nơi khác thì sẽ thêm các chi tiết như sau: ngày chuyển đi, nơi chuyển, ghi chú. Trường hợp 
nhân khẩu qua đời thì phần ghi chú là “Đã qua đời” """


def ThayDoiNhanKhau(NgayChuyenDi, NoiChuyenDi, GhiChu, HoTen, CCCD, MaSo):
    errorCode = 0
    try:
        ID = connectDB.TimIDTuMaSoCCCDHoTen(MaSo, CCCD, HoTen)
    except:
        errorCode = 1
        return errorCode

    connectDB.updateCUDAN_ChuyenDi(ID, NgayChuyenDi, NoiChuyenDi, GhiChu)
    if GhiChu == 'Đã qua đời':
        NoiDung = 'Thành viên ' + HoTen + ' ' + CCCD + ' của Hộ Khẩu ' + \
            MaSo + ' đã qua đời vào ngày ' + NgayChuyenDi
    else:
        if (NoiChuyenDi == ""):
            errorCode = 2
            return errorCode
        NoiDung = 'Thành viên ' + HoTen + ' ' + CCCD + ' của Hộ Khẩu ' + MaSo + \
            ' chuyển đi ' + NoiChuyenDi + ' vào ngày ' + NgayChuyenDi
    biendoi = TaoBienDoi(1, 1,KieuBienDoi='Thay đổi nhân khẩu', NoiDungBienDoi=NoiDung, MaSo=MaSo, IDQuanLy = QuanLy.IDQuanLy)
    connectDB.insertBienDoi(biendoi)
    return errorCode


""" Những thay đổi liên quan cả hộ (ví dụ như thay đổi chủ hộ) cần ghi nhận các chi tiết như nội dung thay đổi, ngày thay đổi """


def ThayDoiChuHo(DanhSachIDThanhVien, DanhSachQuanHe, MaSo):
    global QuanLy
    for i in range(len(DanhSachIDThanhVien)):
        connectDB.ThayDoiQuanHe(
            ID=DanhSachIDThanhVien[i], QuanHeMoi=DanhSachQuanHe[i])
    NoiDung = 'Hộ khẩu ' + MaSo + 'thay đổi chủ hộ'
    biendoi = TaoBienDoi(1, 1,KieuBienDoi='Thay đổi chủ hộ', NoiDungBienDoi=NoiDung, MaSo=MaSo, IDQuanLy = QuanLy.IDQuanLy)
    connectDB.insertBienDoi(biendoi)


""" Khi tách hộ từ một hộ khẩu đã có thì một sổ hộ khẩu mới sẽ được tạo ra với các nhân khẩu được chọn """
# HoKhau_1 và HoKhau_2 có dạng: [ MaSo, [ [ID, QuanHe], [ID, QuanHe],... ], SoNha, Phuong, Quan, Tinh]


def TachHoKhau(HoKhau_1, HoKhau_2):
    MaSo_1, DanhSachNhanKhau, SoNha, Phuong, Quan, Tinh = HoKhau_1[
        0], HoKhau_1[1], HoKhau_1[2], HoKhau_1[3], HoKhau_1[4], HoKhau_1[5]
    connectDB.UpdateThanhVien(MaSo_1, DanhSachNhanKhau)
    MaSo_2, DanhSachNhanKhau, SoNha, Phuong, Quan, Tinh = HoKhau_2[
        0], HoKhau_2[1], HoKhau_2[2], HoKhau_2[3], HoKhau_2[4], HoKhau_2[5]
    MaSo_2 = random.randint(240000002, 259999999)
    DanhSachMaHoKhau = connectDB.LayDanhSachMaHoKhau()
    while MaSo_2 in DanhSachMaHoKhau:
        MaSo_2 = random.randint(100000002, 999999999)
    connectDB.InsertSoHoKhau(MaSo_2, DanhSachNhanKhau,
                             SoNha, Phuong, Quan, Tinh)
    NoiDung = 'Sổ hộ khẩu ' + \
        str(MaSo_1) + ' được tách thành 2 sổ hộ khẩu mới là: ' + \
        str(MaSo_1) + ' và ' + str(MaSo_2)
    biendoi = TaoBienDoi(1, 1,KieuBienDoi='Tách hộ khẩu', NoiDungBienDoi=NoiDung, MaSo=MaSo_1, IDQuanLy = QuanLy.IDQuanLy)
    connectDB.insertBienDoi(biendoi)


""" Khi hộ gia đình có ai đó đi xa dài ngày thì phải đến gặp tổ trưởng thông báo và xin cấp giấy tạm vắng có thời hạn. Ngược lại nếu có nhân khẩu từ địa
phương khác đến cư trú tạm thời trong một khoảng thời gian thì phải khai báo để được cấp giấy tạm trú """


def CapGiayTamVang(HoTen, CCCD, NoiTamVang, NgayBatDau: datetime.datetime, NgayKetThuc: datetime.datetime, LyDo, NgayLamDon: datetime.datetime):
    error_code = 0
    try:
        MaSo = connectDB.LayMaHoKhauTuTenCCCD(HoTen, CCCD)
        id = connectDB.TimIDTuMaSoCCCDHoTen(MaSo,CCCD, HoTen)
    except:
        error_code = 1
        return error_code
    connectDB.InsertTamVang(id, HoTen, CCCD, NoiTamVang,
                            NgayBatDau, NgayKetThuc, LyDo, NgayLamDon)
    NoiDung = 'Cấp giấy tạm vắng cho cư dân ' + HoTen + ', số căn cước ' + CCCD + \
        ' từ ngày ' + \
        str(NgayBatDau).split(' ')[0] + \
        ' đến ngày ' + str(NgayKetThuc).split(' ')[0]
    biendoi = TaoBienDoi(1, 1,KieuBienDoi='Cấp giấy tạm vắng', NoiDungBienDoi=NoiDung, MaSo=MaSo, IDQuanLy = QuanLy.IDQuanLy)
    connectDB.insertBienDoi(biendoi)
    return error_code

# Thông tin giấy tạm vắng bao gồm:
# MaGiayTamVang, HoTen, CCCD, NoiTamVang ,Tu, Den, LyDo, NgayLamDon


def XemGiayTamVang(HoTen, CCCD):
    error_code = 0
    try :
        ThongTinGiayTamVang = connectDB.getTamVang(HoTen, CCCD)[0]
    except:
        error_code = 1
        return 1,1
    return error_code, ThongTinGiayTamVang

# ----------------------------------------------------------------


def CapGiayTamTru(HoTen, CCCD, QueQuan, DiaChiThuongTru, NgayBatDau: datetime.datetime, NgayKetThuc: datetime.datetime, LyDo, NgayLamDon: datetime.datetime):
    error_code = 0
    try:
        MaSo = connectDB.LayMaHoKhauTuTenCCCD(HoTen, CCCD)
        id = connectDB.TimIDTuMaSoCCCDHoTen(MaSo,CCCD, HoTen)
    except:
        error_code = 1
        return error_code
    connectDB.InsertTamTru(id ,HoTen, CCCD, QueQuan, DiaChiThuongTru,
                           NgayBatDau, NgayKetThuc, LyDo, NgayLamDon)
    NoiDung = 'Cấp giấy tạm trú cho cư dân ' + HoTen + ', số căn cước ' + CCCD + ' từ ngày ' + \
        str(NgayBatDau).split(' ')[
            0] + ' đến ngày ' + str(NgayKetThuc).split(' ')[0] + ' tại ' + DiaChiThuongTru
    biendoi = TaoBienDoi(1, 1,KieuBienDoi='Cấp giấy tạm trú', NoiDungBienDoi=NoiDung, MaSo=MaSo, IDQuanLy = QuanLy.IDQuanLy)
    connectDB.insertBienDoi(biendoi)
    return error_code

# Thông tin giấy tạm vắng bao gồm:
# MaGiayTamVang, HoTen, CCCD, Tu, Den, LyDo, NgayLamDon


def XemGiayTamTru(HoTen, CCCD):
    try:
        ThongTinGiayTamTru = connectDB.getTamTru(HoTen, CCCD)[0]
    except:
        return 1,1
    return 0, ThongTinGiayTamTru


""" Xem lịch sử biến đổi nhân khẩu """
# Hàm trả về danh sách tất cả Thay đổi nhân khẩu
# Thông tin một bảng thay đổi: MaBienDoi, Ngay, KieuBienDoi, NoiDungBienDoi, MaSo
def LayLichSuBienDoiNhanKhau():
    try:
        return 0, connectDB.GetDanhSachThayDoiNhanKhau()
    except:
        return 1,1

# Hàm trả thông tin của các bản thay đổi nhân khẩu của một Sổ Hộ Khẩu
def XemLichSuBienDoiNhanKhau(MaSo):
    try:
        return 0, connectDB.XemDanhSachThayDoiNhanKhau(MaSo)
    except:
        return 1,1

""" Thống kê theo giới tính """
def ThongKeGioiTinh():
    # Trả về số lượng Nam, Nữ
    return connectDB.LaySoLuongGioiTinh()

""" Thống kê theo độ tuổi theo độ tuổi (mầm non / mẫu giáo / cấp 1 / cấp 2 / cấp 3 / độ tuổi lao động / nghỉ hưu) """
def CheckTuoi(Tuoi, Khoang):
    if Tuoi >= Khoang[0] and Tuoi <= Khoang[1]:
        return 1
    return 0
# Hàm trả về list chứa số lượng cư dân ứng với các độ tuổi: mầm non / mẫu giáo / cấp 1 / cấp 2 / cấp 3 / độ tuổi lao động / nghỉ hưu
def ThongKeTheoDoTuoi():
    MamNon = [0,3]
    MauGiao = [3,5]
    Cap1 = [6,10]
    Cap2 = [11,15]
    Cap3 = [15,18]
    LaoDong = [15,60]
    NghiHuu = [61,999]
    CacKhoangTuoi = [MamNon, MauGiao, Cap1, Cap2, Cap3, LaoDong, NghiHuu]
    ThongKeDoTuoi = [0, 0, 0, 0, 0, 0, 0]
    DanhSachTuoi = connectDB.LayDanhSachTuoi()
    for tuoi in DanhSachTuoi:
        for i in range(len(CacKhoangTuoi)):
            if CheckTuoi(tuoi, CacKhoangTuoi[i]):
                ThongKeDoTuoi[i] +=1
    return ThongKeDoTuoi

""" Thống kê tạm trú, tạm vắng """
# Hàm trả về 2 giá trị: Số lượng tạm trú, số lượng tạm vắng
def ThongKeTamtruTamVang():
    SoLuongTamTru = connectDB.LaySoLuongTamTru()
    SoLuongTamVang = connectDB.LaySoLuongTamVang()
    return SoLuongTamTru, SoLuongTamVang

""" Các thông tin phản ánh, kiến nghị của nhân dân trong tổ sẽ được tổ trưởng ghi nhận để tổng hợp gửi lên cấp trên. Mỗi
phản ảnh, kiến nghị cần ghi nhận: người phản ánh, nội dung, ngày phản ánh, phân loại và trạng thái. """
def TaoDonKienNghi( HoTen, CCCD, NoiDung, NgayKN: datetime.datetime, PhanLoai):
    try:
        CuDan = connectDB.TimCUDANTuHoTenCCCD(HoTen, CCCD)
    except:
        return 1, 'Họ tên và căn cước không hợp lệ', 1
    DonKienNghi = TaoKienNghi(1, CuDan.ID, CCCD, NoiDung, NgayKN, PhanLoai ,'Mới ghi nhận')
    return 0, connectDB.InsertDonKienNghi(DonKienNghi)

# Trả về Cư Dân và danh sách kiến nghị của cư dân đó
# Trả về 3 giá trị: error code, CuDan, DanhSachKienNghi
# error code = 0 --> không lỗi, error code = 1 --> Lỗi Họ tên và CCCD, error code =2 --> Cư dân đó không có đơn kiến nghị
def XemDonKienNghi(HoTen, CCCD):
    try:
        CuDan = connectDB.TimCUDANTuHoTenCCCD(HoTen, CCCD)
    except:
        return 1, 'Họ tên và căn cước không hợp lệ', 1
    list = connectDB.TimDonKienNghi(CuDan)
    if len(list) == 0:
        return 2, CuDan, ('Cư dân ' + CuDan.HoTen + ' không có đơn kiến nghị nào.')
    DanhSachKienNghi = []
    for i in list:
        DanhSachKienNghi.append(TaoKienNghi.init_values(i))
    return 0, CuDan, DanhSachKienNghi

""" Cấp trên trả lời kiến nghị """
def TraLoiKienNghi(MaKienNghi, NoiDung):
    ThuTraLoi = TaoTraLoiKienNghi(1, MaKienNghi, NoiDung, 1, 1, QuanLy.TenQuanLy, QuanLy.IDQuanLy)
    connectDB.InsertTraLoiKienNghi(ThuTraLoi)
    
    

""" Khi có phản hồi từ các cơ quan có liên quan, tổ trưởng sẽ ghi nhận lại với phản ánh / kiến nghị tương ứng và thông báo cho
cá nhân có liên quan. Các kiến nghị trùng nhau có thể được gộp lại thành một nhưng phải ghi nhận những người phản ánh và số lần phản ánh """
