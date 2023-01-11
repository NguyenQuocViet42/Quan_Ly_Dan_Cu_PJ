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
    def __init__(self, values):
        self.MaKienNghi = values[0]
        self.ID = values[1]
        self.CCCD = values[2]
        self.NoiDung = values[3]
        self.NgayKN = values[4]
        self.PhanLoai = values[5]
        self.TrangThai = values[6]