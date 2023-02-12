import datetime


class TAMTRU:
    def __init__(self, MaGiayTamTru, ID, HoTen, CCCD, QueQuan, DiaChiTamTru, Tu: datetime.datetime, Den: datetime.datetime, LyDo, NgayLamDon: datetime.datetime):
        self.MaGiayTamTru = MaGiayTamTru
        self.ID = ID
        self.HoTen = HoTen
        self.CCCD = CCCD
        self.queQuan = QueQuan
        self.DiaChiTamTru = DiaChiTamTru
        self.Tu = Tu
        self.Den = Den
        self.LyDo = LyDo
        self.NgayLamDon = NgayLamDon

    def init_values(values):
        tamtru = TAMTRU(values[0], values[1], values[2], values[3],
                        values[4], values[5], values[6], values[7], values[8], values[9])
        return tamtru
