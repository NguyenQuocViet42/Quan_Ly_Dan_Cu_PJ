import datetime

class TraLoiKienNGhi:
    def __init__(self, MaTraLoi, MaKienNghi, NoiDung, NgayTraLoi: datetime.datetime, TrangThai, TenNguoiTraLoi):
        self.MaTraLoi = MaTraLoi
        self.MaKienNghi = MaKienNghi
        self.NoiDung = NoiDung
        self.NgayTraLoi = NgayTraLoi
        self.TrangThai = TrangThai
        self.TenNguoiTraLoi = TenNguoiTraLoi