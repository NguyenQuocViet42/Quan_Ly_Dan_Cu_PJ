USE [master]
GO
/****** Object:  Database [QLCUDAN]    Script Date: 2/19/2023 8:56:56 PM ******/
CREATE DATABASE [QLCUDAN]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'QLCUDAN', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\QLCUDAN.mdf' , SIZE = 73728KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'QLCUDAN_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\QLCUDAN_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [QLCUDAN] SET COMPATIBILITY_LEVEL = 100
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [QLCUDAN].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [QLCUDAN] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [QLCUDAN] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [QLCUDAN] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [QLCUDAN] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [QLCUDAN] SET ARITHABORT OFF 
GO
ALTER DATABASE [QLCUDAN] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [QLCUDAN] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [QLCUDAN] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [QLCUDAN] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [QLCUDAN] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [QLCUDAN] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [QLCUDAN] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [QLCUDAN] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [QLCUDAN] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [QLCUDAN] SET  DISABLE_BROKER 
GO
ALTER DATABASE [QLCUDAN] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [QLCUDAN] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [QLCUDAN] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [QLCUDAN] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [QLCUDAN] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [QLCUDAN] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [QLCUDAN] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [QLCUDAN] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [QLCUDAN] SET  MULTI_USER 
GO
ALTER DATABASE [QLCUDAN] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [QLCUDAN] SET DB_CHAINING OFF 
GO
ALTER DATABASE [QLCUDAN] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [QLCUDAN] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [QLCUDAN] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [QLCUDAN] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'QLCUDAN', N'ON'
GO
ALTER DATABASE [QLCUDAN] SET QUERY_STORE = ON
GO
ALTER DATABASE [QLCUDAN] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [QLCUDAN]
GO
/****** Object:  Table [dbo].[BangGopKienNghi]    Script Date: 2/19/2023 8:56:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BangGopKienNghi](
	[MaKienNghi] [int] NULL,
	[DanhSachHoTen] [nvarchar](max) NULL,
	[DanhSachCCCD] [nvarchar](max) NULL,
	[SoLuong] [int] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BIENDOI]    Script Date: 2/19/2023 8:56:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BIENDOI](
	[MaBienDoi] [int] IDENTITY(1,1) NOT NULL,
	[Ngay] [date] NULL,
	[KieuBienDoi] [nvarchar](50) NULL,
	[NoiDungBienDoi] [nvarchar](max) NULL,
	[MaSo] [int] NULL,
	[IDQuanLy] [varchar](15) NULL,
 CONSTRAINT [PK_BIENDOI] PRIMARY KEY CLUSTERED 
(
	[MaBienDoi] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CUDAN]    Script Date: 2/19/2023 8:56:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CUDAN](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[CCCD] [nvarchar](20) NULL,
	[HoTen] [nvarchar](50) NOT NULL,
	[GioiTinh] [nvarchar](5) NOT NULL,
	[NgaySinh] [date] NULL,
	[DanToc] [nvarchar](20) NOT NULL,
	[QuocTich] [nvarchar](50) NOT NULL,
	[NgheNghiep] [nvarchar](50) NULL,
	[QueQuan] [nvarchar](max) NULL,
	[BiDanh] [nvarchar](50) NULL,
	[MaSo] [int] NOT NULL,
	[QuanHe] [nvarchar](50) NOT NULL,
	[NgayDangKyThuongTru] [date] NULL,
	[DiaChiCu] [nvarchar](100) NULL,
	[NgayChuyenDi] [date] NULL,
	[NoiChuyenDi] [nvarchar](100) NULL,
	[GhiChu] [nvarchar](50) NULL,
 CONSTRAINT [PK_CUDAN] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DANGNHAP]    Script Date: 2/19/2023 8:56:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DANGNHAP](
	[IDQuanLy] [varchar](15) NOT NULL,
	[MatKhau] [nvarchar](30) NOT NULL,
	[TenQuanLy] [nvarchar](50) NULL,
 CONSTRAINT [PK_DANGNHAP] PRIMARY KEY CLUSTERED 
(
	[IDQuanLy] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[KIENNGHI]    Script Date: 2/19/2023 8:56:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KIENNGHI](
	[MaKienNghi] [int] IDENTITY(1,1) NOT NULL,
	[ID] [int] NOT NULL,
	[CCCD] [varchar](12) NOT NULL,
	[NoiDung] [nvarchar](max) NULL,
	[NgayKN] [datetime] NOT NULL,
	[PhanLoai] [nvarchar](20) NULL,
	[TrangThai] [nvarchar](20) NULL,
 CONSTRAINT [PK_KIENNGHI] PRIMARY KEY CLUSTERED 
(
	[MaKienNghi] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SOHOKHAU]    Script Date: 2/19/2023 8:56:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SOHOKHAU](
	[MaSo] [int] NOT NULL,
	[SoThanhVien] [int] NOT NULL,
	[SoNha/TenDuong] [nvarchar](max) NULL,
	[Phuong/Xa] [nvarchar](50) NOT NULL,
	[Quan/Huyen] [nvarchar](50) NOT NULL,
	[Tinh] [nvarchar](50) NOT NULL,
	[IDChuHo] [int] NOT NULL,
 CONSTRAINT [PK_SOHOKHAU] PRIMARY KEY CLUSTERED 
(
	[MaSo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TAMTRU]    Script Date: 2/19/2023 8:56:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TAMTRU](
	[MaGiayTamTru] [int] IDENTITY(1,1) NOT NULL,
	[ID] [int] NOT NULL,
	[HoTen] [nvarchar](50) NULL,
	[CCCD] [varchar](12) NOT NULL,
	[QueQuan] [nvarchar](50) NULL,
	[DiaChiTamTru] [nvarchar](100) NULL,
	[Tu] [date] NOT NULL,
	[Den] [date] NOT NULL,
	[LyDo] [nvarchar](max) NULL,
	[NgayLamDon] [date] NOT NULL,
 CONSTRAINT [PK_TAMTRU] PRIMARY KEY CLUSTERED 
(
	[MaGiayTamTru] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TAMVANG]    Script Date: 2/19/2023 8:56:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TAMVANG](
	[MaGiayTamVang] [int] IDENTITY(1,1) NOT NULL,
	[ID] [int] NULL,
	[HoTen] [nvarchar](50) NOT NULL,
	[CCCD] [varchar](12) NOT NULL,
	[NoiTamVang] [nvarchar](100) NULL,
	[Tu] [date] NOT NULL,
	[Den] [date] NOT NULL,
	[LyDo] [nvarchar](max) NOT NULL,
	[NgayLamDon] [date] NOT NULL,
 CONSTRAINT [PK_TAMVANG] PRIMARY KEY CLUSTERED 
(
	[MaGiayTamVang] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TraLoiKienNghi]    Script Date: 2/19/2023 8:56:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TraLoiKienNghi](
	[MaTraLoi] [int] IDENTITY(1,1) NOT NULL,
	[MaKienNghi] [int] NULL,
	[NoiDung] [nvarchar](max) NULL,
	[NgayTraLoi] [date] NULL,
	[TrangThai] [nvarchar](20) NULL,
	[TenNguoiTraLoi] [nvarchar](50) NULL,
	[IDQuanLy] [varchar](15) NULL,
 CONSTRAINT [PK_TraLoiKienNghi] PRIMARY KEY CLUSTERED 
(
	[MaTraLoi] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
INSERT [dbo].[BangGopKienNghi] ([MaKienNghi], [DanhSachHoTen], [DanhSachCCCD], [SoLuong]) VALUES (30, N'Nguyễn Quốc Việt,Nguyễn Khánh Duy', N'001202008652,001202031426', 3)
INSERT [dbo].[BangGopKienNghi] ([MaKienNghi], [DanhSachHoTen], [DanhSachCCCD], [SoLuong]) VALUES (32, N'Nguyễn Quốc Việt,Nguyễn Khánh Duy', N'001202008652,001202031426', 2)
GO
SET IDENTITY_INSERT [dbo].[BIENDOI] ON 

INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (43, CAST(N'2023-02-13' AS Date), N'Thêm nhân khẩu mới', N'Thêm nhân khẩu Nguyễn Bá Phúc 001201004678 vào hộ khẩu 999999999', 999999999, N'totruong08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (44, CAST(N'2023-02-13' AS Date), N'Cấp giấy tạm trú', N'Cấp giấy tạm trú cho cư dân Nguyễn Bá Phúc, số căn cước 001201004678 từ ngày 02/13/23 đến ngày 02/24/23 tại 16 Đ. Phùng Hưng, P. Phúc La, Hà Đông, Hà Nội', 250000014, N'totruong08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (45, CAST(N'2023-02-13' AS Date), N'Cấp giấy tạm vắng', N'Cấp giấy tạm vắng cho cư dân Nguyễn Bá Phúc, số căn cước 001201004678 từ ngày 02/13/23 đến ngày 02/24/23', 250000014, N'totruong08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (46, CAST(N'2023-02-13' AS Date), N'Thêm nhân khẩu mới', N'Thêm nhân khẩu Nguyễn Quốc Việt 001202031426 vào hộ khẩu 999999999', 999999999, N'totruong08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (47, CAST(N'2023-02-13' AS Date), N'Cấp giấy tạm trú', N'Cấp giấy tạm trú cho cư dân Nguyễn Quốc Việt, số căn cước 001202031426 từ ngày 02/13/23 đến ngày 02/23/23 tại Hoàng Văn Thụ, Hoàng Mai, Hà Nội', 100000001, N'totruong08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (48, CAST(N'2023-02-13' AS Date), N'Thêm nhân khẩu mới', N'Thêm nhân khẩu Nguyễn Anh Vũ 001205004707 vào hộ khẩu 999999999', 999999999, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (49, CAST(N'2023-02-13' AS Date), N'Cấp giấy tạm trú', N'Cấp giấy tạm trú cho cư dân Nguyễn Anh Vũ, số căn cước 001205004707 từ ngày 02/13/23 đến ngày 02/24/23 tại Đại La, Hà Nội', 250000014, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (50, CAST(N'2023-02-13' AS Date), N'Cấp giấy tạm vắng', N'Cấp giấy tạm vắng cho cư dân Nguyễn Anh Vũ, số căn cước 001205004707 từ ngày 02/13/23 đến ngày 02/23/23', 250000014, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (51, CAST(N'2023-02-13' AS Date), N'Cấp giấy tạm vắng', N'Cấp giấy tạm vắng cho cư dân Nguyễn Hoàng Anh, số căn cước 001200000033 từ ngày 02/13/23 đến ngày 02/09/24', 250000009, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (53, CAST(N'2023-02-13' AS Date), N'Tách hộ khẩu', N'Sổ hộ khẩu 240000003 được tách thành 2 sổ hộ khẩu mới là: 240000003 và 247306090', 240000003, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (54, CAST(N'2023-02-13' AS Date), N'Tách hộ khẩu', N'Sổ hộ khẩu 240000005 được tách thành 2 sổ hộ khẩu mới là: 240000005 và 250019781', 240000005, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (58, CAST(N'2023-02-19' AS Date), N'Thêm nhân khẩu mới', N'Thêm nhân khẩu Nguyễn Khánh Duy 001202008652 vào hộ khẩu 240000002', 240000002, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (59, CAST(N'2023-02-19' AS Date), N'Thêm nhân khẩu mới', N'Thêm nhân khẩu Nguyễn Khánh Duy 001202008653 vào hộ khẩu 240000001', 240000001, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (60, CAST(N'2023-02-19' AS Date), N'Thêm nhân khẩu mới', N'Thêm nhân khẩu Nguyễn Con Trai 001202008655 vào hộ khẩu 240000002', 240000002, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (61, CAST(N'2023-02-19' AS Date), N'Thêm nhân khẩu mới', N'Thêm nhân khẩu Nguyễn Thị Lan 001202031427 vào hộ khẩu 240000001', 240000001, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (62, CAST(N'2023-02-19' AS Date), N'Thêm nhân khẩu mới', N'Thêm nhân khẩu Nguyễn Khánh Duy 001202008652 vào hộ khẩu 240000001', 240000001, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (63, CAST(N'2023-02-19' AS Date), N'Cấp giấy tạm trú', N'Cấp giấy tạm trú cho cư dân Nguyễn Khánh Duy, số căn cước 001202008652 từ ngày 02/19/23 đến ngày 02/19/23 tại Hà Nội', 240000001, N'captren08')
INSERT [dbo].[BIENDOI] ([MaBienDoi], [Ngay], [KieuBienDoi], [NoiDungBienDoi], [MaSo], [IDQuanLy]) VALUES (64, CAST(N'2023-02-19' AS Date), N'Thêm nhân khẩu mới', N'Thêm nhân khẩu Nguyễn Khánh Duy 001202008652 vào hộ khẩu 240000001', 240000001, N'captren08')
SET IDENTITY_INSERT [dbo].[BIENDOI] OFF
GO
SET IDENTITY_INSERT [dbo].[CUDAN] ON 

INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (2, N'001078000015', N'Hoàng Văn Thụ', N'Nam', CAST(N'1978-08-09' AS Date), N'Kinh', N'Việt Nam', NULL, N'Hà Nội', NULL, 240000004, N'Chủ hộ', CAST(N'1990-06-02' AS Date), N'46 Nguyễn Thị Định, Trung Hòa, Cầu Giấy, Hà Nội', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (3, N'001080000001', N'Nguyễn Văn Hà', N'Nam', CAST(N'1980-11-15' AS Date), N'Kinh', N'Việt Nam', N'Viên Chức', N'Thanh Hóa', N'Hà', 240000001, N'Chủ hộ', CAST(N'2002-05-04' AS Date), N'Quảng Tiến, Sầm Sơn, Thanh Hóa', CAST(N'2023-09-01' AS Date), N'Thạch Thất, Hà Nội', N'Về quê')
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (4, N'001090000023', N'Nguyễn Văn Trỗi', N'Nam', CAST(N'1990-07-26' AS Date), N'Kinh', N'Việt Nam', N'Công nhân', N'Hà Nội', NULL, 240000006, N'Chủ hộ', CAST(N'2010-12-12' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (5, N'001098000037', N'Bùi Kỳ Anh', N'Nam', CAST(N'1998-08-24' AS Date), N'Kinh', N'Việt Nam', N'Nhân Viên', N'Hà Nội', NULL, 250000011, N'Chủ hộ', CAST(N'2012-08-14' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (6, N'001178000016', N'Nguyễn Thị Bạch Mai', N'Nữ', CAST(N'1978-03-11' AS Date), N'Kinh', N'Việt Nam', N'Viên chức', N'Hà Nội', NULL, 240000004, N'Vợ', CAST(N'1990-06-02' AS Date), N'48 Nguyễn Thị Định, Trung Hòa, Cầu Giấy, Hà Nội', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (7, N'001182000288', N'Hà Thị Thanh Huyền', N'Nữ', CAST(N'1982-12-07' AS Date), N'Kinh', N'Việt Nam', N'Giảng Viên', N'Hà Nội', N'Hà Huyềnn', 250000014, N'Vợ', CAST(N'2000-12-03' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (8, N'001198000026', N'Lê Thanh Thúy', N'Nữ', CAST(N'1998-09-12' AS Date), N'Kinh', N'Việt Nam', N'Bác Sĩ', N'Hà Nội', NULL, 240000007, N'Chủ hộ', CAST(N'2020-03-18' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (9, N'001200000033', N'Nguyễn Hoàng Anh', N'Nam', CAST(N'2000-12-06' AS Date), N'Kinh', N'Việt Nam', N'Công Nhân', N'Hà Nội', NULL, 250000009, N'Con 1', CAST(N'2000-12-06' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (10, N'001201004678', N'Nguyễn Bá Phúc', N'Nam', CAST(N'2001-01-01' AS Date), N'Kinh', N'Việt Nam', N'Sinh Viên', N'Hà Nội', NULL, 250000014, N'Con 1', CAST(N'2001-01-01' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (12, N'001202004647', N'Nguyễn Khánh Duy', N'Nam', CAST(N'2002-07-15' AS Date), N'Kinh', N'Việt Nam', N'Sinh Viên', N'Hà Nội', NULL, 250000014, N'Con 2', CAST(N'2002-07-15' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (13, N'001203000017', N'Hoàng Văn Xuân', N'Nam', CAST(N'2003-04-19' AS Date), N'Kinh', N'Việt Nam', N'Sinh Viên', N'Hà Nội', NULL, 240000004, N'Con 1', CAST(N'2003-04-19' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (14, N'001205004707', N'Nguyễn Anh Vũ', N'Nam', CAST(N'2004-05-28' AS Date), N'Kinh', N'Việt Nam', N'Sinh Viên', N'Hà Nội', N'Dũ', 250000014, N'Con 3', CAST(N'2004-05-28' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (15, N'001210000034', N'Nguyễn Việt Nam', N'Nam', CAST(N'2010-08-25' AS Date), N'Kinh', N'Việt Nam', N'Học Sinh', N'Hà Nội', NULL, 250000009, N'Con 2', CAST(N'2010-08-25' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (16, N'001218000022', N'Bàn Văn Anh', N'Nam', CAST(N'2018-12-31' AS Date), N'Tày', N'Việt Nam', NULL, N'Bắc Kạn', NULL, 240000005, N'Con 2', CAST(N'2018-12-31' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (17, N'001218000043', N'Lương Hoàng Khánh', N'Nam', CAST(N'2018-12-02' AS Date), N'Kinh', N'Việt Nam', N'Học Sinh', N'Hà Nội', NULL, 250000012, N'Con 2', CAST(N'2018-12-02' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (18, N'001300000036', N'Nguyễn Ánh Dương', N'Nữ', CAST(N'2000-11-18' AS Date), N'Kinh', N'Việt Nam', N'Nhân Viên', N'Hà Nội', NULL, 250000010, N'Vợ', CAST(N'2010-10-06' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (19, N'001302000038', N'Hoàng Anh', N'Nữ', CAST(N'2002-06-02' AS Date), N'Kinh', N'Việt Nam', N'Sinh Viên', N'Hà Nội', NULL, 250000011, N'Vợ', CAST(N'2012-08-14' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (20, N'001305000005', N'Nguyễn Hoàng Lan', N'Nữ', CAST(N'2005-12-03' AS Date), N'Kinh', N'Việt Nam', N'Học Sinh', N'Hà Nội', NULL, 240000001, N'Con 1', CAST(N'2005-12-03' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (21, N'001308000006', N'Nguyễn Thị Thơ', N'Nữ', CAST(N'2008-08-07' AS Date), N'Kinh', N'Việt Nam', N'Học Sinh', N'Hà Nội', NULL, 240000001, N'Con 2', CAST(N'2008-08-07' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (22, N'001310000018', N'Hoàng Anh', N'Nữ', CAST(N'2010-12-30' AS Date), N'Kinh', N'Việt Nam', N'Học Sinh', N'Hà Nội', NULL, 240000004, N'Con 2', CAST(N'2010-12-30' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (23, N'001312000021', N'Bàn Thị Tuyết', N'Nữ', CAST(N'2012-02-19' AS Date), N'Nùng', N'Việt Nam', N'Học Sinh', N'Bắc Kạn', NULL, 250019781, N'Con 1', CAST(N'2017-09-13' AS Date), N'Tổ 13, Sông Cầu, tp. Bắc Kạn, Bắc Kạn', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (24, N'001312000042', N'Lương Minh Hạnh', N'Nữ', CAST(N'2012-05-14' AS Date), N'Kinh', N'Việt Nam', N'Học Sinh', N'Hà Nội', NULL, 250000012, N'Con 1', CAST(N'2012-05-14' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (25, N'001316000025', N'Nguyễn Xuân Mai', N'Nữ', CAST(N'2015-10-10' AS Date), N'Kinh', N'Việt Nam', N'Học Sinh', N'Hà Nội', NULL, 240000006, N'Con 1', CAST(N'2015-10-10' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (26, N'001322000039', N'Bùi Thanh Mai', N'Nữ', CAST(N'2022-09-23' AS Date), N'Kinh', N'Việt Nam', N'', N'Hà Nội', N'', 250000011, N'Con 1', CAST(N'2022-09-23' AS Date), N'', CAST(N'2023-02-13' AS Date), N'', NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (27, N'002182000002', N'Vũ Thị Ánh Kim', N'Nữ', CAST(N'1982-03-12' AS Date), N'Kinh', N'Việt Nam', N'Bán Hàng', N'Hà Giang', NULL, 240000001, N'Vợ', CAST(N'2002-05-04' AS Date), N'Việt Lâm, Vị Xuyên, Hà Giang', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (28, N'004084000028', N'Hà Thị Lựu', N'Nữ', CAST(N'1984-08-13' AS Date), N'Mông', N'Việt Nam', N'Bán Hàng', N'Cao Bằng', NULL, 240000008, N'Vợ', CAST(N'2008-12-08' AS Date), N'Sông Hiến, tx. Cao Bằng, Cao Bằng', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (29, N'004085000027', N'Lò Văn Sơn', N'Nam', CAST(N'1985-11-21' AS Date), N'Mông', N'Việt Nam', N'Bác Sĩ', N'Cao Bằng', NULL, 240000008, N'Chủ hộ', CAST(N'2008-12-08' AS Date), N'Sông Hiến, tx. Cao Bằng, Cao Bằng', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (30, N'004185000008', N'Bùi Ánh Viên', N'Nữ', CAST(N'1985-05-16' AS Date), N'Nùng', N'Việt Nam', N'Vận Động Viên', N'Cao Bằng', NULL, 240000002, N'Chủ hộ', CAST(N'2003-09-12' AS Date), N'Đề Thám, tx. Cao Bằng, Cao Bằng', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (31, N'004310000029', N'Lò Thị Thái', N'Nữ', CAST(N'2010-05-31' AS Date), N'Mông', N'Việt Nam', N'Học Sinh', N'Cao Bằng', NULL, 240000008, N'Con 1', CAST(N'2010-05-31' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (32, N'004312000030', N'Lò Thị Thơm', N'Nữ', CAST(N'2012-08-27' AS Date), N'Mông', N'Việt Nam', N'Học Sinh', N'Cao Bằng', NULL, 240000008, N'Con 2', CAST(N'2012-08-27' AS Date), NULL, NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (33, N'006080000044', N'Hà Văn Duy', N'Nam', CAST(N'1980-03-21' AS Date), N'Tày', N'Việt Nam', N'Nông Dân', N'Bắc Kạn', NULL, 250000013, N'Chủ hộ', CAST(N'2015-10-24' AS Date), N'Nông Hạ, Chợ Mới, Bắc Kạn', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (34, N'006090000020', N'Bàn Văn Hoan', N'Nam', CAST(N'1990-09-23' AS Date), N'Tày', N'Việt Nam', N'Nông Dân', N'Bắc Kạn', NULL, 250019781, N'Chủ hộ', CAST(N'2017-09-13' AS Date), N'Tổ 13, Sông Cầu, tp. Bắc Kạn, Bắc Kạn', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (35, N'006182000045', N'Phạm Thị Hoan', N'Nữ', CAST(N'1982-12-03' AS Date), N'Tày', N'Việt Nam', N'Nông Dân', N'Bắc Kạn', NULL, 250000013, N'Vợ', CAST(N'2015-10-24' AS Date), N'Nông Hạ, Chợ Mới, Bắc Kạn', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (36, N'006188000019', N'Phan Thị Anh Thư', N'Nữ', CAST(N'1988-10-27' AS Date), N'Nùng', N'Việt Nam', N'Giáo Viên', N'Bắc Kạn', NULL, 240000005, N'Chủ hộ', CAST(N'2017-09-13' AS Date), N'Tổ 13, Sông Cầu, tp. Bắc Kạn, Bắc Kạn', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (37, N'006201000046', N'Hà Văn Thành', N'Nam', CAST(N'2001-09-06' AS Date), N'Tày', N'Việt Nam', N'Sinh Viên', N'Bắc Kạn', NULL, 250000013, N'Con 1', CAST(N'2015-10-24' AS Date), N'Nông Hạ, Chợ Mới, Bắc Kạn', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (38, N'006205000047', N'Hà Văn Thái', N'Nam', CAST(N'2005-09-09' AS Date), N'Tày', N'Việt Nam', N'Sinh Viên', N'Bắc Kạn', NULL, 250000013, N'Con 2', CAST(N'2015-10-24' AS Date), N'Nông Hạ, Chợ Mới, Bắc Kạn', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (39, N'008099000035', N'Phạm Văn Bắc', N'Nam', CAST(N'1999-09-13' AS Date), N'Thái', N'Việt Nam', N'Nhân Viên', N'Tuyên Quang', NULL, 250000010, N'Chủ hộ', CAST(N'2010-10-06' AS Date), N'An Khang, Yên Sơn, Tuyên Quang', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (40, N'019074000031', N'Nguyễn Hoàng Nu', N'Nam', CAST(N'1974-02-19' AS Date), N'Kinh', N'Việt Nam', N'Công chức', N'Thái Nguyên', NULL, 250000009, N'Chủ hộ', CAST(N'2000-02-14' AS Date), N'Tân Lập, tp. Thái NGuyên, Thái Nguyên', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (41, N'019175000032', N'Phạm Thị Thu Nga', N'Nữ', CAST(N'1975-04-29' AS Date), N'Kinh', N'Việt Nam', N'Viên Chức', N'Thái Nguyên', NULL, 250000009, N'Vợ', CAST(N'2000-02-14' AS Date), N'Tân Lập, tp. Thái NGuyên, Thái Nguyên', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (42, N'024060000010', N'Lê Minh Hùng', N'Nam', CAST(N'1960-11-09' AS Date), N'Kinh', N'Việt Nam', NULL, N'Bắc Giang', NULL, 240000003, N'Chủ hộ', CAST(N'2010-02-24' AS Date), N'Mai Trung, Hiệp Hòa, Bắc Giang', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (43, N'024080004704', N'Nguyễn Quốc Việt', N'Nam', CAST(N'1980-02-09' AS Date), N'Kinh', N'Việt Nam', N'Giảng Viên', N'Bắc Giang', N'Vịt', 250000014, N'Chủ hộ', CAST(N'2000-12-03' AS Date), N'Thạch Thất, Hà Nội', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (46, N'024192000041', N'Nguyễn Thanh Hiệp', N'Nữ', CAST(N'1992-12-18' AS Date), N'Kinh', N'Việt Nam', N'Bán Hàng', N'Bắc Giang', NULL, 250000012, N'Vợ', CAST(N'2010-07-26' AS Date), N'Trần Nguyên Hãn, tp. Bắc Giang, Bắc Giang', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (47, N'024201000014', N'Lê Minh Sơn', N'Nam', CAST(N'2010-09-12' AS Date), N'Kinh', N'Việt Nam', N'Học Sinh', N'Bắc Giang', NULL, 240000003, N'Cháu nội 1', CAST(N'2010-09-12' AS Date), N'Mai Trung, Hiệp Hòa, Bắc Giang', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (48, N'031192000013', N'Hoàng Thị Nga', N'Nữ', CAST(N'1992-12-03' AS Date), N'Kinh', N'Việt Nam', N'Viên Chức', N'Hải Phòng', NULL, 240000003, N'Con dâu 1', CAST(N'2010-02-24' AS Date), N'Mai Trung, Hiệp Hòa, Bắc Giang', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (49, N'035190000024', N'Lã Thị Lệ Hà', N'Nữ', CAST(N'1990-12-09' AS Date), N'Kinh', N'Việt Nam', N'Giáo Viên', N'Hà Nam', NULL, 240000006, N'Vợ', CAST(N'2010-12-12' AS Date), N'Hai Bà Trưng, Phủ Lý, Hà Nam', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (50, N'038045000003', N'Nguyễn Văn Túy', N'Nam', CAST(N'1945-07-12' AS Date), N'Kinh', N'Việt Nam', NULL, N'Thanh Hóa', NULL, 240000001, N'Bố', CAST(N'2002-05-04' AS Date), N'Quảng Tiến, Sầm Sơn, Thanh Hóa', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (51, N'038150000004', N'Hoàng Thị Ánh', N'Nữ', CAST(N'1950-09-03' AS Date), N'Kinh', N'Việt Nam', NULL, N'Thanh Hóa', NULL, 240000001, N'Mẹ', CAST(N'2002-05-04' AS Date), N'Quảng Tiến, Sầm Sơn, Thanh Hóa', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (52, N'040090000040', N'Lương Văn Hòa', N'Nam', CAST(N'1990-11-30' AS Date), N'Kinh', N'Việt Nam', N'Nông Dân', N'Nghệ An', NULL, 250000012, N'Chủ hộ', CAST(N'2010-07-26' AS Date), N'Mỹ Sơn, Đô Lương, Nghệ An', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (58, N'001202031426', N'Nguyễn Quốc Việt', N'Nam', CAST(N'2002-11-15' AS Date), N'Kinh', N'viet Nam', NULL, N'Hanoi', N'Tony', 100000001, N'Chủ Hộ', CAST(N'2002-11-15' AS Date), N'Mới Sinh', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (68, N'Mới Sinh', N'Nguyễn Quốc', N'Nam', CAST(N'2023-01-10' AS Date), N'Kinh', N'Việt Nam', N'Mới Sinh', N'Hà Nội', N'No', 100000001, N'Con', CAST(N'2023-01-10' AS Date), N'Mới Sinh', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (69, N'0728347283', N'Vũ Văn Lợi', N'Nam', CAST(N'2023-02-06' AS Date), N'Kinh', N'Việt Nam', N'Tạm Trú', N'Ninh Bình', N'NULL', 999999999, N'Tạm Trú', CAST(N'2023-02-06' AS Date), N'Ninh Bình', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (74, N'001201004678', N'Nguyễn Bá Phúc', N'Nam', CAST(N'2023-02-13' AS Date), N'Kinh', N'Việt Nam', N'Tạm Trú', N'16 Đ. Phùng Hưng, P. Phúc La, Hà Đông, Hà Nội', N'NULL', 999999999, N'Tạm Trú', CAST(N'2023-02-13' AS Date), N'16 Đ. Phùng Hưng, P. Phúc La, Hà Đông, Hà Nội', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (75, N'001202031426', N'Nguyễn Quốc Việt', N'Nam', CAST(N'2023-02-13' AS Date), N'Kinh', N'Việt Nam', N'Tạm Trú', N'Thạch Thất Hà Nội', N'NULL', 999999999, N'Tạm Trú', CAST(N'2023-02-13' AS Date), N'Thạch Thất Hà Nội', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (76, N'001205004707', N'Nguyễn Anh Vũ', N'Nam', CAST(N'2023-02-13' AS Date), N'Kinh', N'Việt Nam', N'Tạm Trú', N'Bắc Kạn', N'NULL', 999999999, N'Tạm Trú', CAST(N'2023-02-13' AS Date), N'Bắc Kạn', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (80, N'001202008655', N'Nguyễn Con Trai', N'Nam', CAST(N'2023-02-19' AS Date), N'Kinh', N'Việt Nam', N'Sinh viên', N'Nam Định', N'Không có', 240000002, N'con trai', CAST(N'2023-02-19' AS Date), N'Nam Định', NULL, NULL, NULL)
INSERT [dbo].[CUDAN] ([ID], [CCCD], [HoTen], [GioiTinh], [NgaySinh], [DanToc], [QuocTich], [NgheNghiep], [QueQuan], [BiDanh], [MaSo], [QuanHe], [NgayDangKyThuongTru], [DiaChiCu], [NgayChuyenDi], [NoiChuyenDi], [GhiChu]) VALUES (81, N'001202031427', N'Nguyễn Thị Lan', N'Nữ', CAST(N'2002-02-01' AS Date), N'Kinh', N'Việt Nam', N'Sinh viên', N'Hà Nội', N'', 240000001, N'Con gái', CAST(N'2023-02-19' AS Date), N'Nam Định', NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[CUDAN] OFF
GO
INSERT [dbo].[DANGNHAP] ([IDQuanLy], [MatKhau], [TenQuanLy]) VALUES (N'captren08', N'vietdeptrai', N'Nguyễn Quốc Việt')
INSERT [dbo].[DANGNHAP] ([IDQuanLy], [MatKhau], [TenQuanLy]) VALUES (N'topho08', N'vietdeptrai', N'Nguyễn Khánh Duy')
INSERT [dbo].[DANGNHAP] ([IDQuanLy], [MatKhau], [TenQuanLy]) VALUES (N'totruong08', N'vietdeptrai', N'Nguyễn Anh Vũ')
GO
SET IDENTITY_INSERT [dbo].[KIENNGHI] ON 

INSERT [dbo].[KIENNGHI] ([MaKienNghi], [ID], [CCCD], [NoiDung], [NgayKN], [PhanLoai], [TrangThai]) VALUES (35, 58, N'001202031426', N'Nội dung kiến nghị thứ nhất', CAST(N'2023-02-13T00:00:00.000' AS DateTime), N'Nhà đất', N'Mới ghi nhận')
INSERT [dbo].[KIENNGHI] ([MaKienNghi], [ID], [CCCD], [NoiDung], [NgayKN], [PhanLoai], [TrangThai]) VALUES (37, 58, N'001202031426', N'Kiến nghị thứ 3	', CAST(N'2023-02-13T00:00:00.000' AS DateTime), N'bồi thường', N'Mới ghi nhận')
INSERT [dbo].[KIENNGHI] ([MaKienNghi], [ID], [CCCD], [NoiDung], [NgayKN], [PhanLoai], [TrangThai]) VALUES (38, 9, N'001200000033', N'Nội dung kiến nghị thứ nhất của Nguyễn Hoàng Anh	', CAST(N'2023-02-13T00:00:00.000' AS DateTime), N'môi trường', N'Đã thông báo')
INSERT [dbo].[KIENNGHI] ([MaKienNghi], [ID], [CCCD], [NoiDung], [NgayKN], [PhanLoai], [TrangThai]) VALUES (39, 9, N'001200000033', N'Nội dung kiến nghị thứ 2 của Nguyễn Hoàng Anh	', CAST(N'2023-02-13T00:00:00.000' AS DateTime), N'Ô Nhiễm môi trường', N'Mới ghi nhận')
INSERT [dbo].[KIENNGHI] ([MaKienNghi], [ID], [CCCD], [NoiDung], [NgayKN], [PhanLoai], [TrangThai]) VALUES (41, 14, N'001205004707', N'Nội dung kiến nghị thứ nhất của Nguyễn Anh Vũ	', CAST(N'2023-02-13T00:00:00.000' AS DateTime), N'Công việc', N'Mới ghi nhận')
INSERT [dbo].[KIENNGHI] ([MaKienNghi], [ID], [CCCD], [NoiDung], [NgayKN], [PhanLoai], [TrangThai]) VALUES (42, 14, N'001205004707', N'Nội dung kiến nghị thứ 2 của Nguyễn Anh Vũ	', CAST(N'2023-02-13T00:00:00.000' AS DateTime), N'Đất đai', N'Mới ghi nhận')
INSERT [dbo].[KIENNGHI] ([MaKienNghi], [ID], [CCCD], [NoiDung], [NgayKN], [PhanLoai], [TrangThai]) VALUES (43, 10, N'001201004678', N'Nội dung kiến nghị thứ nhất của Nguyễn Bá Phúc', CAST(N'2023-02-13T00:00:00.000' AS DateTime), N'ô nhiễm không khí', N'Mới ghi nhận')
INSERT [dbo].[KIENNGHI] ([MaKienNghi], [ID], [CCCD], [NoiDung], [NgayKN], [PhanLoai], [TrangThai]) VALUES (44, 10, N'001201004678', N'Nội dung kiến nghị thứ 2 của Nguyễn Bá Phúc', CAST(N'2023-02-13T00:00:00.000' AS DateTime), N'ô nhiễm tiếng ồn', N'Mới ghi nhận')
INSERT [dbo].[KIENNGHI] ([MaKienNghi], [ID], [CCCD], [NoiDung], [NgayKN], [PhanLoai], [TrangThai]) VALUES (45, 58, N'001202031426', N'Kiến nghị của Nguyễn Quốc Việt	', CAST(N'2023-02-13T00:00:00.000' AS DateTime), N'test', N'Mới ghi nhận')
SET IDENTITY_INSERT [dbo].[KIENNGHI] OFF
GO
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (100000001, 2, N'Số 1', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (240000001, 2, N'Số 1 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (240000002, 2, N'số 7 La Khê', N'xã La Khê', N'phường La Khê', N'tỉnh La Khê', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (240000003, 2, N'Số 164 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (240000004, 2, N'Số 42 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (240000005, 2, N'Tầng 1 số 52 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (240000006, 2, N'Số 2 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (240000007, 2, N'Số 323 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (240000008, 2, N'Số 123 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (250000009, 2, N'Số 62 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (250000010, 2, N'Số 87 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (250000011, 2, N'Số 123 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (250000012, 2, N'Tầng 3 số 52 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (250000013, 2, N'Số 200 tổ 7', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (250000014, 2, N'Số 1 Giải Phóng', N'Bách Khoa', N'Hai Bà Trưng', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (250019781, 2, N'số nhà 2', N'phường 2', N'huyện 2', N'tỉnh 2', 34)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (655646080, 2, N'Số 2', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
INSERT [dbo].[SOHOKHAU] ([MaSo], [SoThanhVien], [SoNha/TenDuong], [Phuong/Xa], [Quan/Huyen], [Tinh], [IDChuHo]) VALUES (999999999, 2, N'Tạm Trú', N'La Khê', N'Hà Đông', N'Hà Nội', 36)
GO
SET IDENTITY_INSERT [dbo].[TAMTRU] ON 

INSERT [dbo].[TAMTRU] ([MaGiayTamTru], [ID], [HoTen], [CCCD], [QueQuan], [DiaChiTamTru], [Tu], [Den], [LyDo], [NgayLamDon]) VALUES (3, 10, N'Nguyễn Bá Phúc', N'001201004678', N'16 Đ. Phùng Hưng, P. Phúc La, Hà Đông, Hà Nội', N'16 Đ. Phùng Hưng, P. Phúc La, Hà Đông, Hà Nội', CAST(N'2023-02-13' AS Date), CAST(N'2023-02-24' AS Date), N'Đi du lịch', CAST(N'2023-02-13' AS Date))
INSERT [dbo].[TAMTRU] ([MaGiayTamTru], [ID], [HoTen], [CCCD], [QueQuan], [DiaChiTamTru], [Tu], [Den], [LyDo], [NgayLamDon]) VALUES (4, 58, N'Nguyễn Quốc Việt', N'001202031426', N'Thạch Thất Hà Nội', N'Hoàng Văn Thụ, Hoàng Mai, Hà Nội', CAST(N'2023-02-13' AS Date), CAST(N'2023-02-23' AS Date), N'Học đại học', CAST(N'2023-02-13' AS Date))
INSERT [dbo].[TAMTRU] ([MaGiayTamTru], [ID], [HoTen], [CCCD], [QueQuan], [DiaChiTamTru], [Tu], [Den], [LyDo], [NgayLamDon]) VALUES (5, 14, N'Nguyễn Anh Vũ', N'001205004707', N'Bắc Kạn', N'Đại La, Hà Nội', CAST(N'2023-02-13' AS Date), CAST(N'2023-02-24' AS Date), N'Học đại học', CAST(N'2023-02-13' AS Date))
SET IDENTITY_INSERT [dbo].[TAMTRU] OFF
GO
SET IDENTITY_INSERT [dbo].[TAMVANG] ON 

INSERT [dbo].[TAMVANG] ([MaGiayTamVang], [ID], [HoTen], [CCCD], [NoiTamVang], [Tu], [Den], [LyDo], [NgayLamDon]) VALUES (5, 10, N'Nguyễn Bá Phúc', N'001201004678', N'16 Đ. Phùng Hưng, P. Phúc La, Hà Đông, Hà Nội', CAST(N'2023-02-13' AS Date), CAST(N'2023-02-24' AS Date), N'Đi du lịch', CAST(N'2023-02-13' AS Date))
INSERT [dbo].[TAMVANG] ([MaGiayTamVang], [ID], [HoTen], [CCCD], [NoiTamVang], [Tu], [Den], [LyDo], [NgayLamDon]) VALUES (6, 14, N'Nguyễn Anh Vũ', N'001205004707', N'Bắc Kạn', CAST(N'2023-02-13' AS Date), CAST(N'2023-02-23' AS Date), N'Học đại học', CAST(N'2023-02-13' AS Date))
INSERT [dbo].[TAMVANG] ([MaGiayTamVang], [ID], [HoTen], [CCCD], [NoiTamVang], [Tu], [Den], [LyDo], [NgayLamDon]) VALUES (7, 9, N'Nguyễn Hoàng Anh', N'001200000033', N'Nghệ An', CAST(N'2023-02-13' AS Date), CAST(N'2024-02-09' AS Date), N'Học đại học', CAST(N'2023-02-13' AS Date))
SET IDENTITY_INSERT [dbo].[TAMVANG] OFF
GO
SET IDENTITY_INSERT [dbo].[TraLoiKienNghi] ON 

INSERT [dbo].[TraLoiKienNghi] ([MaTraLoi], [MaKienNghi], [NoiDung], [NgayTraLoi], [TrangThai], [TenNguoiTraLoi], [IDQuanLy]) VALUES (12, 38, N'Trả lời kiến nghị của Nguyễn Hoàng Anh', CAST(N'2023-02-13' AS Date), N'Đã thông báo', N'Nguyễn Quốc Việt', N'captren08')
SET IDENTITY_INSERT [dbo].[TraLoiKienNghi] OFF
GO
ALTER TABLE [dbo].[BIENDOI]  WITH CHECK ADD  CONSTRAINT [Biến đổi của hộ khẩu] FOREIGN KEY([MaSo])
REFERENCES [dbo].[SOHOKHAU] ([MaSo])
GO
ALTER TABLE [dbo].[BIENDOI] CHECK CONSTRAINT [Biến đổi của hộ khẩu]
GO
ALTER TABLE [dbo].[BIENDOI]  WITH CHECK ADD  CONSTRAINT [FK_BIENDOI_DANGNHAP1] FOREIGN KEY([IDQuanLy])
REFERENCES [dbo].[DANGNHAP] ([IDQuanLy])
GO
ALTER TABLE [dbo].[BIENDOI] CHECK CONSTRAINT [FK_BIENDOI_DANGNHAP1]
GO
ALTER TABLE [dbo].[CUDAN]  WITH CHECK ADD  CONSTRAINT [Cư dân của hộ khẩu] FOREIGN KEY([MaSo])
REFERENCES [dbo].[SOHOKHAU] ([MaSo])
GO
ALTER TABLE [dbo].[CUDAN] CHECK CONSTRAINT [Cư dân của hộ khẩu]
GO
ALTER TABLE [dbo].[KIENNGHI]  WITH CHECK ADD  CONSTRAINT [Kiến nghị của cư dân] FOREIGN KEY([ID])
REFERENCES [dbo].[CUDAN] ([ID])
GO
ALTER TABLE [dbo].[KIENNGHI] CHECK CONSTRAINT [Kiến nghị của cư dân]
GO
ALTER TABLE [dbo].[TAMTRU]  WITH CHECK ADD  CONSTRAINT [Giấy tạm trú của cư dân] FOREIGN KEY([ID])
REFERENCES [dbo].[CUDAN] ([ID])
GO
ALTER TABLE [dbo].[TAMTRU] CHECK CONSTRAINT [Giấy tạm trú của cư dân]
GO
ALTER TABLE [dbo].[TAMVANG]  WITH CHECK ADD  CONSTRAINT [Giấy tạm vắng của cư dân] FOREIGN KEY([ID])
REFERENCES [dbo].[CUDAN] ([ID])
GO
ALTER TABLE [dbo].[TAMVANG] CHECK CONSTRAINT [Giấy tạm vắng của cư dân]
GO
ALTER TABLE [dbo].[TraLoiKienNghi]  WITH CHECK ADD  CONSTRAINT [Quản Lý trả lời] FOREIGN KEY([IDQuanLy])
REFERENCES [dbo].[DANGNHAP] ([IDQuanLy])
GO
ALTER TABLE [dbo].[TraLoiKienNghi] CHECK CONSTRAINT [Quản Lý trả lời]
GO
ALTER TABLE [dbo].[TraLoiKienNghi]  WITH CHECK ADD  CONSTRAINT [Trả lời] FOREIGN KEY([MaKienNghi])
REFERENCES [dbo].[KIENNGHI] ([MaKienNghi])
GO
ALTER TABLE [dbo].[TraLoiKienNghi] CHECK CONSTRAINT [Trả lời]
GO
USE [master]
GO
ALTER DATABASE [QLCUDAN] SET  READ_WRITE 
GO
