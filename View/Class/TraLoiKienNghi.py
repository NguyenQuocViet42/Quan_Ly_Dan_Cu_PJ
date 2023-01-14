import datetime

class TraLoiKienNghi:
    def __init__(self, MaTraLoi, MaKienNghi, NoiDung, NgayTraLoi: datetime.datetime, TrangThai, TenNguoiTraLoi, IDQuanLy):
        self.MaTraLoi = MaTraLoi
        self.MaKienNghi = MaKienNghi
        self.NoiDung = NoiDung
        self.NgayTraLoi = NgayTraLoi
        self.TrangThai = TrangThai
        self.TenNguoiTraLoi = TenNguoiTraLoi
        self.IDQuanLy = IDQuanLy
        
    def init_values(values):
        TraLoi = TraLoiKienNghi(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
        return TraLoi