import datetime
class CUDAN:
    def __init__(self, ID, CCCD ,HoTen, GioiTinh, NgaySinh: datetime.datetime, DanToc, QuocTich, NgheNghiep, 
                QueQuan, BiDanh, MaSo, QuanHe, NgayDangKyThuongtru, DiaChiCu, NgayChuyenDi, NoiChuyenDi, GhiChu):
        self.ID = ID
        self.CCCD = CCCD
        self.HoTen = HoTen
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
    def init_values(values):
        CuDan = CUDAN(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[16])
        return CuDan