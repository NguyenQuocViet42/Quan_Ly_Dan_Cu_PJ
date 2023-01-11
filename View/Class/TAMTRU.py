import CUDAN
import datetime
class TAMTRU:
    def __init__(self, MaGiayTamTru ,NguoiLamDon: CUDAN, DiaChiTamTru, Tu: datetime.datetime, den: datetime.datetime, LyDo, NgayLamDon: datetime.datetime):
        self.MaGiayTamTru = MaGiayTamTru
        self.NguoiLamDon = NguoiLamDon
        self.DiaChiTamTru = DiaChiTamTru
        self.Tu = Tu
        self.den = den
        self.LyDo = LyDo
        self.NgayLamDon =NgayLamDon