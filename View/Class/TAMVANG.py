
import datetime


class TAMVANG:
    def __init__(self, MaGiayTamTru, ID, HoTen, CCCD,  NoiTamVang, Tu: datetime.datetime, Den: datetime.datetime, LyDo, NgayLamDon: datetime.datetime):
        self.MaGiayTamTru = MaGiayTamTru
        self.ID = ID
        self.HoTen = HoTen
        self.CCCD = CCCD
        self.NoiTamVang = NoiTamVang
        self.Tu = Tu
        self.Den = Den
        self.LyDo = LyDo
        self.NgayLamDon = NgayLamDon

    def init_values(values):
        tamvang = TAMVANG(values[0], values[1], values[2], values[3],
                          values[4], values[5], values[6], values[7], values[8])
        return tamvang
