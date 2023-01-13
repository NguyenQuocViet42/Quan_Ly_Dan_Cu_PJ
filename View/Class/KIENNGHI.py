import datetime
class KIENNGHI:
    def __init__(self, MaKienNghi, ID, CCCD, NoiDung, NgayKN: datetime.datetime, PhanLoai ,TrangThai):
        self.MaKienNghi = MaKienNghi
        self.ID = ID
        self.CCCD = CCCD
        self.NoiDung = NoiDung
        self.NgayKN = NgayKN
        self.PhanLoai = PhanLoai
        self.TrangThai = TrangThai
    def init_values(values):
        kiennghi = KIENNGHI(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
        return kiennghi