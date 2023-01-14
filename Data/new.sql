use QLCUDAN

select count(b1.MaKienNghi), COUNT(b2.MaKienNghi), COUNT(b3.MaKienNghi), COUNT(b4.MaKienNghi)
from KIENNGHI as b1, KIENNGHI as b2, KIENNGHI as b3, KIENNGHI as b4 
where b1.TrangThai = N'Mới ghi nhận' and b2.TrangThai = N'Chưa xử lý' and b3.TrangThai = N'Đã xử lý'
and b4.TrangThai = N'Đã thông báo'