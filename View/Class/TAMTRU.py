import datetime
class TAMTRU:
    def __init__(self, MaGiayTamTru, ID ,HoTen, CCCD, QueQuan, DiaChiTamTru, Tu: datetime.datetime, den: datetime.datetime, LyDo, NgayLamDon: datetime.datetime):
        self.MaGiayTamTru = MaGiayTamTru
        self.ID = ID
        self.HoTen = HoTen
        self.CCCD = CCCD
        self.queQuan = QueQuan
        self.DiaChiTamTru = DiaChiTamTru
        self.Tu = Tu
        self.den = den
        self.LyDo = LyDo
        self.NgayLamDon =NgayLamDon