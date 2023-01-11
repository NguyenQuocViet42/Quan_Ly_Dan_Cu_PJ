import datetime
class CUDAN:
    def __init__(self, ID, CCCD ,Ten, GioiTinh, NgaySinh: datetime.datetime, DanToc, QuocTich, NgheNghiep, 
                QueQuan, BiDanh, MaSo, QuanHe, NgayDangKyThuongtru, DiaChiCu, NgayChuyenDi, NoiChuyenDi, GhiChu):
        self.ID = ID
        self.CCCD = CCCD
        self.Ten = Ten
        self.GioiTinh = GioiTinh
        self.NgaySinh = NgaySinh
        self.DanToc = DanToc
        self.QuocTich = QuocTich
        self.NgheNghiep = NgheNghiep
        self.QueQuan = QueQuan
        self.BiDanh = BiDanh
        self.MaSo = MaSo
        self.QuanHe = QuanHe
        self.NgayDangKyThuongtru = NgayDangKyThuongtru
        self.DiaChiCu = DiaChiCu
        self.NgayChuyenDi = NgayChuyenDi
        self.NoiChuyenDi = NoiChuyenDi
        self.GhiChu = GhiChu
    def __init__(self, values):
        self.ID = values[0]
        self.CCCD = values[1]
        self.Ten = values[2]
        self.GioiTinh = values[3]
        self.NgaySinh = values[4]
        self.DanToc = values[5]
        self.QuocTich = values[6]
        self.NgheNghiep = values[7]
        self.QueQuan = values[8]
        self.BiDanh = values[9]
        self.MaSo = values[10]
        self.QuanHe = values[11]
        self.NgayDangKyThuongtru = values[12]
        self.DiaChiCu = values[13]
        self.NgayChuyenDi = values[14]
        self.NoiChuyenDi = values[15]
        self.GhiChu = values[16]