# import required modules
import pyodbc

# create connection object
mydb = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-H9AI1NN1;'
                      'Database=QLCUDAN;'
                      'Trusted_Connection=yes;')

# create cursor object
cursor = mydb.cursor()


def getAllHoKhau():
    query = "SELECT * FROM SOHOKHAU"
    cursor.execute(query)
    return cursor.fetchall()

# Thêm nhân khẩu mới
def insertCUDAN(values):
    query = "INSERT INTO CUDAN (CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, MaSo, QuanHe, NgayDangKyThuongTru, DiaChiCu, NgayChuyenDi, NoiChuyenDi, GhiChu) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, None, None, None)"
    cursor.execute(query, values)
    mydb.commit()

# Lấy thông tin cư dân
def getCUDAN(ID):
    query = "select CUDAN.* from CUDAN where CUDAN.ID = ?"
    val = (ID,)
    # biến truyền vào dưới dạng 1 mảng
    cursor.execute(query, val)
    return cursor.fetchall()
#Lấy thông tin hộ khẩu
def getHoKhau(hostId):
    query = "SELECT * FROM SOHOKHAU WHERE  MaSo = ?"
    val = (hostId,)
    cursor.execute(query, val)
    return cursor.fetchall()
# Lấy danh sách ID cư dân thuộc hộ khẩu
def getListCuDanFromHoKhau(MaSo):
    query = "select ID from CUDAN where MaSo = ?"
    val = (MaSo,)
    cursor.execute(query,val)
    return cursor.fetchall()
# Thêm vào bảng Biến Đổi
def insertBienDoi(KieuBienDoi, NoiDungBienDoi, MaSo):
    query = "insert into BIENDOI values (getdate(), ?, ?, ?)"
    val = (KieuBienDoi, NoiDungBienDoi, MaSo)
    cursor.execute(query, val)
    mydb.commit()
    
# Khi có Nhân khẩu chuyển đi
def updateCUDAN_ChuyenDi(ID, NgayChuyenDi, NoiChuyenDi, GhiChu):
    values = (NgayChuyenDi, NoiChuyenDi, GhiChu, ID)
    query = "UPDATE CUDAN SET NgayChuyenDi = ?, NoiChuyenDi = ?, GhiChu = ? WHERE ID =?"
    cursor.execute(query, values)
    mydb.commit()

# Thay đổi quan hệ trong hộ khẩu
def ThayDoiQuanHe(ID, QuanHeMoi):
    values = (QuanHeMoi, ID)
    query = "UPDATE CUDAN SET QuanHe = ? WHERE ID =?"
    cursor.execute(query, values)
    mydb.commit()