import CUDAN
import datetime
class KIENNGHI:
    def __init__(self, MaKienNghi, NguoiLamDon: CUDAN, NoiDung, NgayKN: datetime.datetime, TrangThai):
        self.MaKienNghi = MaKienNghi
        self.NguoiLamDon = NguoiLamDon
        self.NoiDung = NoiDung
        self.NgayKN = NgayKN
        self.TrangThai = TrangThai