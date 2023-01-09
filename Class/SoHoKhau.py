import Person
class SoHoKhau:
    def __init__(self, SOHOKHAU, ChuHo: Person, SoNha, Duong, Phuong, Quan):
        self.SoHoKhau = SOHOKHAU
        self.TenChuHo = ChuHo.Ten
        self.ChuHo = ChuHo
        self.SoNha = SoNha
        self.Duong = Duong
        self.Phuong = Phuong
        self.Quan = Quan