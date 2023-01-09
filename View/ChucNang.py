import connectDB

""" Xem thông tin hộ khẩu | Trả về 2 list, list đầu tiên là thông tin hộ khẩu, list tiếp theo là thông tin các cư dân """
def XemSoHoKhau(MaSo):
    # Thông tin hộ khẩu: 
    # MaSo, CCCDChuHo, SoThanhVien, SoNha/TenDuong, Phuong/Xa, Quan/Huyen,Tinh
    HoKhau = connectDB.getHoKhau(MaSo)[0]
    ListCCCD = connectDB.getListCuDanFromHoKhau(HoKhau[0])
    ListCuDan = []
    # Thông tin nhân khẩu:
    # ID ,CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú
    for i in range(len(ListCCCD)):
        thongtincudan = connectDB.getCUDAN(ListCCCD[i][0])[0]
        ListCuDan.append(tuple(thongtincudan))
    return HoKhau,ListCuDan

""" Thêm nhân khẩu mới gia đình sinh thêm con thì sẽ thêm mới thông tin nhân khẩu như trên, bỏ trống các chi tiết về nghề nghiệp, CMND và nơi
 thường trú chuyển đến sẽ ghi là “mới sinh” """
# Thông tin nhân khẩu:
# CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ
def ThemNhanKhauMoi(CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, MaSo , QuanHe, NgayDangKyThuongTru, DiaChiCu):
    CCCD = 'Mới Sinh'
    DiaChiCu = 'Mới Sinh'
    NgheNghiep = None
    val = (CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, MaSo , QuanHe, NgayDangKyThuongTru, DiaChiCu)
    # Thêm vào data base
    connectDB.insertCUDAN(val)
    NoiDung = 'Thêm nhân khẩu ' + Hoten + ' '  + CCCD + ' vào hộ khẩu ' + MaSo 
    connectDB.insertBienDoi(KieuBienDoi='Thêm nhân khẩu mới', NoiDungBienDoi = NoiDung, MaSo = MaSo)
    
""" Thay đổi nhân khẩu: nếu có một nhân khẩu chuyển đi nơi khác thì sẽ thêm các chi tiết như sau: ngày chuyển đi, nơi chuyển, ghi chú. Trường hợp 
nhân khẩu qua đời thì phần ghi chú là “Đã qua đời” """
def ThayDoiNhanKhau(ID, NgayChuyenDi, NoiChuyenDi, GhiChu, HoTen, CCCD, MaSo):
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