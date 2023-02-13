import ChucNang
from math import ceil
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import tkinter
import config.config as config
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image
import PIL
import os
import pyperclip

matplotlib.use('TkAgg')

ID = 2

dirname = os.path.dirname(__file__)
win_bg = config.win_bg
selected_bg = config.selected_bg
btn_trang_chu_bg = win_bg
btn_ho_khau_bg = win_bg
btn_kien_nghi_bg = win_bg
btn_thong_ke_bg = win_bg
btn_lich_su_bg = win_bg

padx = 10
pady = 7

font_header1 = "Arial 20 bold"
font_header2 = "Arial 16 bold"
font_header3 = "Arial 14 bold"
font_content = "Arial 12 bold"
font_content_mini = "Arial 10"


root = Tk(className="Quản Lý")
root.resizable(False, False)
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (config.win_w/2)
y = (hs/2) - (config.win_h/2)
root.geometry(f"{config.win_w}x{config.win_h}+{int(x)}+0")

'''Load IMAGE'''
# Đăng nhập
pathLogoLogin = os.path.join(
    dirname, 'config\\image\\icon_homepage.png')
logoIconLogin = PIL.Image.open(pathLogoLogin)
logoLogin = logoIconLogin.resize(
    (100, 100), Image.ANTIALIAS)
logoLogin = ImageTk.PhotoImage(logoLogin)
# Nav Bar
pathLogo = os.path.join(
    dirname, 'config\\image\\icon_homepage.png')
logoIcon = PIL.Image.open(pathLogo)
logo = logoIcon.resize(
    (60, 60), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
# ---------------
pathNavHomePageIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_home.png')
navHomePageImage = PIL.Image.open(pathNavHomePageIcon)
navHomePageImage = navHomePageImage.resize(
    (30, 30), Image.ANTIALIAS)
navHomePageImage = ImageTk.PhotoImage(navHomePageImage)
# -------------------------
pathNavFamilyIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_family.png')
navFamilyImage = PIL.Image.open(pathNavFamilyIcon)
navFamilyImage = navFamilyImage.resize(
    (30, 30), Image.ANTIALIAS)
navFamilyImage = ImageTk.PhotoImage(navFamilyImage)
# -------------------------
pathNavDemandIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_demand.png')
navDemandImage = PIL.Image.open(pathNavDemandIcon)
navDemandImage = navDemandImage.resize(
    (30, 30), Image.ANTIALIAS)
navDemandImage = ImageTk.PhotoImage(navDemandImage)
# -------------------------
pathThongKeBtn = os.path.join(
    dirname, 'config\\image\\thong_ke_button.png')
navThongKeImage = PIL.Image.open(pathThongKeBtn)
navThongKeImage = navThongKeImage.resize(
    (30, 30), Image.ANTIALIAS)
navThongKeImage = ImageTk.PhotoImage(navThongKeImage)
# -------------------------
pathLichSuIcon = os.path.join(
    dirname, 'config\\image\\icon_lich_su.png')
lichSuImage = PIL.Image.open(pathLichSuIcon)
lichSuImage = lichSuImage.resize(
    (30, 30), Image.ANTIALIAS)
lichSuImage = ImageTk.PhotoImage(lichSuImage)
# ------------------------
pathDangXuatIcon = os.path.join(
    dirname, 'config\\image\\icon_dang_xuat.png')
dangXuatImage = PIL.Image.open(pathDangXuatIcon)
dangXuatImage = dangXuatImage.resize(
    (30, 30), Image.ANTIALIAS)
dangXuatImage = ImageTk.PhotoImage(dangXuatImage)

'''HOME'''
# -- load icon schedule
pathSchedule = os.path.join(
    dirname, 'config\\image\\icon_schedule.png')
scheduleImage = PIL.Image.open(pathSchedule)
scheduleImage = scheduleImage.resize(
    (16, 16), Image.ANTIALIAS)
scheduleImage = ImageTk.PhotoImage(scheduleImage)
# ------------------------
# ThayDoiNhanKhau
pathThayDoiNhanKhau = os.path.join(
    dirname, 'config\\image\\change_person_button.png')
ThayDoiNhanKhauImage = PIL.Image.open(pathThayDoiNhanKhau)
ThayDoiNhanKhauImage = ThayDoiNhanKhauImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
ThayDoiNhanKhauImage = ImageTk.PhotoImage(ThayDoiNhanKhauImage)
# -------------------------
# viewMyInfo
pathViewMyInfo = os.path.join(
    dirname, 'config\\image\\view_my_info_button.png')
viewMyInfoImage = PIL.Image.open(pathViewMyInfo)
viewMyInfoImage = viewMyInfoImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
viewMyInfoImage = ImageTk.PhotoImage(viewMyInfoImage)
# ------------------------
# tách khẩu
pathTachKhau = os.path.join(
    dirname, 'config\\image\\tach_khau_button.png')
tachKhauImage = PIL.Image.open(pathTachKhau)
tachKhauImage = tachKhauImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tachKhauImage = ImageTk.PhotoImage(tachKhauImage)
# ------------------------
# tạm trú
pathTamTru = os.path.join(
    dirname, 'config\\image\\tam_tru_button.png')
tamTruImage = PIL.Image.open(pathTamTru)
tamTruImage = tamTruImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tamTruImage = ImageTk.PhotoImage(tamTruImage)
# ------------------------
# tạm vắng
pathTamVang = os.path.join(
    dirname, 'config\\image\\tam_vang_button.png')
tamVangImage = PIL.Image.open(pathTamVang)
tamVangImage = tamVangImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tamVangImage = ImageTk.PhotoImage(tamVangImage)
# ---------------------

# Config style cho drop down menu
someStyle = ttk.Style()
someStyle.configure('DropDownStyle.TMenubutton',
                    font=('Arial', 12, "bold"))


def switch(frame, maHoKhau="", hoKhau=(), listCuDan=[]):
    for f in frames:
        for widget in f.winfo_children():
            widget.destroy()
    # home
    if (frame == f_trang_chu):
        TrangChu()
    # xem hộ khẩu
    elif (frame == f_authen_family):
        AuthenFamily()
    # thay đổi nhân khẩu
    elif (frame == f_bien_doi_nhan_khau):
        BienDoiNhanKhau()
    # thêm nhân khẩu mới
    elif (frame == f_them_nhan_khau):
        ThemNhanKhau()

    elif (frame == f_thay_doi_nhan_khau):
        ThayDoiNhanKhau()
    # thay đổi chủ hộ
    elif (frame == f_authen_thay_doi_chu_ho):
        AuthenThayDoiChuHo()
    elif (frame == f_thay_doi_chu_ho):
        ThayDoiChuHo(maHoKhau=maHoKhau, hoKhau=hoKhau, listCuDan=listCuDan)
    elif (frame == f_authen_tach_khau):
        AuthenTachKhau()
    elif (frame == f_tach_khau):
        TachKhau(maHoKhau=maHoKhau, hoKhau=hoKhau, listCuDan=listCuDan)
    elif (frame == f_tam_tru):
        TamTru()
    elif (frame == f_tao_giay_tam_tru):
        TaoGiayTamTru()
    elif (frame == f_authen_xem_giay_tam_tru):
        AuthenXemGiayTamTru()
    elif (frame == f_xem_tat_ca_tam_tru):
        XemTatCaTamTru()
    elif (frame == f_tam_vang):
        TamVang()
    elif (frame == f_tao_giay_tam_vang):
        TaoGiayTamVang()
    elif (frame == f_authen_xem_giay_tam_vang):
        AuthenXemGiayTamVang()
    elif (frame == f_xem_tat_ca_tam_vang):
        XemTatCaTamVang()
    elif (frame == f_lich_su):
        LichSu()
    elif (frame == f_authen_lich_su_bien_doi_theo_ho_khau):
        AuthenXemLichSuBienDoiTheoHoKhau()
    elif (frame == f_lich_su_bien_doi_theo_ho_khau):
        XemLichSuBienDoiTheoHoKhau(maHoKhau=maHoKhau)
    elif (frame == f_tat_ca_lich_su_bien_doi):
        XemTatCaLichSuBienDoi()
    elif (frame == f_thong_ke):
        ThongKe()
    elif (frame == f_thong_ke_theo_do_tuoi):
        ThongKeTheoDoTuoi()
    elif (frame == f_thong_ke_theo_gioi_tinh):
        ThongKeTheoGioiTinh()
    elif (frame == f_thong_ke_tam_tru_tam_vang):
        ThongKeTamTruTamVang()
    elif (frame == f_kien_nghi):
        KienNghi()
    elif (frame == f_tao_kien_nghi):
        TaoKienNghi()
    elif (frame == f_tra_loi_kien_nghi):
        TraLoiKienNghi()

    Nav()
    frame.tkraise()


# Tạo các frame sẵn để nâng lên khi cần xuất hiện

f_trang_chu = tkinter.Frame(root)

f_authen_family = tkinter.Frame(root)
f_family = tkinter.Frame(root)

f_them_nhan_khau = tkinter.Frame(root)

f_bien_doi_nhan_khau = tkinter.Frame(root)
f_thay_doi_nhan_khau = tkinter.Frame(root)

f_authen_thay_doi_chu_ho = tkinter.Frame(root)
f_thay_doi_chu_ho = tkinter.Frame(root)

f_authen_tach_khau = tkinter.Frame(root)
f_tach_khau = tkinter.Frame(root)

f_tam_tru = tkinter.Frame(root)
f_tao_giay_tam_tru = tkinter.Frame(root)
f_authen_xem_giay_tam_tru = tkinter.Frame(root)
f_xem_giay_tam_tru = tkinter.Frame(root)
f_xem_tat_ca_tam_tru = tkinter.Frame(root)

f_tam_vang = tkinter.Frame(root)
f_tao_giay_tam_vang = tkinter.Frame(root)
f_authen_xem_giay_tam_vang = tkinter.Frame(root)
f_xem_giay_tam_vang = tkinter.Frame(root)
f_xem_tat_ca_tam_vang = tkinter.Frame(root)

f_lich_su = tkinter.Frame(root)
f_authen_lich_su_bien_doi_theo_ho_khau = tkinter.Frame(root)
f_lich_su_bien_doi_theo_ho_khau = tkinter.Frame(root)
f_tat_ca_lich_su_bien_doi = tkinter.Frame(root)

f_thong_ke = tkinter.Frame(root)
f_thong_ke_theo_do_tuoi = tkinter.Frame(root)
f_thong_ke_theo_gioi_tinh = tkinter.Frame(root)
f_thong_ke_tam_tru_tam_vang = tkinter.Frame(root)

f_kien_nghi = tkinter.Frame(root)
f_tao_kien_nghi = tkinter.Frame(root)
f_authen_xem_kien_nghi_theo_ca_nhan = tkinter.Frame(root)

f_xem_kien_nghi = tkinter.Frame(root)
f_tra_loi_kien_nghi = tkinter.Frame(root)
# set các frame chồng lên nhau.
frames = (f_trang_chu, f_authen_family, f_family, f_them_nhan_khau, f_bien_doi_nhan_khau, f_thay_doi_nhan_khau,  f_authen_thay_doi_chu_ho,
          f_thay_doi_chu_ho, f_authen_tach_khau, f_tach_khau, f_tam_tru, f_tao_giay_tam_tru, f_authen_xem_giay_tam_tru, f_xem_giay_tam_tru, f_xem_tat_ca_tam_tru,
          f_tam_vang, f_tao_giay_tam_vang, f_authen_xem_giay_tam_vang, f_xem_giay_tam_vang, f_xem_tat_ca_tam_vang, f_lich_su, f_authen_lich_su_bien_doi_theo_ho_khau,
          f_lich_su_bien_doi_theo_ho_khau, f_tat_ca_lich_su_bien_doi, f_thong_ke, f_thong_ke_theo_do_tuoi, f_thong_ke_theo_gioi_tinh,
          f_thong_ke_tam_tru_tam_vang, f_kien_nghi, f_tao_kien_nghi, f_authen_xem_kien_nghi_theo_ca_nhan, f_xem_kien_nghi, f_tra_loi_kien_nghi)
for f in frames:
    f.place(relx=1, rely=0, relheight=1, relwidth=0.8, anchor=NE)

# separator in root
win_separator = ttk.Separator(root, orient=VERTICAL)
win_separator.place(relx=0.199, rely=0, relheight=1, anchor=NW)
# nav_bar
nav_bar = tkinter.Frame(root, bg=win_bg)
nav_bar.place(relx=0, rely=0, relheight=1, relwidth=0.198, anchor=NW)


def Nav():
    # 1.Top
    topFrameNav = tkinter.Frame(nav_bar, padx=10, pady=5, bg=win_bg)
    topFrameNav.place(relx=0, rely=0, relwidth=1, relheight=0.15, anchor=NW)
    # 1.1 In top nav
    tkinter.Label(
        topFrameNav, image=logo, anchor=CENTER, bg=win_bg, padx=5).place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    # 1.2 App name
    tkinter.Label(
        topFrameNav, text="Quản lý", font=font_header1, anchor=W, bg=win_bg, padx=5).place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
    # ------------------------
    # 2.Middle
    middleFrameNav = tkinter.Frame(nav_bar, bg=win_bg, pady=20)
    middleFrameNav.place(relx=0, rely=0.15, relheight=0.6,
                         relwidth=1, anchor=NW)
    # 2.1 Home Butotn
    homeFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_trang_chu_bg, padx=5, pady=0)
    homeFrame_middle_nav.place(
        relx=0, rely=0, relheight=0.1, relwidth=1, anchor=NW)

    tkinter.Label(
        homeFrame_middle_nav, image=navHomePageImage, bg=btn_trang_chu_bg, anchor=E, padx=5).place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    tkinter.Button(
        homeFrame_middle_nav, text="Trang chủ", font=font_header3, anchor=W, bg=btn_trang_chu_bg, borderwidth=0, cursor="hand2",
        command=lambda: switch(f_trang_chu)).place(relx=1, rely=0, relheight=1,
                                                   relwidth=0.7, anchor=NE)

    # 2.2 Family Button

    familyFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_ho_khau_bg, padx=5, pady=0)
    familyFrame_middle_nav.place(
        relx=0, rely=0.1, relheight=0.1, relwidth=1, anchor=NW)

    tkinter.Label(
        familyFrame_middle_nav, image=navFamilyImage, bg=btn_ho_khau_bg, anchor=E, padx=5).place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    tkinter.Button(
        familyFrame_middle_nav, text="Sổ hộ khẩu", font=font_header3, anchor=W, bg=btn_ho_khau_bg, borderwidth=0, cursor="hand2",
        command=lambda: switch(f_authen_family)).place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
    # 2.3 Demand Button

    demandFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_kien_nghi_bg, padx=5, pady=0)
    demandFrame_middle_nav.place(
        relx=0, rely=0.2, relheight=0.1, relwidth=1, anchor=NW)

    tkinter.Label(
        demandFrame_middle_nav, image=navDemandImage, bg=btn_kien_nghi_bg, anchor=E, padx=5).place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    tkinter.Button(
        demandFrame_middle_nav, text="Kiến Nghị", font=font_header3, anchor=W, bg=btn_kien_nghi_bg, borderwidth=0, cursor="hand2",
        command=lambda: switch(f_kien_nghi)).place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)

    # 2.4 Thống kê
    thongKeFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_thong_ke_bg, padx=5, pady=0)
    thongKeFrame_middle_nav.place(
        relx=0, rely=0.3, relheight=0.1, relwidth=1, anchor=NW)
    tkinter.Label(
        thongKeFrame_middle_nav, image=navThongKeImage, bg=btn_thong_ke_bg, anchor=E, padx=5).place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    tkinter.Button(
        thongKeFrame_middle_nav, text="Thống kê", font=font_header3, anchor=W, bg=btn_thong_ke_bg, borderwidth=0, cursor="hand2",
        command=lambda: switch(f_thong_ke)).place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)

    '''Bottom'''
    bottomFrame_nav = tkinter.Frame(nav_bar, bg=win_bg, padx=10, pady=20)
    bottomFrame_nav.place(relx=0, rely=1, relheight=0.25,
                          relwidth=1, anchor=SW)
    # 3.1 History
    helpFrame_bottom_nav = tkinter.Frame(
        bottomFrame_nav, bg=btn_lich_su_bg, padx=5, pady=0)
    helpFrame_bottom_nav.place(
        relx=0, rely=0, relheight=0.3, relwidth=1, anchor=NW)

    tkinter.Label(
        helpFrame_bottom_nav, text="", image=lichSuImage, bg=btn_lich_su_bg, anchor=E, padx=5).place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    tkinter.Button(
        helpFrame_bottom_nav, text="Lịch sử", font=font_header3, anchor=W, bg=btn_lich_su_bg, borderwidth=0, cursor="hand2",
        command=lambda: switch(f_lich_su)).place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
    # 3.2 Logout
    settingFrame_bottom_nav = tkinter.Frame(
        bottomFrame_nav, bg=win_bg, padx=5, pady=0)
    settingFrame_bottom_nav.place(
        relx=0, rely=0.3, relheight=0.3, relwidth=1, anchor=NW)

    tkinter.Label(
        settingFrame_bottom_nav, image=dangXuatImage, bg=win_bg, anchor=E, padx=5).place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    tkinter.Button(
        settingFrame_bottom_nav, text="Đăng xuất", font=font_header3, anchor=W, bg=win_bg, borderwidth=0, cursor="hand2",
        command=lambda: LogIn()).place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)


'''End Nav Bar'''
# ---------------------------------------------------------------------------------------------------------------------------------
"""Start Home"""

# HomeView


def TrangChu():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_home = tkinter.Frame(
        f_trang_chu, highlightbackground="black", highlightthickness=2)
    f_trang_chu.grid_columnconfigure(0, weight=1)
    f_trang_chu.grid_rowconfigure(0, weight=1)
    f_all_home.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    topFrame_home = tkinter.Frame(f_all_home, bg=win_bg, pady=20, padx=5)
    topFrame_home.place(
        relx=0, rely=0, relheight=0.15, relwidth=1, anchor=NW)
    tkinter.Label(topFrame_home, text="Trang chủ", font=font_header1, bg=win_bg,
                  justify=LEFT, anchor=CENTER).grid(column=0, row=0, sticky=W)
    tkinter.Label(topFrame_home, text="", image=scheduleImage, bg=win_bg,
                  justify=LEFT, anchor=E).grid(column=1, row=0, sticky=W)
    tkinter.Label(topFrame_home, text=config.currentDate, font=font_content_mini, bg=win_bg,
                  justify=RIGHT, anchor=E).grid(column=2, row=0)
    topFrame_home.grid_columnconfigure(0, weight=1)
    topFrame_home.grid_rowconfigure(1, weight=1)

    '''BOTTOM'''
    # create FRAME
    bottomFrame_home = tkinter.Frame(f_all_home, bg=win_bg)
    bottomFrame_home.place(
        relx=0, rely=1, relheight=0.85, relwidth=1, anchor=SW)

    requestFrame_bottom_home = tkinter.Frame(bottomFrame_home, bg=win_bg)
    requestFrame_bottom_home.place(
        relx=0, rely=0, relheight=1, relwidth=0.4, anchor=NW)
    # label
    tkinter.Label(
        requestFrame_bottom_home, text="Yêu cầu của bạn", font=font_header2, anchor=W, padx=20, pady=10, bg=win_bg).place(relx=0, rely=0, relwidth=1, anchor=NW)
    # ---------------------------------------
    # thay đổi nhân khẩu
    tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=ThayDoiNhanKhauImage, borderwidth=0, bg=win_bg,
        command=lambda: switch(f_bien_doi_nhan_khau)).place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.07, anchor=NW)
    # -------------------------------------------
    # tách khẩu
    tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tachKhauImage, borderwidth=0, bg=win_bg,
        command=lambda: switch(f_authen_tach_khau)).place(relx=0.1, rely=0.18, relwidth=0.8, relheight=0.07, anchor=NW)
    # ---------------------------------------------
    # tạm trú
    tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tamTruImage, borderwidth=0, bg=win_bg,
        command=lambda: switch(f_tam_tru)).place(relx=0.1, rely=0.26, relwidth=0.8, relheight=0.07, anchor=NW)
    # ------------------------------------------------
    # tạm vắng
    tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tamVangImage, borderwidth=0, bg=win_bg,
        command=lambda: switch(f_tam_vang)).place(relx=0.1, rely=0.34, relwidth=0.8, relheight=0.07, anchor=NW)

    # ------------------------------------------------

    # RESPONSE
    responseFrame_bottom_home = tkinter.Frame(
        bottomFrame_home, bg=win_bg)
    responseFrame_bottom_home.place(
        relx=1, rely=0, relheight=1, relwidth=0.5, anchor=NE)

    # label
    labelText_request = tkinter.Label(
        responseFrame_bottom_home, text="Kiến nghị được trả lời gần đây:", font="Arial 16 bold", anchor=W, padx=20, pady=10, bg=win_bg)
    labelText_request.place(relx=0, rely=0, relwidth=1, anchor=NW)

    # subFrame kiến nghị
    f_thong_bao = tkinter.Frame(
        responseFrame_bottom_home, bg=config.response_demand_bg, borderwidth=1, padx=5, pady=5)
    f_thong_bao.place(
        relx=0.05, rely=0.12, relheight=0.85, relwidth=0.9, anchor=NW)

    for i in range(6):
        f_thong_bao.grid_rowconfigure(3*i+0, weight=10)
        f_thong_bao.grid_rowconfigure(3*i+1, weight=10)
        f_thong_bao.grid_rowconfigure(3*i+2, weight=1)

    errCode, Data = ChucNang.XemToanBoKienNghiTheoTrangThai("Đã xử lý")
    if (errCode == 0):
        tkinter.Label(f_thong_bao, text="Không có thông báo mới", font=font_header3, bg=config.response_demand_bg,
                      fg="red", justify=CENTER).place(relx=0.5, rely=0.5, anchor=N)
    else:
        tkinter.Button(responseFrame_bottom_home, text="Xem tất cả", relief=FLAT, cursor='hand2',
                       font=font_content_mini+" bold underline", anchor=E, bg=win_bg, command=lambda: viewAll()).place(relx=0.98, rely=0.07, anchor=NE)
        n = len(Data)
        for i in range(n):
            if (i >= 6):
                break
            if (len(Data[i][1].NoiDung) > 48):
                content = Data[i][1].NoiDung[0:45] + "..."
            else:
                content = Data[i][1].NoiDung

            tkinter.Label(f_thong_bao, text=Data[i][0].HoTen + " - "+Data[i][0].CCCD, font=font_content, anchor=NW,
                          justify=LEFT, wraplength=350, bg=config.response_demand_bg).grid(column=0, row=3*i+0, sticky=NW, padx=5, pady=2)
            tkinter.Label(f_thong_bao, text=content, font=font_content_mini, anchor=NW, justify=LEFT,
                          wraplength=350, bg=config.response_demand_bg).grid(column=0, row=3*i+1, sticky=NW, padx=5, pady=2)
            ttk.Separator(f_thong_bao, orient=HORIZONTAL).grid(
                column=0, row=3*i+2, sticky=EW)

        def viewAll():
            Data = ChucNang.GetTraLoiKienNghi()
            XemKienNghi(Data, False)


'''Biến đổi nhân khẩu'''
# xác nhận loại biến đổi (thêm người, thay đổi nhân khẩu, thay đổi chủ hộ)


def BienDoiNhanKhau():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_authen_change = tkinter.Frame(
        f_bien_doi_nhan_khau, highlightbackground="black", highlightthickness=2)
    f_bien_doi_nhan_khau.grid_columnconfigure(0, weight=1)
    f_bien_doi_nhan_khau.grid_rowconfigure(0, weight=1)
    f_all_authen_change.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    tkinter.Label(f_all_authen_change, text="Biến đổi nhân khẩu", font=font_header1,
                  justify=LEFT).grid(column=0, row=0, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_authen_change, text="Chọn loại biến đổi: ", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Thêm nhân khẩu mới", "Thay đổi nhân khẩu", "Thay đổi chủ hộ")
    chosed = StringVar(f_all_authen_change)
    dropDownGender = ttk.OptionMenu(
        f_all_authen_change, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownGender['menu'].configure(font=('Arial', 12))
    dropDownGender.grid(column=1, row=1, sticky=W,
                        padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_authen_change, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2',
        command=lambda: submit(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def submit(chose):
        if (chose == "Thêm nhân khẩu mới"):
            switch(f_them_nhan_khau)
        elif (chose == "Thay đổi nhân khẩu"):
            switch(f_thay_doi_nhan_khau)
        elif (chose == "Thay đổi chủ hộ"):
            switch(f_authen_thay_doi_chu_ho)


# CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ


def ThemNhanKhau():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_add_person = tkinter.Frame(
        f_them_nhan_khau, highlightbackground="black", highlightthickness=2)
    f_them_nhan_khau.grid_columnconfigure(0, weight=1)
    f_them_nhan_khau.grid_rowconfigure(0, weight=1)
    f_all_add_person.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_add_person.grid_columnconfigure(0, weight=1)
    f_all_add_person.grid_columnconfigure(1, weight=1)
    f_all_add_person.grid_columnconfigure(2, weight=1)
    f_all_add_person.grid_columnconfigure(3, weight=1)
    f_all_add_person.grid_columnconfigure(4, weight=1)
    f_all_add_person.grid_columnconfigure(5, weight=1)
    f_all_add_person.grid_columnconfigure(6, weight=1)
    f_all_add_person.grid_columnconfigure(7, weight=1)
    f_all_add_person.grid_columnconfigure(8, weight=1)
    f_all_add_person.grid_columnconfigure(9, weight=1)
    f_all_add_person.grid_columnconfigure(10, weight=1)
    f_all_add_person.grid_columnconfigure(11, weight=1)

    # row 0
    tkinter.Label(f_all_add_person, text="Thêm nhân khẩu", font=font_header1,
                  justify=LEFT).grid(column=0, row=0, columnspan=4, padx=padx, pady=pady)

    tkinter.Label(
        f_all_add_person, text="Quan hệ với chủ hộ:", font=font_header3, anchor=W).grid(row=1, column=0, columnspan=2, padx=padx, pady=pady, sticky=W)
    quanHe = tkinter.Entry(f_all_add_person, font=font_content, width=40)
    quanHe.grid(row=1, column=2, padx=padx,
                pady=pady, sticky=W, columnspan=2)

    # row 1
    tkinter.Label(
        f_all_add_person, text="Họ và tên: ", font=font_content, anchor=W).grid(column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)

    hoTen = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    hoTen.grid(column=1, row=2, padx=padx, pady=pady, columnspan=3)

    # row 2
    tkinter.Label(
        f_all_add_person, text="Bí danh(nếu có): ", font=font_content, anchor=W).grid(column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

    biDanh = tkinter.Entry(
        f_all_add_person, font=font_content, width=20)
    biDanh.grid(column=1, row=3, padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_add_person, text="Nghề nghiệp: ", font=font_content, anchor=W).grid(column=2, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

    ngheNghiep = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    ngheNghiep.grid(column=3, row=3, padx=padx, pady=pady, columnspan=1)

    # row 3
    tkinter.Label(
        f_all_add_person, text="Ngày sinh: ", font=font_content, anchor=W).grid(column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)

    ngaySinh = DateEntry(f_all_add_person, font=font_content)
    ngaySinh.grid(column=1, row=4, sticky=W,
                  padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_add_person, text="Giới tính: ", font=font_content, anchor=W).grid(column=2, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Nam", "Nữ")
    chosed = StringVar(f_all_add_person)

    dropDownGender = ttk.OptionMenu(
        f_all_add_person, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownGender['menu'].configure(font=('Arial', 12))
    dropDownGender.grid(column=3, row=4, sticky=W,
                        padx=padx, pady=pady, columnspan=1)

    # row 4
    tkinter.Label(
        f_all_add_person, text="Quê quán: ", font=font_content, anchor=W).grid(column=0, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    queQuan = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    queQuan.grid(column=1, row=5, sticky=W,
                 padx=padx, pady=pady, columnspan=3)

    # row 5
    tkinter.Label(
        f_all_add_person, text="Số căn cước công dân:", anchor=W, font=font_content).grid(column=0, row=6, padx=padx, pady=pady, sticky=W, columnspan=1)

    CCCD = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    CCCD.grid(column=1, row=6, padx=padx,
              pady=pady, sticky=W, columnspan=1)

    tkinter.Label(
        f_all_add_person, text="Mã hộ khẩu: ", anchor=W, font=font_content).grid(column=2, row=6, padx=padx,
                                                                                 pady=pady, sticky=W, columnspan=1)

    maHoKhau = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    maHoKhau.grid(column=3, row=6, padx=padx,
                  pady=pady, sticky=W, columnspan=1)

    # row 6
    tkinter.Label(
        f_all_add_person, text="Dân tộc: ", font=font_content, anchor=W).grid(column=0, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)

    danToc = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    danToc.grid(column=1, row=7, sticky=W,
                padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_add_person, text="Quốc tịch: ", font=font_content, anchor=W).grid(column=2, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)
    quocTich = tkinter.Entry(
        f_all_add_person, font=font_content, width=20)
    quocTich.grid(column=3, row=7, sticky=W,
                  padx=padx, pady=pady, columnspan=1)

    # row 7
    tkinter.Label(
        f_all_add_person, text="Địa chỉ cũ:", font=font_content, anchor=W).grid(column=0, row=8, sticky=W, padx=padx, pady=pady, columnspan=1)

    diaChiCu = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    diaChiCu.grid(
        column=1, row=8, padx=padx, pady=pady, columnspan=3)

    # row 8
    tkinter.Label(
        f_all_add_person, text="Ngày đăng ký thường trú: ", font=font_content, anchor=W).grid(column=0, row=9, sticky=W, padx=padx, pady=pady, columnspan=2)

    ngayDK = DateEntry(f_all_add_person, font=font_content)
    ngayDK.grid(column=2, row=9, sticky=W,
                padx=padx, pady=pady, columnspan=2)

    # row 10
    tkinter.Button(
        f_all_add_person, text="Gửi",  font=font_header3, fg="white", bg="blue", relief="groove", cursor='hand2',
        command=lambda: submit()).grid(column=0, row=10, padx=padx, pady=pady, columnspan=4)

    errorMessage = tkinter.Label(
        f_all_add_person, text="", font=font_content, fg="red", justify=CENTER)
    errorMessage.grid(column=0, row=11, columnspan=4)

    def submit():
        if (hoTen.get() == "" or danToc.get() == "" or quocTich.get() == "" or maHoKhau.get() == "" or quanHe.get() == ""):
            errorMessage['text'] = "Vui lòng điền đầy đủ thông tin!"
            return

        error_code, HoKhau, ListCuDan = ChucNang.XemSoHoKhau(maHoKhau.get())
        if (len(ListCuDan) == 0 and quanHe.get().upper() != "CHỦ HỘ"):
            errorMessage['text'] = "Hộ khẩu trống, vui lòng nhập chủ hộ đầu tiên!"
            return
        if (len(ListCuDan) and quanHe.get().upper() == "CHỦ HỘ"):
            errorMessage['text'] = "Vui lòng xem lại quan hệ, chủ hộ của hộ khẩu này đã tồn tại!"
            return

        # CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ
        ChucNang.ThemNhanKhauMoi(CCCD.get(),  # căn cước
                                 hoTen.get(),  # họ và tên
                                 chosed.get(),  # giới tính
                                 ngaySinh.get_date().strftime("%m/%d/%y"),  # ngày sinh
                                 danToc.get(),  # dân tộc
                                 quocTich.get(),  # quốc tịch
                                 ngheNghiep.get(),  # nghề nghiệp
                                 queQuan.get(),  # quê quán
                                 biDanh.get(),  # bí danh
                                 maHoKhau.get(),  # mã sổ hộ khẩu
                                 quanHe.get(),  # quan hệ vs chủ hộ
                                 ngayDK.get_date().strftime("%m/%d/%y"),  # ngày đăng kí thường trú
                                 diaChiCu.get())  # địa chỉ cũ
        messagebox.showinfo("", "Thêm nhân khẩu mới thành công!")
        switch(f_trang_chu)

#   NgayChuyenDi, NoiChuyenDi, GhiChu#


def ThayDoiNhanKhau():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_change_person = tkinter.Frame(
        f_thay_doi_nhan_khau, highlightbackground="black", highlightthickness=2)
    f_thay_doi_nhan_khau.grid_columnconfigure(0, weight=1)
    f_thay_doi_nhan_khau.grid_rowconfigure(0, weight=1)
    f_all_change_person.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_change_person.grid_columnconfigure(0, weight=1)
    f_all_change_person.grid_columnconfigure(1, weight=1)
    f_all_change_person.grid_columnconfigure(2, weight=1)
    f_all_change_person.grid_columnconfigure(3, weight=1)
    f_all_change_person.grid_columnconfigure(4, weight=1)

    tkinter.Label(f_all_change_person, text="Thay đổi nhân khẩu", font=font_header1,
                  justify=LEFT).grid(column=0, row=0, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_change_person, text="Nhập họ và tên:", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    hoTen = tkinter.Entry(
        f_all_change_person, font=font_content, width=40)
    hoTen.grid(column=1, row=1, sticky=W,
               padx=padx, pady=pady, columnspan=2)
    tkinter.Label(
        f_all_change_person, text="Nhập CCCD:", font=font_content, anchor=W).grid(column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    CCCD = tkinter.Entry(
        f_all_change_person, font=font_content, width=40)
    CCCD.grid(column=1, row=2, sticky=W,
              padx=padx, pady=pady, columnspan=2)

    tkinter.Button(
        f_all_change_person, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit()).grid(column=0, row=3, padx=padx, pady=pady, columnspan=4)

    errorMessage = tkinter.Label(
        f_all_change_person, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=4, padx=padx,
                      pady=pady, sticky=N, columnspan=4)

    def submit():
        hovaten = hoTen.get()
        cccd = CCCD.get()
        if (hovaten == "" or cccd == ""):
            errorMessage['text'] = "Vui lòng nhập đầy đủ thông tin!"
            return
        else:
            errorCode, CuDan = ChucNang.XemCuDan(hovaten, cccd)
            if (errorCode == 1):
                errorMessage['text'] = "Vui lòng kiểm tra lại thông tin!"
            elif (errorCode == 0):
                view(CuDan)

    def view(Data):
        for widget in f_all_change_person.winfo_children():
            widget.destroy()
        # row 0
        tkinter.Label(f_all_change_person, text="Thay đổi nhân khẩu", font=font_header1,
                      justify=LEFT).grid(column=0, row=0, columnspan=4, padx=padx, pady=pady)
        tkinter.Label(
            f_all_change_person, text="Quan hệ với chủ hộ:", font=font_header3, anchor=W).grid(row=1, column=0, columnspan=2, padx=padx, pady=pady, sticky=W)
        quanHe = tkinter.Entry(f_all_change_person,
                               font=font_content, width=40)
        quanHe.grid(row=1, column=2, padx=padx,
                    pady=pady, sticky=W, columnspan=2)
        if (Data.QuanHe):
            quanHe.insert(0, Data.QuanHe)
        # row 1
        tkinter.Label(
            f_all_change_person, text="Họ và tên: ", font=font_content, anchor=W).grid(column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)

        hoTen = tkinter.Entry(
            f_all_change_person, font=font_content, width=60)
        hoTen.grid(column=1, row=2, padx=padx,
                   pady=pady, sticky=W, columnspan=3)
        if (Data.HoTen):
            hoTen.insert(0, Data.HoTen)

        # row 2
        tkinter.Label(
            f_all_change_person, text="Bí danh(nếu có): ", font=font_content, anchor=W).grid(column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

        biDanh = tkinter.Entry(
            f_all_change_person, font=font_content, width=20)
        biDanh.grid(column=1, row=3, padx=padx,
                    pady=pady, sticky=W, columnspan=1)
        if (Data.BiDanh):
            biDanh.insert(0, Data.BiDanh)

        tkinter.Label(
            f_all_change_person, text="Nghề nghiệp: ", font=font_content, anchor=W).grid(column=2, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

        ngheNghiep = tkinter.Entry(
            f_all_change_person, font=font_content, width=20)
        ngheNghiep.grid(column=3, row=3, padx=padx,
                        pady=pady, sticky=W, columnspan=1)
        if (Data.NgheNghiep):
            ngheNghiep.insert(0, Data.NgheNghiep)

        # row 3
        tkinter.Label(
            f_all_change_person, text="Ngày sinh: ", font=font_content, anchor=W).grid(column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)

        ngaySinh = DateEntry(f_all_change_person, font=font_content)
        ngaySinh.grid(column=1, row=4, sticky=W,
                      padx=padx, pady=pady, columnspan=1)
        if (Data.NgaySinh):
            y_m_d = Data.NgaySinh.split("-")
            NgaySinh = ""+y_m_d[2]+"/"+y_m_d[1]+"/"+y_m_d[0]
            ngaySinh.set_date(NgaySinh)

        tkinter.Label(
            f_all_change_person, text="Giới tính: ", font=font_content, anchor=W).grid(column=2, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)

        option = ("Nam", "Nữ")
        chosed = StringVar(f_all_change_person)

        dropDownGender = ttk.OptionMenu(
            f_all_change_person, chosed, Data.GioiTinh, *option, style='DropDownStyle.TMenubutton')
        dropDownGender['menu'].configure(font=('Arial', 12))
        dropDownGender.grid(column=3, row=4, sticky=W,
                            padx=padx, pady=pady, columnspan=1)

        # row 4
        tkinter.Label(
            f_all_change_person, text="Quê quán: ", font=font_content, anchor=W).grid(column=0, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

        queQuan = tkinter.Entry(
            f_all_change_person, font=font_content, width=60)
        queQuan.grid(column=1, row=5, sticky=W,
                     padx=padx, pady=pady, columnspan=3)
        if (Data.QueQuan):
            queQuan.insert(0, Data.QueQuan)

        # row 5
        tkinter.Label(
            f_all_change_person, text="Số căn cước công dân:", anchor=W, font=font_content).grid(column=0, row=6, padx=padx, pady=pady, sticky=W, columnspan=1)

        CCCD = tkinter.Entry(f_all_change_person, font=font_content, width=20)
        CCCD.grid(column=1, row=6, padx=padx,
                  pady=pady, sticky=W, columnspan=1)
        if (Data.CCCD):
            CCCD.insert(0, Data.CCCD)

        tkinter.Label(
            f_all_change_person, text="Mã hộ khẩu: ", anchor=W, font=font_content).grid(column=2, row=6, padx=padx,
                                                                                        pady=pady, sticky=W, columnspan=1)

        maHoKhau = tkinter.Entry(
            f_all_change_person, font=font_content, width=20)
        maHoKhau.grid(column=3, row=6, padx=padx,
                      pady=pady, sticky=W, columnspan=1)
        if (Data.MaSo):
            maHoKhau.insert(0, Data.MaSo)

        # row 6
        tkinter.Label(
            f_all_change_person, text="Dân tộc: ", font=font_content, anchor=W).grid(column=0, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)

        danToc = tkinter.Entry(f_all_change_person,
                               font=font_content, width=20)
        danToc.grid(column=1, row=7, sticky=W,
                    padx=padx, pady=pady, columnspan=1)
        if (Data.DanToc):
            danToc.insert(0, Data.DanToc)

        tkinter.Label(
            f_all_change_person, text="Quốc tịch: ", font=font_content, anchor=W).grid(column=2, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)
        quocTich = tkinter.Entry(
            f_all_change_person, font=font_content, width=20)
        quocTich.grid(column=3, row=7, sticky=W,
                      padx=padx, pady=pady, columnspan=1)
        if (Data.QuocTich):
            quocTich.insert(0, Data.QuocTich)

        # row 7
        tkinter.Label(
            f_all_change_person, text="Địa chỉ cũ:", font=font_content, anchor=W).grid(column=0, row=8, sticky=W, padx=padx, pady=pady, columnspan=1)

        diaChiCu = tkinter.Entry(
            f_all_change_person, font=font_content, width=60)
        diaChiCu.grid(
            column=1, row=8, padx=padx, pady=pady, columnspan=3, sticky=W)
        if (Data.DiaChiCu):
            diaChiCu.insert(0, Data.DiaChiCu)

        # row 8
        tkinter.Label(
            f_all_change_person, text="Ngày đăng ký thường trú: ", font=font_content, anchor=W).grid(column=0, row=9, sticky=W, padx=padx, pady=pady, columnspan=2)

        ngayDK = DateEntry(f_all_change_person, font=font_content)
        ngayDK.grid(column=2, row=9, sticky=W,
                    padx=padx, pady=pady, columnspan=2)
        if (Data.NgayDangKyThuongTru):
            y_m_d = Data.NgayDangKyThuongTru.split("-")
            ngayDangKyThuongTru = ""+y_m_d[2]+"/"+y_m_d[1]+"/"+y_m_d[0]
            ngayDK.set_date(ngayDangKyThuongTru)

        # row 8
        tkinter.Label(
            f_all_change_person, text="Ngày chuyển đi: ", font=font_content, anchor=W).grid(column=0, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)

        ngayChuyenDi = DateEntry(f_all_change_person, font=font_content)
        ngayChuyenDi.grid(column=1, row=10, sticky=W,
                          padx=padx, pady=pady, columnspan=1)
        if (Data.NgayChuyenDi):
            y_m_d = Data.NgayChuyenDi.split("-")
            ngayCD = ""+y_m_d[2]+"/"+y_m_d[1]+"/"+y_m_d[0]
            ngayChuyenDi.set_date(ngayCD)

        # row 9
        tkinter.Label(
            f_all_change_person, text="Nơi chuyển đi : ", font=font_content, anchor=W).grid(column=0, row=11, sticky=W, padx=padx, pady=pady, columnspan=1)

        noiChuyenDi = tkinter.Entry(
            f_all_change_person, font=font_content, width=60)
        noiChuyenDi.grid(column=1, row=11, padx=padx,
                         pady=pady, columnspan=3, sticky=W)
        if (Data.NoiChuyenDi):
            noiChuyenDi.insert(0, Data.NoiChuyenDi)

        # row 10
        tkinter.Label(
            f_all_change_person, text="Ghi chú: ", font=font_content, anchor=W).grid(column=0, row=12, sticky=W, padx=padx, pady=pady, columnspan=1)

        ghiChu = tkinter.Entry(
            f_all_change_person, font=font_content, width=60)
        ghiChu.grid(column=1, row=12, padx=padx,
                    pady=pady, columnspan=3, sticky=W)
        if (Data.GhiChu):
            ghiChu.insert(0, Data.GhiChu)

        # row 11
        tkinter.Button(
            f_all_change_person, text="Gửi",  font=font_header3, fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: submit()).grid(column=0, row=13, padx=padx, pady=pady, columnspan=4)

        # row 12
        errorMessage = tkinter.Label(
            f_all_change_person, text="", font=font_content, fg="red", justify=CENTER)
        errorMessage.grid(column=0, row=14, columnspan=4)

        def submit():
            # CCCD, HoTen, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, MaSo, QuanHe, NgayDangKyThuongTru, DiaChiCu, NgayChuyenDi, NoiChuyenDi, GhiChu
            if (CCCD.get() == "" and hoTen.get() == "" and quanHe.get() == "" and maHoKhau.get() == "" and danToc.get() == "" and quocTich.get() == ""):
                errorMessage['text'] = "Vui lòng điền đầy đủ thông tin!"
                return
            errorCode = ChucNang.ThayDoiNhanKhau(CCCD.get(),  # căn cước
                                                 hoTen.get(),  # họ và tên
                                                 chosed.get(),  # giới tính
                                                 ngaySinh.get_date().strftime("%m/%d/%y"),  # ngày sinh
                                                 danToc.get(),  # dân tộc
                                                 quocTich.get(),  # quốc tịch
                                                 ngheNghiep.get(),  # nghề nghiệp
                                                 queQuan.get(),  # quê quán
                                                 biDanh.get(),  # bí danh
                                                 maHoKhau.get(),  # mã sổ hộ khẩu
                                                 quanHe.get(),  # quan hệ vs chủ hộ
                                                 ngayDK.get_date().strftime("%m/%d/%y"),  # ngày đăng kí thường trú
                                                 diaChiCu.get(),  # địa chỉ cũ
                                                 ngayChuyenDi.get(),
                                                 noiChuyenDi.get(),
                                                 ghiChu.get()
                                                 )

            if (errorCode == 0):
                messagebox.showinfo("", "Thay đổi nhân khẩu thành công!")
                switch(f_trang_chu)
            # errC = 1 trong trường hợp không tìm thấy dữ liệu
            elif (errorCode == 1):
                errorMessage['text'] = "Vui lòng kiểm tra lại CCCD, Họ tên, Mã hộ khẩu"


'''Thay đổi chủ hộ'''


def AuthenThayDoiChuHo():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_authen_change_host_person = tkinter.Frame(
        f_authen_thay_doi_chu_ho, highlightbackground="black", highlightthickness=2)
    f_authen_thay_doi_chu_ho.grid_columnconfigure(0, weight=1)
    f_authen_thay_doi_chu_ho.grid_rowconfigure(0, weight=1)
    f_all_authen_change_host_person.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)
    tkinter.Label(f_all_authen_change_host_person, text="Thay đổi chủ hộ", font=font_header1,
                  justify=LEFT).grid(column=0, row=0, padx=padx, pady=pady, sticky=W)
    tkinter.Label(
        f_all_authen_change_host_person, text="Nhập mã hộ khẩu", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    maHoKhau = tkinter.Entry(
        f_all_authen_change_host_person, font=font_content, width=20)
    maHoKhau.grid(column=1, row=1, sticky=W,
                  padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_change_host_person, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(maHoKhau.get(), errorMessage)).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_change_host_person, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=3, padx=padx,
                      pady=pady, sticky=N, columnspan=2)

    def submit(maHoKhau, errorMessage):
        errorCode, hoKhau, listCuDan = ChucNang.XemSoHoKhau(maHoKhau)
        if (errorCode):
            errorMessage['text'] = f"Số hộ khẩu: {maHoKhau} bị sai!. Vui lòng nhập lại"

        else:
            switch(frame=f_thay_doi_chu_ho, maHoKhau=maHoKhau,
                   hoKhau=hoKhau, listCuDan=listCuDan)

# Thông tin nhân khẩu:
# ID ,CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú


def ThayDoiChuHo(maHoKhau, hoKhau, listCuDan):
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    n = len(listCuDan)
    # Create a child frame to destroy when no use parent frame
    f_all_change_host_person = tkinter.Frame(
        f_thay_doi_chu_ho, highlightbackground="black", highlightthickness=2)
    f_thay_doi_chu_ho.grid_columnconfigure(0, weight=1)
    f_thay_doi_chu_ho.grid_rowconfigure(0, weight=1)
    f_all_change_host_person.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_change_host_person.grid_columnconfigure(0, weight=1)
    f_all_change_host_person.grid_columnconfigure(1, weight=1)
    f_all_change_host_person.grid_columnconfigure(2, weight=1)
    tkinter.Label(
        f_all_change_host_person, text="Đổi chủ hộ", font=font_header1, justify=CENTER).grid(column=0, row=0, columnspan=3)

    tkinter.Label(f_all_change_host_person, text="Họ và tên", font=font_header2,
                  anchor=W, justify=LEFT).grid(column=0, row=1, columnspan=1, padx=10, pady=5, sticky=W)
    tkinter.Label(f_all_change_host_person, text="CCCD", font=font_header2,
                  anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=1, padx=10, pady=5, sticky=W)
    tkinter.Label(f_all_change_host_person, text="Quan hệ với chủ hộ mới",
                  font=font_header2, anchor=W, justify=LEFT).grid(column=2, row=1, columnspan=1, padx=10, pady=5, sticky=W)
    listEntry = []
    for i in range(n):
        tkinter.Label(f_all_change_host_person, text=listCuDan[i][2], font=font_content, anchor=W, justify=LEFT).grid(
            column=0, row=i+2, columnspan=1, sticky=W, padx=10, pady=5)
        tkinter.Label(f_all_change_host_person, text=listCuDan[i][1], font=font_content, anchor=W, justify=LEFT).grid(
            column=1, row=i+2, columnspan=1, sticky=W, padx=10, pady=5)
        listEntry.append(tkinter.Entry(
            f_all_change_host_person, font=font_content, width=20))
        listEntry[i].grid(column=2, row=i+2, columnspan=1,
                          sticky=W, padx=10, pady=5)

    tkinter.Button(f_all_change_host_person, text="Gửi",  font=font_header3, fg="white", bg="blue", cursor='hand2',
                   command=lambda: submit()).grid(column=0, row=2+n, columnspan=3)
    errorMessage = tkinter.Label(f_all_change_host_person, text="", font=font_content,
                                 fg="red", justify=CENTER)
    errorMessage.grid(column=0, row=3+n, columnspan=3)

    def submit():
        listId = []
        listQuanHeMoi = []
        countChuHo = 0
        check = True
        for i in range(n):
            if (listEntry[i].get() == ""):
                check = False
                errorMessage['text'] = "Vui lòng điền đủ tất cả các trường quan hệ mới"
                break
            if (listEntry[i].get() == "Chủ hộ"):
                countChuHo = countChuHo+1

            listId.append(listCuDan[i][0])
            listQuanHeMoi.append(listEntry[i].get())
        if (countChuHo <= 0):
            check = False
            errorMessage['text'] = "Cần tồn tại ít nhất 1 chủ hộ"

        elif (countChuHo > 1):
            check = False
            errorMessage['text'] = "Có không quá 1 chủ hộ"

        if (check):
            ChucNang.ThayDoiChuHo(listId, listQuanHeMoi, maHoKhau)
            messagebox.showinfo("", "Đã thay đổi chủ hộ thành công"),
            switch(f_trang_chu)


'''Tách khẩu'''


def AuthenTachKhau():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_authen_tach_khau = tkinter.Frame(
        f_authen_tach_khau, highlightbackground="black", highlightthickness=2)
    f_authen_tach_khau.grid_columnconfigure(0, weight=1)
    f_authen_tach_khau.grid_rowconfigure(0, weight=1)
    f_all_authen_tach_khau.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    tkinter.Label(f_all_authen_tach_khau, text="Tách khẩu", font=font_header1, justify=LEFT).grid(
        column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)
    tkinter.Label(
        f_all_authen_tach_khau, text="Nhập mã hộ khẩu", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    maHoKhau = tkinter.Entry(
        f_all_authen_tach_khau, font=font_content, width=20)
    maHoKhau.grid(column=1, row=1, sticky=W,
                  padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_tach_khau, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(maHoKhau.get(), errorMessage)).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_tach_khau, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=3, padx=padx,
                      pady=pady, sticky=N, columnspan=2)

    def submit(maHoKhau, errorMessage):
        errorCode, hoKhau, listCuDan = ChucNang.XemSoHoKhau(maHoKhau)
        if (errorCode):
            errorMessage['text'] = f"Số hộ khẩu: {maHoKhau} bị sai!. Vui lòng nhập lại"

        else:
            switch(frame=f_tach_khau, maHoKhau=maHoKhau,
                   hoKhau=hoKhau, listCuDan=listCuDan)

# Thông tin nhân khẩu:
# ID ,CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú


def TachKhau(maHoKhau, hoKhau, listCuDan):
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    n = len(listCuDan)
    # Create a child frame to destroy when no use parent frame
    f_all_tach_khau = tkinter.Frame(
        f_tach_khau, highlightbackground="black", highlightthickness=2)
    f_tach_khau.grid_columnconfigure(0, weight=1)
    f_tach_khau.grid_rowconfigure(0, weight=1)
    f_all_tach_khau.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_tach_khau.grid_columnconfigure(0, weight=1)
    f_all_tach_khau.grid_columnconfigure(1, weight=1)
    f_all_tach_khau.grid_columnconfigure(2, weight=1)
    f_all_tach_khau.grid_columnconfigure(3, weight=1)

    for i in range(n+7):
        f_all_tach_khau.grid_rowconfigure(i, weight=1)

    tkinter.Label(
        f_all_tach_khau, text="Tách khẩu", font=font_header1, justify=CENTER).grid(column=0, row=0, columnspan=4, sticky=N)

    tkinter.Label(f_all_tach_khau, text="Họ và tên", font=font_header2,
                  anchor=W, justify=LEFT).grid(column=0, row=1, columnspan=1, padx=10, pady=5, sticky=W)
    tkinter.Label(f_all_tach_khau, text="CCCD", font=font_header2,
                  anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=1, padx=10, pady=5, sticky=W)
    tkinter.Label(f_all_tach_khau, text="Chọn để tách",
                  font=font_header2, anchor=W, justify=LEFT).grid(column=2, row=1, columnspan=1, padx=10, pady=5, sticky=W)
    tkinter.Label(f_all_tach_khau, text="Quan hệ với chủ hộ",
                  font=font_header2, anchor=W, justify=LEFT).grid(column=3, row=1, columnspan=1, padx=10, pady=5, sticky=W)
    listVar = []
    listEntry = []
    for i in range(n):
        tkinter.Label(f_all_tach_khau, text=listCuDan[i][2], font=font_content, anchor=W, justify=LEFT).grid(
            column=0, row=i+2, columnspan=1, sticky=W, padx=10, pady=5)
        tkinter.Label(f_all_tach_khau, text=listCuDan[i][1], font=font_content, anchor=W, justify=LEFT).grid(
            column=1, row=i+2, columnspan=1, sticky=W, padx=10, pady=5)
        listVar.append(IntVar())
        tkinter.Checkbutton(f_all_tach_khau, text="",
                            font=font_content, cursor='hand2', variable=listVar[i], onvalue=1, offvalue=0).grid(column=2, row=i+2, columnspan=1, padx=10, pady=5)
        listEntry.append(tkinter.Entry(
            f_all_tach_khau, font=font_content, width=20))
        listEntry[i].grid(column=3, row=i+2, columnspan=1,
                          sticky=W, padx=10, pady=5)
        listEntry[i].insert(0, listCuDan[i][11])
        listEntry[i].bind(
            "<FocusIn>", lambda args, data=i: listEntry[data].delete('0', 'end'))

    tkinter.Label(f_all_tach_khau, text="Nhập địa chỉ hộ khẩu mới: ",
                  font=font_header3, anchor=W, justify=LEFT).grid(column=0, row=2+n, sticky=W, columnspan=4)
    tkinter.Label(f_all_tach_khau, text="Số nhà:", font=font_content, anchor=W,
                  justify=LEFT).grid(column=0, row=3+n, columnspan=1, sticky=W)
    soNha = tkinter.Entry(f_all_tach_khau, font=font_content, width=20)
    soNha.grid(column=1, row=3+n, columnspan=1, sticky=W)

    tkinter.Label(f_all_tach_khau, text="Phường/Xã:", font=font_content,
                  anchor=W, justify=LEFT).grid(column=2, row=3+n, columnspan=1, sticky=W)
    phuong = tkinter.Entry(f_all_tach_khau, font=font_content, width=20)
    phuong.grid(column=3, row=3+n, columnspan=1, sticky=W)

    tkinter.Label(f_all_tach_khau, text="Quận/Huyện:", font=font_content, anchor=W,
                  justify=LEFT).grid(column=0, row=4+n, columnspan=1, sticky=W)
    huyen = tkinter.Entry(f_all_tach_khau, font=font_content, width=20)
    huyen.grid(column=1, row=4+n, columnspan=1, sticky=W)

    tkinter.Label(f_all_tach_khau, text="Tỉnh/Thành phố:", font=font_content,
                  anchor=W, justify=LEFT).grid(column=2, row=4+n, columnspan=1, sticky=W)
    tinh = tkinter.Entry(f_all_tach_khau, font=font_content, width=20)
    tinh.grid(column=3, row=4+n, columnspan=1, sticky=W)

    tkinter.Button(f_all_tach_khau, text="Gửi",  font=font_header3, fg="white", bg="blue", cursor='hand2',
                   command=lambda: submit()).grid(column=0, row=5+n, columnspan=4)
    errorMessage = tkinter.Label(f_all_tach_khau, text="", font=font_content,
                                 fg="red", justify=CENTER)
    errorMessage.grid(column=0, row=6+n, columnspan=4)

    # HoKhau_1 và HoKhau_2 có dạng: [ MaSo, [ [ID, QuanHe], [ID, QuanHe],... ], SoNha, Phuong, Huyen, Tinh]
    def submit():
        hoKhauOld = [maHoKhau]
        hoKhauNew = [1]
        listCuDanOld = []
        listCuDanNew = []
        countChuHoOld = 0
        countChuHoNew = 0
        check = True
        for i in range(n):
            if (listEntry[i].get() == ""):
                check = False
                errorMessage['text'] = "Vui lòng điền đủ tất cả các trường quan hệ mới"
                break
            # Hộ khẩu mới
            if (listVar[i].get() == 1):
                listCuDanNew.append([listCuDan[i][0], listEntry[i].get()])
                if (listEntry[i].get().lower() == "chủ hộ"):
                    countChuHoNew = countChuHoNew+1
            else:
                listCuDanOld.append([listCuDan[i][0], listEntry[i].get()])
                if (listEntry[i].get().lower() == "chủ hộ"):
                    countChuHoOld = countChuHoOld+1
        hoKhauOld = hoKhauOld + [listCuDanOld, hoKhau.SoNha,
                                 hoKhau.Phuong, hoKhau.Huyen, hoKhau.Tinh]
        hoKhauNew = hoKhauNew + [listCuDanNew, soNha.get(),
                                 phuong.get(), huyen.get(), tinh.get()]

        if (countChuHoOld <= 0):
            check = False
            errorMessage['text'] = "Cần tồn tại ít nhất 1 chủ hộ trong hộ khẩu CŨ"
        elif (countChuHoNew <= 0):
            check = False
            errorMessage['text'] = "Cần tồn tại ít nhất 1 chủ hộ trong hộ khẩu MỚI"
        elif (countChuHoOld > 1):
            check = False
            errorMessage['text'] = "Có không quá 1 chủ hộ trong hộ khẩu CŨ"
        elif (countChuHoNew > 1):
            check = False
            errorMessage['text'] = "Có không quá 1 chủ hộ trong hộ khẩu MỚI"

        if (check):
            MaSoMoi = ChucNang.TachHoKhau(hoKhauOld, hoKhauNew)
            pyperclip.copy(MaSoMoi)

            messagebox.showinfo(
                "", "Tách khẩu thành công với mã hộ khẩu mới là:\n               "+str(MaSoMoi)),
            switch(f_trang_chu)


'''Tạm trú'''


def TamTru():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_all_tam_tru = tkinter.Frame(
        f_tam_tru, highlightbackground="black", highlightthickness=2)
    f_tam_tru.grid_columnconfigure(0, weight=1)
    f_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_tam_tru.grid(column=0, row=0, sticky='news', padx=10, pady=10)
    tkinter.Label(f_all_tam_tru, text="Tạm trú", font=font_header1, justify=LEFT).grid(
        column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_tam_tru, text="Chọn yêu cầu của bạn: ", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Tạo giấy tạm trú", "Xem giấy tạm trú",
              "Xem tất cả giấy tạm trú")
    chosed = StringVar(f_all_tam_tru)
    dropDownTamTru = ttk.OptionMenu(
        f_all_tam_tru, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownTamTru['menu'].configure(font=('Arial', 12))
    dropDownTamTru.grid(column=1, row=1, sticky=W,
                        padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_tam_tru, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def submit(chose):
        if (chose == "Tạo giấy tạm trú"):
            switch(f_tao_giay_tam_tru)
        elif (chose == "Xem giấy tạm trú"):
            switch(f_authen_xem_giay_tam_tru)
        elif (chose == "Xem tất cả giấy tạm trú"):
            switch(f_xem_tat_ca_tam_tru)


# HoTen, CCCD, QueQuan, DiaChiThuongTru, NgayBatDau: datetime.datetime, NgayKetThuc: datetime.datetime, LyDo, NgayLamDon: datetime.datetime

def TaoGiayTamTru():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_tao_giay_tam_tru = tkinter.Frame(
        f_tao_giay_tam_tru, highlightbackground="black", highlightthickness=2)
    f_tao_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_tao_giay_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_tao_giay_tam_tru.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_tao_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_all_tao_giay_tam_tru.grid_columnconfigure(1, weight=1)
    f_all_tao_giay_tam_tru.grid_columnconfigure(2, weight=1)
    f_all_tao_giay_tam_tru.grid_columnconfigure(3, weight=1)
    # row 0
    tkinter.Label(f_all_tao_giay_tam_tru, text="Đơn xin tạm trú", font=font_header1).grid(
        column=0, row=0, padx=padx, pady=0, columnspan=4)

    # row 1
    tkinter.Label(f_all_tao_giay_tam_tru, text="Tên tôi là:", font=font_content, anchor=W).grid(
        column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    hoVaTen = tkinter.Entry(f_all_tao_giay_tam_tru,
                            font=font_content, width=60)
    hoVaTen.grid(column=1, row=1, sticky=W,
                 padx=padx, pady=pady, columnspan=3)
    # row 2
    tkinter.Label(f_all_tao_giay_tam_tru, text="CCCD:", font=font_content, anchor=W).grid(
        column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    CCCD = tkinter.Entry(f_all_tao_giay_tam_tru, font=font_content, width=20)
    CCCD.grid(column=1, row=2, sticky=W,
              padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_tao_giay_tam_tru, text="Mã Hộ Khẩu:", font=font_content, anchor=W).grid(
        column=2, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    maSo = tkinter.Entry(f_all_tao_giay_tam_tru, font=font_content, width=20)
    maSo.grid(column=3, row=2, sticky=W,
              padx=padx, pady=pady, columnspan=1)
    # row 3
    tkinter.Label(f_all_tao_giay_tam_tru, text="Quê quán:", font=font_content, anchor=W).grid(
        column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)
    queQuan = tkinter.Entry(f_all_tao_giay_tam_tru,
                            font=font_content, width=60)
    queQuan.grid(column=1, row=3, sticky=W,
                 padx=padx, pady=pady, columnspan=3)

    # row 4
    tkinter.Label(f_all_tao_giay_tam_tru, text="Địa chỉ tạm trú:", font=font_content, anchor=W).grid(
        column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)
    thuongTru = tkinter.Entry(f_all_tao_giay_tam_tru,
                              font=font_content, width=60)
    thuongTru.grid(column=1, row=4, sticky=W,
                   padx=padx, pady=pady, columnspan=3)

    # row 5
    tkinter.Label(f_all_tao_giay_tam_tru, text="Từ ngày: ", font=font_content, anchor=W).grid(
        column=0, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    tuNgay = DateEntry(f_all_tao_giay_tam_tru, font=font_content)
    tuNgay.grid(column=1, row=5, sticky=W,
                padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_tao_giay_tam_tru, text="Đến ngày: ", font=font_content, anchor=W).grid(
        column=2, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    denNgay = DateEntry(f_all_tao_giay_tam_tru, font=font_content)
    denNgay.grid(column=3, row=5, sticky=W,
                 padx=padx, pady=pady, columnspan=1)

    # row 6
    tkinter.Label(f_all_tao_giay_tam_tru, text="Lý do:", font=font_content, anchor=W).grid(
        column=0, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)
    lyDo = tkinter.Text(
        f_all_tao_giay_tam_tru, font=font_content, height=10, width=60, wrap=WORD)
    lyDo.grid(column=1, row=6, sticky=W,
              padx=padx, pady=pady, columnspan=3)

    # row 7

    tkinter.Label(f_all_tao_giay_tam_tru, text="Ngày làm đơn: ", font=font_content, anchor=W).grid(
        column=0, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)

    ngayLamDon = DateEntry(f_all_tao_giay_tam_tru, font=font_content)
    ngayLamDon.grid(column=1, row=7, sticky=W,
                    padx=padx, pady=pady, columnspan=1)

    # row 8
    tkinter.Button(f_all_tao_giay_tam_tru, text="Xác nhận",  font=font_header3, fg="white", bg="blue", cursor='hand2', command=lambda: submit()).grid(
        column=0, row=8, padx=padx, pady=pady, columnspan=4)

    errorMessage = tkinter.Label(
        f_all_tao_giay_tam_tru, text="", font=font_content, fg="red", justify=CENTER)
    errorMessage.grid(column=0, row=9, columnspan=4)

    def submit():
        if (hoVaTen.get() == "" or CCCD.get() == "" or maSo.get() == "" or queQuan.get() == "" or thuongTru.get() == "" or lyDo.get("1.0", 'end-1c') == ""):
            errorMessage['text'] = "Vui lòng điền đầy đủ các trường!"
            return
        errorCode = ChucNang.CapGiayTamTru(hoVaTen.get(), CCCD.get(), maSo.get(), queQuan.get(), thuongTru.get(), tuNgay.get_date().strftime(
            "%m/%d/%y"), denNgay.get_date().strftime("%m/%d/%y"), lyDo.get("1.0", 'end-1c'), ngayLamDon.get_date().strftime("%m/%d/%y"))
        if (errorCode == 0):
            messagebox.showinfo("", "Đã hoàn thành đơn tạm trú")
            switch(f_trang_chu)
        elif (errorCode == 1):
            errorMessage['text'] = "Vui lòng kiểm tra lại thông tin!"
            return


def AuthenXemGiayTamTru():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_all_authen_xem_giay_tam_tru = tkinter.Frame(
        f_authen_xem_giay_tam_tru, highlightbackground="black", highlightthickness=2)
    f_authen_xem_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_authen_xem_giay_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_authen_xem_giay_tam_tru.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_authen_xem_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_all_authen_xem_giay_tam_tru.grid_columnconfigure(1, weight=1)
    f_all_authen_xem_giay_tam_tru.grid_columnconfigure(2, weight=1)
    f_all_authen_xem_giay_tam_tru.grid_columnconfigure(3, weight=1)
    tkinter.Label(f_all_authen_xem_giay_tam_tru, text="Xem giấy tạm trú", font=font_header1,
                  justify=LEFT).grid(column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_authen_xem_giay_tam_tru, text="Họ và tên:", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    hoVaTen = tkinter.Entry(
        f_all_authen_xem_giay_tam_tru, font=font_content, width=20)
    hoVaTen.grid(column=1, row=1, sticky=W,
                 padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_authen_xem_giay_tam_tru, text="CCCD:", font=font_content, anchor=W).grid(column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    CCCD = tkinter.Entry(
        f_all_authen_xem_giay_tam_tru, font=font_content, width=20)
    CCCD.grid(column=1, row=2, sticky=W,
              padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_xem_giay_tam_tru, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit()).grid(column=0, row=3, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_xem_giay_tam_tru, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=4, padx=padx,
                      pady=pady, sticky=N, columnspan=2)

    def submit():
        if (hoVaTen.get() == "" or CCCD.get() == ""):
            errorMessage['text'] = "Vui lòng nhập đầy đủ thông tin!"
            return

        errorCode, thongTinGiayTamTru = ChucNang.XemGiayTamTru(
            hoVaTen.get(), CCCD.get())
        if (errorCode == 1):
            errorMessage['text'] = "Thông tin bị sai!. Vui lòng nhập lại"
        elif (errorCode == 2):
            errorMessage['text'] = "Người này không có giấy tạm trú"
        else:
            XemGiayTamTru(thongTinGiayTamTru, f_trang_chu)
# MaGiayTamTru, HoTen, CCCD, Tu, Den, LyDo, NgayLamDon


def XemGiayTamTru(thongTinGiayTamTru, frame):
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_xem_giay_tam_tru.tkraise()
    # Create a child frame to destroy when no use parent frame
    f_all_xem_giay_tam_tru = tkinter.Frame(
        f_xem_giay_tam_tru, highlightbackground="black", highlightthickness=2)
    f_xem_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_xem_giay_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_xem_giay_tam_tru.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_xem_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_all_xem_giay_tam_tru.grid_columnconfigure(1, weight=1)
    f_all_xem_giay_tam_tru.grid_columnconfigure(2, weight=1)
    f_all_xem_giay_tam_tru.grid_columnconfigure(3, weight=1)

    # row 0
    tkinter.Label(f_all_xem_giay_tam_tru, text="Đơn xin tạm trú", font=font_header1).grid(
        column=0, row=0, padx=padx, pady=0, columnspan=4)
    # row 1
    tkinter.Label(f_all_xem_giay_tam_tru, text="Tên tôi là: ", font=font_content, anchor=W).grid(
        column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    tkinter.Label(f_all_xem_giay_tam_tru, text=thongTinGiayTamTru.HoTen,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=3, padx=padx, pady=pady, sticky=W)
    # row 2
    tkinter.Label(f_all_xem_giay_tam_tru, text="CCCD:", font=font_content, anchor=W).grid(
        column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    tkinter.Label(f_all_xem_giay_tam_tru, text=thongTinGiayTamTru.CCCD,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=2, columnspan=3, padx=padx, pady=pady, sticky=W)
    tkinter.Label(f_all_xem_giay_tam_tru, text="Địa chỉ tạm trú:", font=font_content, anchor=W).grid(
        column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)
    tkinter.Label(f_all_xem_giay_tam_tru, text=thongTinGiayTamTru.DiaChiTamTru,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=3, columnspan=3, padx=padx, pady=pady, sticky=W)

    # row 5
    tkinter.Label(f_all_xem_giay_tam_tru, text="Từ ngày: ", font=font_content, anchor=W).grid(
        column=0, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_xem_giay_tam_tru, text=thongTinGiayTamTru.Tu,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=5, columnspan=3, padx=padx, pady=pady, sticky=W)

    tkinter.Label(f_all_xem_giay_tam_tru, text="Đến ngày: ", font=font_content, anchor=W).grid(
        column=2, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_xem_giay_tam_tru, text=thongTinGiayTamTru.Den,
                  font=font_content, anchor=W, justify=LEFT).grid(column=3, row=5, columnspan=3, padx=padx, pady=pady, sticky=W)

    # row 6
    tkinter.Label(f_all_xem_giay_tam_tru, text="Lý do:", font=font_content, anchor=W).grid(
        column=0, row=6, sticky=NW, padx=padx, pady=pady, columnspan=1, rowspan=2)
    tkinter.Label(f_all_xem_giay_tam_tru, text=thongTinGiayTamTru.LyDo,
                  font=font_content, anchor=W, justify=LEFT, wraplength=500).grid(column=1, row=6, columnspan=3, rowspan=2, padx=padx, pady=pady, sticky=NW)

    # row 7

    tkinter.Label(f_all_xem_giay_tam_tru, text="Ngày làm đơn: ", font=font_content, anchor=W).grid(
        column=0, row=8, sticky=W, padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_xem_giay_tam_tru, text=thongTinGiayTamTru.NgayLamDon,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=8, columnspan=3, padx=padx, pady=pady, sticky=W)

    btn = tkinter.Button(f_all_xem_giay_tam_tru, text="", font=font_header3, fg="white", bg="blue", relief='groove',
                         cursor='hand2', command=lambda: switch(frame))
    btn.grid(column=0, row=9, columnspan=4, padx=padx, pady=pady)
    if (frame == f_trang_chu):
        btn['text'] = "Về trang chủ"
    elif (frame == f_xem_tat_ca_tam_tru):
        btn['text'] = "Trở lại"


def XemTatCaTamTru():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_all_xem_tat_ca_tam_tru = tkinter.Frame(
        f_xem_tat_ca_tam_tru, highlightbackground="black", highlightthickness=2)
    f_xem_tat_ca_tam_tru.grid_columnconfigure(0, weight=1)
    f_xem_tat_ca_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_xem_tat_ca_tam_tru.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_xem_tat_ca_tam_tru.grid_columnconfigure(0, weight=2)
    f_all_xem_tat_ca_tam_tru.grid_columnconfigure(1, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_columnconfigure(2, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_columnconfigure(3, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_columnconfigure(4, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(1, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(2, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(3, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(4, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(5, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(6, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(7, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(8, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(9, weight=1)
    f_all_xem_tat_ca_tam_tru.grid_rowconfigure(10, weight=1)

    listTamTru = ChucNang.getAllTamTru()
    n = len(listTamTru)
    if (n != 0):
        times = ceil(n/8)

    def showPage(i):
        if (n == 0):
            tkinter.Label(f_all_xem_tat_ca_tam_tru, text="Tất cả tạm trú", font=font_header1, justify=LEFT).grid(
                column=0, row=0, columnspan=5, padx=padx, pady=pady, sticky=N)

            tkinter.Label(f_all_xem_tat_ca_tam_tru, text="Không có giấy tạm trú", fg="red",
                          font=font_header3).grid(column=0, row=1, columnspan=5, sticky=N)
        else:
            # Không cho đi về trước page đầu tiên
            if (i <= 0):
                i = 0
            # Không cho đi quá page cuối
            elif (i >= times-1):
                i = times-1
            # Xóa dữ liệu cũ
            for widget in f_all_xem_tat_ca_tam_tru.winfo_children():
                widget.destroy()
            # Hiện thông tin page thứ i
            XemTamTru(i)

    def XemTamTru(i):
        tkinter.Label(f_all_xem_tat_ca_tam_tru, text="Tất cả giấy tạm trú", font=font_header1, justify=LEFT).grid(
            column=0, row=0, columnspan=5, padx=padx, pady=pady, sticky=N)

        tkinter.Label(f_all_xem_tat_ca_tam_tru, text="Họ và tên", font=font_content,
                      anchor=W, justify=LEFT).grid(column=0, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_xem_tat_ca_tam_tru, text="CCCD", font=font_content,
                      anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_xem_tat_ca_tam_tru, text="Từ ngày", font=font_content,
                      anchor=W, justify=LEFT).grid(column=2, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_xem_tat_ca_tam_tru, text="Đến ngày", font=font_content,
                      anchor=W, justify=LEFT).grid(column=3, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_xem_tat_ca_tam_tru, text="Xem chi tiết", font=font_content,
                      anchor=W, justify=LEFT).grid(column=4, row=1, columnspan=1, sticky=NW)

        for j in range(8):
            if (i*8 + j >= n):
                break
            tkinter.Label(f_all_xem_tat_ca_tam_tru, text=listTamTru[i*8 + j].HoTen, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=200).grid(column=0, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_xem_tat_ca_tam_tru, text=listTamTru[i*8 + j].CCCD, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=100).grid(column=1, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_xem_tat_ca_tam_tru, text=listTamTru[i*8 + j].Tu, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=100).grid(column=2, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_xem_tat_ca_tam_tru, text=listTamTru[i*8 + j].Den, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=100).grid(column=3, row=j+2, columnspan=1, sticky=NW)
            tkinter.Button(f_all_xem_tat_ca_tam_tru, text="Chi tiết", font=font_content_mini, anchor=W, fg="white",
                           bg="blue", cursor="hand2", command=lambda data=i*8+j: showDetail(data)).grid(column=4, row=j+2, columnspan=1, sticky=NW)
        if (i != 0):
            tkinter.Button(
                f_all_xem_tat_ca_tam_tru, text="Trang trước",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i-1)).grid(column=0, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)
        if (i != times-1):
            tkinter.Button(
                f_all_xem_tat_ca_tam_tru, text="Trang sau",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i+1)).grid(column=4, row=10, sticky=E, padx=padx, pady=pady, columnspan=1)

        def showDetail(data):
            XemGiayTamTru(listTamTru[data], f_xem_tat_ca_tam_tru)

    showPage(0)


'''Tạm vắng'''


def TamVang():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_all_tam_vang = tkinter.Frame(
        f_tam_vang, highlightbackground="black", highlightthickness=2)
    f_tam_vang.grid_columnconfigure(0, weight=1)
    f_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_tam_vang.grid(column=0, row=0, sticky='news', padx=10, pady=10)
    tkinter.Label(f_all_tam_vang, text="Tạm vắng", font=font_header1, justify=LEFT).grid(
        column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_tam_vang, text="Chọn yêu cầu của bạn: ", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Tạo giấy tạm vắng", "Xem giấy tạm vắng", "Xem tất cả tạm vắng")
    chosed = StringVar(f_all_tam_vang)
    dropDownTamVang = ttk.OptionMenu(
        f_all_tam_vang, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownTamVang['menu'].configure(font=('Arial', 12))
    dropDownTamVang.grid(column=1, row=1, sticky=W,
                         padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_tam_vang, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def submit(chose):
        if (chose == "Tạo giấy tạm vắng"):
            switch(f_tao_giay_tam_vang)
        elif (chose == "Xem giấy tạm vắng"):
            switch(f_authen_xem_giay_tam_vang)
        elif (chose == "Xem tất cả tạm vắng"):
            switch(f_xem_tat_ca_tam_vang)


# HoTen, CCCD, NoiTamVang, NgayBatDau: datetime.datetime, NgayKetThuc: datetime.datetime, LyDo, NgayLamDon: datetime.datetime

def TaoGiayTamVang():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_tao_giay_tam_vang = tkinter.Frame(
        f_tao_giay_tam_vang, highlightbackground="black", highlightthickness=2)
    f_tao_giay_tam_vang.grid_columnconfigure(0, weight=1)
    f_tao_giay_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_tao_giay_tam_vang.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_tao_giay_tam_vang.grid_columnconfigure(0, weight=1)
    f_all_tao_giay_tam_vang.grid_columnconfigure(1, weight=1)
    f_all_tao_giay_tam_vang.grid_columnconfigure(2, weight=1)
    f_all_tao_giay_tam_vang.grid_columnconfigure(3, weight=1)
    # row 0
    tkinter.Label(f_all_tao_giay_tam_vang, text="Đơn xin tạm vắng", font=font_header1).grid(
        column=0, row=0, padx=padx, pady=0, columnspan=4)

    # row 1
    tkinter.Label(f_all_tao_giay_tam_vang, text="Tên tôi là:", font=font_content, anchor=W).grid(
        column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    hoVaTen = tkinter.Entry(f_all_tao_giay_tam_vang,
                            font=font_content)
    hoVaTen.grid(column=1, row=1, sticky=W,
                 padx=padx, pady=pady, columnspan=3)
    # row 2
    tkinter.Label(f_all_tao_giay_tam_vang, text="CCCD:", font=font_content, anchor=W).grid(
        column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    CCCD = tkinter.Entry(f_all_tao_giay_tam_vang, font=font_content, width=20)
    CCCD.grid(column=1, row=2, sticky=W,
              padx=padx, pady=pady, columnspan=1)

    # row 3
    tkinter.Label(f_all_tao_giay_tam_vang, text="Nơi tạm vắng:", font=font_content, anchor=W).grid(
        column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)
    noiTamVang = tkinter.Entry(f_all_tao_giay_tam_vang,
                               font=font_content, width=60)
    noiTamVang.grid(column=1, row=3, sticky=W,
                    padx=padx, pady=pady, columnspan=3)

    # row 5
    tkinter.Label(f_all_tao_giay_tam_vang, text="Từ ngày: ", font=font_content, anchor=W).grid(
        column=0, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    tuNgay = DateEntry(f_all_tao_giay_tam_vang, font=font_content)
    tuNgay.grid(column=1, row=5, sticky=W,
                padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_tao_giay_tam_vang, text="Đến ngày: ", font=font_content, anchor=W).grid(
        column=2, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    denNgay = DateEntry(f_all_tao_giay_tam_vang, font=font_content)
    denNgay.grid(column=3, row=5, sticky=W,
                 padx=padx, pady=pady, columnspan=1)

    # row 6
    tkinter.Label(f_all_tao_giay_tam_vang, text="Lý do:", font=font_content, anchor=W).grid(
        column=0, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)
    lyDo = tkinter.Text(
        f_all_tao_giay_tam_vang, font=font_content, height=10, width=60, wrap=WORD)
    lyDo.grid(column=1, row=6, sticky=W,
              padx=padx, pady=pady, columnspan=3)

    # row 7

    tkinter.Label(f_all_tao_giay_tam_vang, text="Ngày làm đơn: ", font=font_content, anchor=W).grid(
        column=0, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)

    ngayLamDon = DateEntry(f_all_tao_giay_tam_vang, font=font_content)
    ngayLamDon.grid(column=1, row=7, sticky=W,
                    padx=padx, pady=pady, columnspan=1)

    # row 8
    tkinter.Button(f_all_tao_giay_tam_vang, text="Xác nhận",  font=font_header3, fg="white", bg="blue", cursor='hand2', command=lambda: submit()).grid(
        column=0, row=8, padx=padx, pady=pady, columnspan=4)

    errorMessage = tkinter.Label(
        f_all_tao_giay_tam_vang, text="", font=font_content, fg="red", justify=CENTER)
    errorMessage.grid(column=0, row=9, columnspan=4)

    def submit():
        if (hoVaTen.get() == "" or CCCD.get() == "" or noiTamVang.get() == "" or lyDo.get("1.0", 'end-1c') == ""):
            errorMessage['text'] = "Vui lòng điền đầy đủ các trường!"
            return
        errorCode = ChucNang.CapGiayTamVang(hoVaTen.get(), CCCD.get(), noiTamVang.get(), tuNgay.get_date().strftime(
            "%m/%d/%y"), denNgay.get_date().strftime("%m/%d/%y"), lyDo.get("1.0", 'end-1c'), ngayLamDon.get_date().strftime("%m/%d/%y"))
        if (errorCode == 0):
            messagebox.showinfo("", "Đã hoàn thành đơn tạm vắng")
            switch(f_trang_chu)
        elif (errorCode == 1):
            errorMessage['text'] = "Vui lòng kiểm tra lại thông tin!"
            return


def AuthenXemGiayTamVang():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_all_authen_xem_giay_tam_vang = tkinter.Frame(
        f_authen_xem_giay_tam_vang, highlightbackground="black", highlightthickness=2)
    f_authen_xem_giay_tam_vang.grid_columnconfigure(0, weight=1)
    f_authen_xem_giay_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_authen_xem_giay_tam_vang.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)
    tkinter.Label(f_all_authen_xem_giay_tam_vang, text="Xem giấy tạm vắng", font=font_header1,
                  justify=LEFT).grid(column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_authen_xem_giay_tam_vang, text="Họ và tên:", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    hoVaTen = tkinter.Entry(
        f_all_authen_xem_giay_tam_vang, font=font_content, width=20)
    hoVaTen.grid(column=1, row=1, sticky=W,
                 padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_authen_xem_giay_tam_vang, text="CCCD:", font=font_content, anchor=W).grid(column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    CCCD = tkinter.Entry(
        f_all_authen_xem_giay_tam_vang, font=font_content, width=20)
    CCCD.grid(column=1, row=2, sticky=W,
              padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_xem_giay_tam_vang, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit()).grid(column=0, row=3, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_xem_giay_tam_vang, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=4, padx=padx,
                      pady=pady, sticky=N, columnspan=2)

    def submit():
        if (hoVaTen.get() == "" or CCCD.get() == ""):
            errorMessage['text'] = "Vui lòng nhập đầy đủ thông tin!"
            return

        errorCode, thongTinGiayTamVang = ChucNang.XemGiayTamVang(
            hoVaTen.get(), CCCD.get())
        if (errorCode == 1):
            errorMessage['text'] = "Thông tin bị sai!. Vui lòng nhập lại"
        elif (errorCode == 2):
            errorMessage['text'] = "Người này không có giấy tạm vắng"
        else:
            XemGiayTamVang(thongTinGiayTamVang, f_trang_chu)


# MaGiayTamVang, HoTen, CCCD, NoiTamVang ,Tu, Den, LyDo, NgayLamDon

def XemGiayTamVang(thongTinGiayTamVang, frame):
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_xem_giay_tam_vang.tkraise()
    for widget in f_xem_giay_tam_vang.winfo_children():
        widget.destroy()
    f_all_xem_giay_tam_vang = tkinter.Frame(
        f_xem_giay_tam_vang, highlightbackground="black", highlightthickness=2)
    f_xem_giay_tam_vang.grid_columnconfigure(0, weight=1)
    f_xem_giay_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_xem_giay_tam_vang.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_xem_giay_tam_vang.grid_columnconfigure(0, weight=1)
    f_all_xem_giay_tam_vang.grid_columnconfigure(1, weight=1)
    f_all_xem_giay_tam_vang.grid_columnconfigure(2, weight=1)
    f_all_xem_giay_tam_vang.grid_columnconfigure(3, weight=1)
    # row 0
    tkinter.Label(f_all_xem_giay_tam_vang, text="Đơn xin tạm vắng", font=font_header1).grid(
        column=0, row=0, padx=padx, pady=0, columnspan=4)
    # row 1
    tkinter.Label(f_all_xem_giay_tam_vang, text="Tên tôi là: ", font=font_content, anchor=W).grid(
        column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    tkinter.Label(f_all_xem_giay_tam_vang, text=thongTinGiayTamVang.HoTen,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=3, padx=padx, pady=pady, sticky=W)
    # row 2
    tkinter.Label(f_all_xem_giay_tam_vang, text="CCCD:", font=font_content, anchor=W).grid(
        column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    tkinter.Label(f_all_xem_giay_tam_vang, text=thongTinGiayTamVang.CCCD,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=2, columnspan=3, padx=padx, pady=pady, sticky=W)

    # row 3
    tkinter.Label(f_all_xem_giay_tam_vang, text="Nơi tạm vắng:", font=font_content, anchor=W).grid(
        column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)
    tkinter.Label(f_all_xem_giay_tam_vang, text=thongTinGiayTamVang.NoiTamVang,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=3, columnspan=3, padx=padx, pady=pady, sticky=W)

    # row 5
    tkinter.Label(f_all_xem_giay_tam_vang, text="Từ ngày: ", font=font_content, anchor=W).grid(
        column=0, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_xem_giay_tam_vang, text=thongTinGiayTamVang.Tu,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=5, columnspan=3, padx=padx, pady=pady, sticky=W)

    tkinter.Label(f_all_xem_giay_tam_vang, text="Đến ngày: ", font=font_content, anchor=W).grid(
        column=2, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_xem_giay_tam_vang, text=thongTinGiayTamVang.Den,
                  font=font_content, anchor=W, justify=LEFT).grid(column=3, row=5, columnspan=3, padx=padx, pady=pady, sticky=W)

    # row 6
    tkinter.Label(f_all_xem_giay_tam_vang, text="Lý do:", font=font_content, anchor=W).grid(
        column=0, row=6, sticky=NW, padx=padx, pady=pady, columnspan=1, rowspan=2)
    tkinter.Label(f_all_xem_giay_tam_vang, text=thongTinGiayTamVang.LyDo,
                  font=font_content, anchor=W, justify=LEFT, wraplength=500).grid(column=1, row=6, columnspan=3, rowspan=2, padx=padx, pady=pady, sticky=NW)

    # row 7

    tkinter.Label(f_all_xem_giay_tam_vang, text="Ngày làm đơn: ", font=font_content, anchor=W).grid(
        column=0, row=8, sticky=W, padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_xem_giay_tam_vang, text=thongTinGiayTamVang.NgayLamDon,
                  font=font_content, anchor=W, justify=LEFT).grid(column=1, row=8, columnspan=3, padx=padx, pady=pady, sticky=W)

    btn = tkinter.Button(f_all_xem_giay_tam_vang, text="", font=font_header3, fg="white", bg="blue", relief='groove',
                         cursor='hand2', command=lambda: switch(frame))
    btn.grid(column=0, row=9, columnspan=4, padx=padx, pady=pady)
    if (frame == f_trang_chu):
        btn['text'] = "Về trang chủ"
    elif (frame == f_xem_tat_ca_tam_vang):
        btn['text'] = "Trở lại"


def XemTatCaTamVang():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = selected_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_all_xem_tat_ca_tam_vang = tkinter.Frame(
        f_xem_tat_ca_tam_vang, highlightbackground="black", highlightthickness=2)
    f_xem_tat_ca_tam_vang.grid_columnconfigure(0, weight=1)
    f_xem_tat_ca_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_xem_tat_ca_tam_vang.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_xem_tat_ca_tam_vang.grid_columnconfigure(0, weight=2)
    f_all_xem_tat_ca_tam_vang.grid_columnconfigure(1, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_columnconfigure(2, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_columnconfigure(3, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_columnconfigure(4, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(1, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(2, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(3, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(4, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(5, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(6, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(7, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(8, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(9, weight=1)
    f_all_xem_tat_ca_tam_vang.grid_rowconfigure(10, weight=1)

    listTamVang = ChucNang.getAllTamVang()
    n = len(listTamVang)
    if (n != 0):
        times = ceil(n/8)

    def showPage(i):
        if (n == 0):
            tkinter.Label(f_all_xem_tat_ca_tam_vang, text="Tất cả tạm vắng", font=font_header1, justify=LEFT).grid(
                column=0, row=0, columnspan=5, padx=padx, pady=pady, sticky=N)

            tkinter.Label(f_all_xem_tat_ca_tam_vang, text="Không có giấy tạm vắng", fg="red",
                          font=font_header3).grid(column=0, row=1, columnspan=5, sticky=N)
        else:
            # Không cho đi về trước page đầu tiên
            if (i <= 0):
                i = 0
            # Không cho đi quá page cuối
            elif (i >= times-1):
                i = times-1
            # Xóa dữ liệu cũ
            for widget in f_all_xem_tat_ca_tam_vang.winfo_children():
                widget.destroy()
            # Hiện thông tin page thứ i
            XemTamVang(i)

    def XemTamVang(i):
        tkinter.Label(f_all_xem_tat_ca_tam_vang, text="Tất cả giấy tạm trú", font=font_header1, justify=LEFT).grid(
            column=0, row=0, columnspan=5, padx=padx, pady=pady, sticky=N)

        tkinter.Label(f_all_xem_tat_ca_tam_vang, text="Họ và tên", font=font_content,
                      anchor=W, justify=LEFT).grid(column=0, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_xem_tat_ca_tam_vang, text="CCCD", font=font_content,
                      anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_xem_tat_ca_tam_vang, text="Từ ngày", font=font_content,
                      anchor=W, justify=LEFT).grid(column=2, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_xem_tat_ca_tam_vang, text="Đến ngày", font=font_content,
                      anchor=W, justify=LEFT).grid(column=3, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_xem_tat_ca_tam_vang, text="Xem chi tiết", font=font_content,
                      anchor=W, justify=LEFT).grid(column=4, row=1, columnspan=1, sticky=NW)

        for j in range(8):
            if (i*8 + j >= n):
                break
            tkinter.Label(f_all_xem_tat_ca_tam_vang, text=listTamVang[i*8 + j].HoTen, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=200).grid(column=0, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_xem_tat_ca_tam_vang, text=listTamVang[i*8 + j].CCCD, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=100).grid(column=1, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_xem_tat_ca_tam_vang, text=listTamVang[i*8 + j].Tu, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=100).grid(column=2, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_xem_tat_ca_tam_vang, text=listTamVang[i*8 + j].Den, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=100).grid(column=3, row=j+2, columnspan=1, sticky=NW)
            tkinter.Button(f_all_xem_tat_ca_tam_vang, text="Chi tiết", font=font_content_mini, anchor=W, fg="white",
                           bg="blue", cursor="hand2", command=lambda data=i*8+j: showDetail(data)).grid(column=4, row=j+2, columnspan=1, sticky=NW)
        if (i != 0):
            tkinter.Button(
                f_all_xem_tat_ca_tam_vang, text="Trang trước",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i-1)).grid(column=0, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)
        if (i != times-1):
            tkinter.Button(
                f_all_xem_tat_ca_tam_vang, text="Trang sau",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i+1)).grid(column=4, row=10, sticky=E, padx=padx, pady=pady, columnspan=1)

        def showDetail(data):
            XemGiayTamVang(listTamVang[data], f_xem_tat_ca_tam_vang)

    showPage(0)


"""END HOME"""

# ------------------------------------------------------------------------------------------------------------------------------------

"""Family <=> Xem hộ khẩu"""
# Giao diện check mã hộ khẩu (hostId)


def AuthenFamily():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = selected_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_all_authen_family = tkinter.Frame(
        f_authen_family, highlightbackground="black", highlightthickness=2)
    f_authen_family.grid_columnconfigure(0, weight=1)
    f_authen_family.grid_rowconfigure(0, weight=1)
    f_all_authen_family.grid(column=0, row=0, sticky='news', padx=10, pady=10)
    tkinter.Label(f_all_authen_family, text="Sổ hộ khẩu", font=font_header1, justify=LEFT).grid(
        column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_authen_family, text="Chọn chức năng: ", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Thêm hộ khẩu mới", "Thay đổi thông tin hộ khẩu", "Xem hộ khẩu")
    chosed = StringVar(f_all_authen_family)
    dropDownGender = ttk.OptionMenu(
        f_all_authen_family, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownGender['menu'].configure(font=('Arial', 12))
    dropDownGender.grid(column=1, row=1, sticky=W,
                        padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_authen_family, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2',
        command=lambda: submit(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def submit(chose):
        if (chose == "Thêm hộ khẩu mới"):
            ThemHoKhau()
        elif (chose == "Thay đổi thông tin hộ khẩu"):
            ThayDoiThongTinHoKhau()
        elif (chose == "Xem hộ khẩu"):
            XemHoKhau()

# Thông tin nhân khẩu:
# ID ,CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú
# Giao diện xem nhân khẩu


def ThemHoKhau():
    for f in frames:
        for widget in f.winfo_children():
            widget.destroy()
    f_family.tkraise()
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = selected_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_family = tkinter.Frame(
        f_family, highlightbackground="black", highlightthickness=2)
    f_family.grid_columnconfigure(0, weight=1)
    f_family.grid_rowconfigure(0, weight=1)
    f_all_family.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_family.grid_rowconfigure(0, weight=1)
    f_all_family.grid_rowconfigure(1, weight=1)
    f_all_family.grid_rowconfigure(2, weight=1)
    f_all_family.grid_rowconfigure(3, weight=1)
    f_all_family.grid_rowconfigure(4, weight=1)
    f_all_family.grid_rowconfigure(5, weight=1)
    f_all_family.grid_rowconfigure(6, weight=1)
    f_all_family.grid_rowconfigure(7, weight=1)
    f_all_family.grid_columnconfigure(0, weight=1)
    f_all_family.grid_columnconfigure(1, weight=3)

    tkinter.Label(f_all_family, text="Thêm hộ khẩu", font=font_header1,
                  anchor=N, justify=CENTER).grid(column=0, row=0, columnspan=2)

    tkinter.Label(f_all_family, text="Mã hộ khẩu:",
                  font=font_content, anchor=W, justify=LEFT).grid(column=0, row=1, sticky=W, padx=padx, pady=pady)
    maHoKhau = tkinter.Entry(f_all_family, font=font_content,
                             width=60, justify=LEFT)
    maHoKhau.grid(column=1, row=1, sticky=W, padx=padx, pady=pady)

    tkinter.Label(f_all_family, text="Số nhà/tên đường:",
                  font=font_content, anchor=W, justify=LEFT).grid(column=0, row=2, sticky=W, padx=padx, pady=pady)
    soNhaTenDuong = tkinter.Entry(f_all_family, font=font_content,
                                  width=60, justify=LEFT)
    soNhaTenDuong.grid(column=1, row=2, sticky=W, padx=padx, pady=pady)

    tkinter.Label(f_all_family, text="Xã/Phường:",
                  font=font_content, anchor=W, justify=LEFT).grid(column=0, row=3, sticky=W, padx=padx, pady=pady)
    xaPhuong = tkinter.Entry(f_all_family, font=font_content,
                             width=60, justify=LEFT)
    xaPhuong.grid(column=1, row=3, sticky=W, padx=padx, pady=pady)

    tkinter.Label(f_all_family, text="Quận/Huyện:",
                  font=font_content, anchor=W, justify=LEFT).grid(column=0, row=4, sticky=W, padx=padx, pady=pady)
    quanHuyen = tkinter.Entry(f_all_family, font=font_content,
                              width=60, justify=LEFT)
    quanHuyen.grid(column=1, row=4, sticky=W, padx=padx, pady=pady)

    tkinter.Label(f_all_family, text="Tỉnh/Thành phố:",
                  font=font_content, anchor=W, justify=LEFT).grid(column=0, row=5, sticky=W, padx=padx, pady=pady)
    tinhThanhPho = tkinter.Entry(f_all_family, font=font_content,
                                 width=60, justify=LEFT)
    tinhThanhPho.grid(column=1, row=5, sticky=W, padx=padx, pady=pady)

    tkinter.Button(f_all_family, text="Thêm", font=font_header3, bg="blue", cursor='hand2',
                   fg="white", command=lambda: submit()).grid(column=0, row=6, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_family, text="", fg="red", justify=CENTER, font=font_content)
    errorMessage.grid(column=0, row=7, columnspan=2,
                      sticky=N, padx=padx, pady=pady)

    def submit():
        maSo = maHoKhau.get()
        nha = soNhaTenDuong.get()
        xa = xaPhuong.get()
        quan = quanHuyen.get()
        tinh = tinhThanhPho.get()

        if (maSo == "" or nha == "" or xa == "" or quan == "" or tinh == ""):
            errorMessage['text'] = "Vui lòng nhập đầy đủ thông tin!"
            return
        if (len(maSo) != 9):
            errorMessage['text'] = "Mã hộ khẩu phải có 9 chữ số"
        else:
            errorCode = ChucNang.TaoHoKhauMoi(maSo, nha, xa, quan, tinh)
            if (errorCode):
                errorMessage['text'] = "Vui lòng kiểm tra lại mã hộ khẩu!"
                return
            else:
                pyperclip.copy(maSo)
                messagebox.showinfo(
                    "", 'Sổ hộ khẩu với mã sổ: ' + str(maSo) + " đã được tạo")
                switch(f_trang_chu)


def ThayDoiThongTinHoKhau():
    for f in frames:
        for widget in f.winfo_children():
            widget.destroy()
    f_family.tkraise()
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = selected_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_family = tkinter.Frame(
        f_family, highlightbackground="black", highlightthickness=2)
    f_family.grid_columnconfigure(0, weight=1)
    f_family.grid_rowconfigure(0, weight=1)
    f_all_family.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_family.grid_columnconfigure(0, weight=1)
    f_all_family.grid_columnconfigure(1, weight=1)
    f_all_family.grid_columnconfigure(2, weight=1)
    f_all_family.grid_columnconfigure(3, weight=1)

    tkinter.Label(f_all_family, text="Thay đổi thông tin hộ khẩu", font=font_header1, justify=CENTER,
                  anchor=W).grid(column=0, row=0, columnspan=2, sticky=W, padx=padx, pady=pady)
    tkinter.Label(f_all_family, text="Nhập mã hộ khẩu", font=font_content,
                  justify=LEFT, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady)
    maHoKhau = tkinter.Entry(
        f_all_family, font=font_content, justify=LEFT, width=20)
    maHoKhau.grid(column=1, row=1, sticky=W, padx=padx, pady=pady)

    tkinter.Button(f_all_family, text="Gửi", font=font_content, fg="white", bg="blue", cursor='hand2',
                   command=lambda: submitAuthen()).grid(column=0, row=2, columnspan=2, padx=padx, pady=pady)

    errorMessage = tkinter.Label(
        f_all_family, text="", font=font_content, fg="red")
    errorMessage.grid(column=0, row=3, columnspan=2, padx=padx, pady=pady)

    def submitAuthen():
        maSo = maHoKhau.get()
        if (maSo == ""):
            errorMessage['text'] = "Vui lòng điền mã hộ khẩu"
            return
        else:
            errorCode, hoKhau = ChucNang.GetThongTinHoKhau(maSo)
            if (errorCode):
                errorMessage['text'] = "Vui lòng kiểm tra lại mã hộ khẩu"
            else:
                View(hoKhau)

    def View(hoKhau):
        for widget in f_all_family.winfo_children():
            widget.destroy()

        f_all_family.grid_rowconfigure(0, weight=1)
        f_all_family.grid_rowconfigure(1, weight=1)
        f_all_family.grid_rowconfigure(2, weight=1)
        f_all_family.grid_rowconfigure(3, weight=1)
        f_all_family.grid_rowconfigure(4, weight=1)
        f_all_family.grid_rowconfigure(5, weight=1)
        f_all_family.grid_rowconfigure(6, weight=1)
        f_all_family.grid_rowconfigure(7, weight=1)
        f_all_family.grid_columnconfigure(0, weight=1)
        f_all_family.grid_columnconfigure(1, weight=3)

        tkinter.Label(f_all_family, text="Thay đổi thông tin hộ khẩu", font=font_header1,
                      anchor=N, justify=CENTER).grid(column=0, row=0, columnspan=2)

        tkinter.Label(f_all_family, text="Số nhà/tên đường:",
                      font=font_content, anchor=W, justify=LEFT).grid(column=0, row=1, sticky=W, padx=padx, pady=pady)
        soNhaTenDuong = tkinter.Entry(f_all_family, font=font_content,
                                      width=60, justify=LEFT)
        soNhaTenDuong.grid(column=1, row=1, sticky=W, padx=padx, pady=pady)
        soNhaTenDuong.insert(0, hoKhau.SoNha)

        tkinter.Label(f_all_family, text="Xã/Phường:",
                      font=font_content, anchor=W, justify=LEFT).grid(column=0, row=2, sticky=W, padx=padx, pady=pady)
        xaPhuong = tkinter.Entry(f_all_family, font=font_content,
                                 width=60, justify=LEFT)
        xaPhuong.grid(column=1, row=2, sticky=W, padx=padx, pady=pady)
        xaPhuong.insert(0, hoKhau.Phuong)
        tkinter.Label(f_all_family, text="Quận/Huyện:",
                      font=font_content, anchor=W, justify=LEFT).grid(column=0, row=3, sticky=W, padx=padx, pady=pady)
        quanHuyen = tkinter.Entry(f_all_family, font=font_content,
                                  width=60, justify=LEFT)
        quanHuyen.grid(column=1, row=3, sticky=W, padx=padx, pady=pady)
        quanHuyen.insert(0, hoKhau.Huyen)
        tkinter.Label(f_all_family, text="Tỉnh/Thành phố:",
                      font=font_content, anchor=W, justify=LEFT).grid(column=0, row=4, sticky=W, padx=padx, pady=pady)
        tinhThanhPho = tkinter.Entry(f_all_family, font=font_content,
                                     width=60, justify=LEFT)
        tinhThanhPho.grid(column=1, row=4, sticky=W, padx=padx, pady=pady)
        tinhThanhPho.insert(0, hoKhau.Tinh)
        tkinter.Button(f_all_family, text="Xác nhận", font=font_header3, bg="blue", cursor='hand2',
                       fg="white", command=lambda: submit()).grid(column=0, row=5, columnspan=2)

        errorMessage = tkinter.Label(
            f_all_family, text="", fg="red", justify=CENTER, font=font_content)
        errorMessage.grid(column=0, row=6, columnspan=2,
                          sticky=N, padx=padx, pady=pady)

        def submit():
            if (soNhaTenDuong.get() == "" or xaPhuong.get() == "" or quanHuyen.get() == "" or tinhThanhPho.get() == ""):
                errorMessage['text'] = "Vui lòng nhập đầy đủ thông tin"
                return
            ChucNang.UpdateThongTinHoKhau(hoKhau.MaSo, soNhaTenDuong.get(
            ), xaPhuong.get(), quanHuyen.get(), tinhThanhPho.get())
            messagebox.showinfo("", "Đã cập nhật thành công")
            switch(f_trang_chu)


def XemHoKhau():
    for f in frames:
        for widget in f.winfo_children():
            widget.destroy()
    f_family.tkraise()
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = selected_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    # Create a child frame to destroy when no use parent frame
    f_all_family = tkinter.Frame(
        f_family, highlightbackground="black", highlightthickness=2)
    f_family.grid_columnconfigure(0, weight=1)
    f_family.grid_rowconfigure(0, weight=1)
    f_all_family.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_family.grid_columnconfigure(0, weight=1)
    f_all_family.grid_columnconfigure(1, weight=1)
    f_all_family.grid_columnconfigure(2, weight=1)
    f_all_family.grid_columnconfigure(3, weight=1)

    tkinter.Label(f_all_family, text="Xem hộ khẩu", font=font_header1,
                  anchor=W, justify=LEFT).grid(column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)
    tkinter.Label(f_all_family, text="Chọn phương thức tìm hộ khẩu",
                  font=font_content, justify=LEFT).grid(column=0, row=1, columnspan=2, padx=padx, pady=pady, sticky=W)
    option = ("Tìm bằng mã hộ khẩu", "Tìm bằng thông tin bản thân")
    chosed = StringVar(f_all_family)
    dropDownXemHoKhau = ttk.OptionMenu(
        f_all_family, chosed, option[0], *option, style='DropDownStyle.TMenubutton', command=lambda x=None: commandDrop())
    dropDownXemHoKhau['menu'].configure(font=('Arial', 12))
    dropDownXemHoKhau.grid(column=0, row=2, sticky=W,
                           padx=padx, pady=pady, columnspan=2)

    def commandDrop():
        if (chosed.get() == "Tìm bằng mã hộ khẩu"):
            for widget in f_all_family.grid_slaves():
                if (widget.grid_info()['row'] > 2):
                    widget.grid_forget()
            tkinter.Label(
                f_all_family, text="Nhập mã hộ khẩu:", font=font_content, anchor=W).grid(column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)
            maHoKhau = tkinter.Entry(
                f_all_family, font=font_content, width=20)
            maHoKhau.grid(column=1, row=3, sticky=W,
                          padx=padx, pady=pady, columnspan=1)

            tkinter.Button(
                f_all_family, text="Gửi", font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(maHoKhau.get(), errorMessage)).grid(column=0, row=4, padx=padx, pady=pady, columnspan=2)

            errorMessage = tkinter.Label(
                f_all_family, text="", font=font_content, fg="red", anchor=W)
            errorMessage.grid(column=0, row=5, padx=padx,
                              pady=pady, sticky=N, columnspan=2)

            def submit(maHoKhau, errorMessage):
                if (maHoKhau == ""):
                    errorMessage['text'] = "Vui lòng nhập mã hộ khẩu muốn xem"
                    return
                errorCode, hoKhau, listCuDan = ChucNang.XemSoHoKhau(
                    MaSo=maHoKhau)
                if (errorCode == 2):
                    errorMessage['text'] = f"Số hộ khẩu: {maHoKhau} bị sai!. Vui lòng nhập lại"

                else:
                    XemNhanKhau(listCuDan)
        elif (chosed.get() == "Tìm bằng thông tin bản thân"):
            for widget in f_all_family.grid_slaves():
                if (widget.grid_info()['row'] > 2):
                    widget.grid_forget()

            tkinter.Label(f_all_family, text="Họ và tên:", font=font_content,
                          anchor=W, justify=LEFT).grid(column=0, row=3, columnspan=1, sticky=NW, padx=padx, pady=pady)
            hoVaTen = tkinter.Entry(f_all_family, font=font_content, width=40)
            hoVaTen.grid(column=1, row=3, columnspan=3,
                         sticky=NW, padx=padx, pady=pady)

            tkinter.Label(f_all_family, text="CCCD:", font=font_content,
                          anchor=W, justify=LEFT).grid(column=0, row=4, columnspan=1, sticky=NW, padx=padx, pady=pady)
            CCCD = tkinter.Entry(f_all_family, font=font_content, width=40)
            CCCD.grid(column=1, row=4, columnspan=1,
                      sticky=NW, padx=padx, pady=pady)

            tkinter.Button(
                f_all_family, text="Gửi", font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(hoVaTen.get(), CCCD.get(), errorMessage)).grid(column=0, row=5, padx=padx, pady=pady, columnspan=2)

            errorMessage = tkinter.Label(
                f_all_family, text="", font=font_content, fg="red", anchor=W)
            errorMessage.grid(column=0, row=6, padx=padx,
                              pady=pady, sticky=N, columnspan=2)

            def submit(hovaten, CCCD, errorMessage):
                if (hovaten == "" or CCCD == ""):
                    errorMessage['text'] = "Vui lòng nhập đầy đủ thông tin!"
                    return
                errorCode, hoKhau, listCuDan = ChucNang.XemSoHoKhau(
                    hoTen=hovaten, CCCD=CCCD)
                if (errorCode == 1):
                    errorMessage['text'] = "Vui lòng kiểm tra lại họ tên và CCCD"
                elif (errorCode == 2):
                    errorMessage['text'] = "Không tìm thấy hộ khẩu của người này"
                else:
                    XemNhanKhau(listCuDan)

    def XemNhanKhau(listCuDan):
        for widget in f_all_family.winfo_children():
            widget.destroy()
        n = len(listCuDan)

        f_all_family.grid_columnconfigure(0, weight=1)
        f_all_family.grid_columnconfigure(1, weight=1)
        f_all_family.grid_columnconfigure(2, weight=1)
        f_all_family.grid_columnconfigure(3, weight=1)

        def showPerson(i):
            if (n == 0):
                f_all_family.grid_columnconfigure(0, weight=1)
                f_all_family.grid_rowconfigure(0, weight=1)
                f_all_family.grid_columnconfigure(4, weight=0)

                tkinter.Label(f_all_family, text="Không có data", fg="red",
                              font=font_header1).grid(column=0, row=0, columnspan=4, sticky=N)
            else:
                # Không cho đi về trước nhân khẩu đầu tiên
                if (i <= 0):
                    i = 0
                # Không cho đi quá nhân khẩu cuối
                elif (i >= n-1):
                    i = n-1
                # Xóa dữ liệu cũ
                for widget in f_all_family.winfo_children():
                    widget.destroy()
                # Hiện thông tin nhân khẩu thứ i
                PersonInfo(i)

        def PersonInfo(i):
            # row 0
            tkinter.Label(
                f_all_family, text="Quan hệ với chủ hộ:", font=font_header3, anchor=W).grid(row=0, column=0, columnspan=2, padx=padx, pady=pady, sticky=W)
            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][11], font=font_content).grid(row=0, column=2, padx=padx, pady=pady, sticky=W, columnspan=2)

            # row 1
            tkinter.Label(
                f_all_family, text="Họ và tên:", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][2], font=font_content).grid(column=1, row=1, padx=padx, pady=pady, columnspan=3, sticky=W)

            # row 2
            tkinter.Label(
                f_all_family, text="Bí danh(Nếu có):", font=font_content, anchor=W).grid(column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][9], font=font_content).grid(column=1, row=2, padx=padx, pady=pady, columnspan=1, sticky=W)

            tkinter.Label(
                f_all_family, text="Nghề nghiệp : ", font=font_content, anchor=W).grid(column=2, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][7], font=font_content, justify=LEFT).grid(column=3, row=2, padx=padx, pady=pady, columnspan=1, sticky=W)

            # row 3
            tkinter.Label(
                f_all_family, text="Ngày sinh: ", font=font_content, anchor=W).grid(column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

            Label(
                f_all_family, anchor=W, text=listCuDan[i][4], font=font_content).grid(column=1, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, text="Giới tính: ", font=font_content, anchor=W).grid(column=2, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

            Label(
                f_all_family, anchor=W, text=listCuDan[i][3], font=font_content).grid(column=3, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

            # row 4
            tkinter.Label(
                f_all_family, text="Quê quán: ", font=font_content, anchor=W).grid(column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][8], font=font_content).grid(column=1, row=4, sticky=W, padx=padx, pady=pady, columnspan=3)

            # row 5
            tkinter.Label(
                f_all_family, text="Số căn cước công dân: ", anchor=W, font=font_content).grid(column=0, row=5, padx=padx, pady=pady, sticky=W, columnspan=2)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][1], font=font_content).grid(column=2, row=5, padx=padx, pady=pady, sticky=W, columnspan=2)

            # row 6
            tkinter.Label(
                f_all_family, text="Dân tộc: ", font=font_content, anchor=W).grid(column=0, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][5], font=font_content).grid(column=1, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, text="Quốc tịch: ", font=font_content, anchor=W).grid(column=2, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)
            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][6], font=font_content).grid(column=3, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)

            # row 7
            tkinter.Label(
                f_all_family, text="Địa chỉ cũ:", font=font_content, anchor=W).grid(column=0, row=7, sticky=W, padx=padx, pady=pady, columnspan=2)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][13], font=font_content).grid(column=1, row=7, padx=padx, pady=pady, columnspan=3, sticky=W)

            # row 8
            tkinter.Label(
                f_all_family, text="Ngày đăng ký thường trú:", font=font_content, anchor=W).grid(column=0, row=8, sticky=W, padx=padx, pady=pady, columnspan=2)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][12], font=font_content).grid(column=2, row=8, padx=padx, pady=pady, columnspan=2, sticky=W)

            # row 9
            tkinter.Label(
                f_all_family, text="Ngày chuyển đi:", font=font_content, anchor=W).grid(column=0, row=9, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][14], font=font_content).grid(column=1, row=9, padx=padx, pady=pady, columnspan=3, sticky=W)

            # row 10
            tkinter.Label(
                f_all_family, text="Nơi chuyển đi:", font=font_content, anchor=W).grid(column=0, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][15], font=font_content).grid(column=1, row=10, padx=padx, pady=pady, columnspan=3, sticky=W)
            # row 11
            tkinter.Label(
                f_all_family, text="Ghi chú:", font=font_content, anchor=W).grid(column=0, row=11, sticky=W, padx=padx, pady=pady, columnspan=1)

            tkinter.Label(
                f_all_family, anchor=W, text=listCuDan[i][16], font=font_content).grid(column=1, row=11, padx=padx, pady=pady, columnspan=3, sticky=W)
            # row 12
            if (i != 0):
                tkinter.Button(
                    f_all_family, text="Trang trước",  font=font_header3, fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPerson(i-1)).grid(column=0, row=12, sticky=W, padx=padx, pady=pady, columnspan=1)
            if (i != n-1):
                tkinter.Button(
                    f_all_family, text="Trang sau",  font=font_header3, fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPerson(i+1)).grid(column=3, row=12, sticky=E, padx=padx, pady=pady, columnspan=1)

        showPerson(0)


"""END FAMILY"""

'''Xem lịch sử'''


def LichSu():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = selected_bg
    f_all_lich_su = tkinter.Frame(f_lich_su)
    f_lich_su.grid_columnconfigure(0, weight=1)
    f_lich_su.grid_rowconfigure(0, weight=1)
    f_all_lich_su.grid(column=0, row=0, sticky='news', padx=10, pady=10)
    # f_all_lich_su.config(padx=10, pady=30)
    tkinter.Label(f_all_lich_su, text="Lịch sử", font=font_header1, justify=LEFT).grid(
        column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_lich_su, text="Chọn yêu cầu của bạn: ", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Xem lịch sử theo hộ khẩu", "Xem tất cả lịch sử")
    chosed = StringVar(f_all_lich_su)
    dropDownLichSu = ttk.OptionMenu(
        f_all_lich_su, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownLichSu['menu'].configure(font=('Arial', 12))
    dropDownLichSu.grid(column=1, row=1, sticky=W,
                        padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_lich_su, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def submit(chose):
        if (chose == "Xem lịch sử theo hộ khẩu"):
            switch(f_authen_lich_su_bien_doi_theo_ho_khau)
        elif (chose == "Xem tất cả lịch sử"):
            switch(f_tat_ca_lich_su_bien_doi)

# Thông tin một bảng thay đổi: MaBienDoi, Ngay, KieuBienDoi, NoiDungBienDoi, MaSo


def XemTatCaLichSuBienDoi():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = selected_bg
    f_all_tat_ca_lich_su = tkinter.Frame(
        f_tat_ca_lich_su_bien_doi, highlightbackground="black", highlightthickness=2)
    f_tat_ca_lich_su_bien_doi.grid_columnconfigure(0, weight=1)
    f_tat_ca_lich_su_bien_doi.grid_rowconfigure(0, weight=1)
    f_all_tat_ca_lich_su.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_tat_ca_lich_su.grid_columnconfigure(0, weight=1)
    f_all_tat_ca_lich_su.grid_columnconfigure(1, weight=2)
    f_all_tat_ca_lich_su.grid_columnconfigure(2, weight=4)
    f_all_tat_ca_lich_su.grid_columnconfigure(3, weight=10)
    f_all_tat_ca_lich_su.grid_columnconfigure(4, weight=2)
    f_all_tat_ca_lich_su.grid_rowconfigure(0, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(1, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(2, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(3, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(4, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(5, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(6, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(7, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(8, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(9, weight=1)
    f_all_tat_ca_lich_su.grid_rowconfigure(10, weight=1)

    errorCode, listLichSu = ChucNang.LayLichSuBienDoiNhanKhau()

    if (listLichSu == 1):
        n = 0
    else:
        n = len(listLichSu)
        times = ceil(n/8)

    def showPage(i):
        if (n == 0):
            tkinter.Label(f_all_tat_ca_lich_su, text="Tất cả lịch sử", font=font_header1, justify=LEFT).grid(
                column=0, row=0, columnspan=5, padx=padx, pady=pady, sticky=N)

            tkinter.Label(f_all_tat_ca_lich_su, text="Lịch sử trống", fg="red",
                          font=font_header3).grid(column=0, row=1, columnspan=5, sticky=N)
        else:
            # Không cho đi về trước page đầu tiên
            if (i <= 0):
                i = 0
            # Không cho đi quá page cuối
            elif (i >= times-1):
                i = times-1
            # Xóa dữ liệu cũ
            for widget in f_all_tat_ca_lich_su.winfo_children():
                widget.destroy()
            # Hiện thông tin page thứ i
            XemLichSu(i)

    def XemLichSu(i):
        tkinter.Label(f_all_tat_ca_lich_su, text="Tất cả lịch sử", font=font_header1, justify=LEFT).grid(
            column=0, row=0, columnspan=5, padx=padx, pady=pady, sticky=N)

        tkinter.Label(f_all_tat_ca_lich_su, text="ID", font=font_content,
                      anchor=W, justify=LEFT).grid(column=0, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_tat_ca_lich_su, text="Ngày", font=font_content,
                      anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_tat_ca_lich_su, text="Kiểu biến đổi", font=font_content,
                      anchor=W, justify=LEFT).grid(column=2, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_tat_ca_lich_su, text="Nội dung", font=font_content,
                      anchor=W, justify=LEFT).grid(column=3, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_tat_ca_lich_su, text="Mã hộ khẩu", font=font_content,
                      anchor=W, justify=LEFT).grid(column=4, row=1, columnspan=1, sticky=NW)

        for j in range(8):
            if (i*8 + j >= n):
                break
            tkinter.Label(f_all_tat_ca_lich_su, text=listLichSu[i*8 + j].MaBienDoi, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=35).grid(column=0, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_tat_ca_lich_su, text=listLichSu[i*8 + j].Ngay, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=70).grid(column=1, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_tat_ca_lich_su, text=listLichSu[i*8 + j].KieuBienDoi, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=140).grid(column=2, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_tat_ca_lich_su, text=listLichSu[i*8 + j].NoiDungBienDoi,
                          font=font_content_mini, anchor=W, justify=LEFT, wraplength=350).grid(column=3, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_tat_ca_lich_su, text=listLichSu[i*8 + j].MaSo, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=70).grid(column=4, row=j+2, columnspan=1, sticky=NW)
        if (i != 0):
            tkinter.Button(
                f_all_tat_ca_lich_su, text="Trang trước",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i-1)).grid(column=0, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)
        if (i != times-1):
            tkinter.Button(
                f_all_tat_ca_lich_su, text="Trang sau",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i+1)).grid(column=4, row=10, sticky=E, padx=padx, pady=pady, columnspan=1)

    if (errorCode == 1):
        switch(f_trang_chu)
    else:
        showPage(0)


def AuthenXemLichSuBienDoiTheoHoKhau():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = selected_bg
    # Create a child frame to destroy when no use parent frame
    f_all_authen_lich_su_gia_dinh = tkinter.Frame(
        f_authen_lich_su_bien_doi_theo_ho_khau, highlightbackground="black", highlightthickness=2)
    f_authen_lich_su_bien_doi_theo_ho_khau.grid_columnconfigure(0, weight=1)
    f_authen_lich_su_bien_doi_theo_ho_khau.grid_rowconfigure(0, weight=1)
    f_all_authen_lich_su_gia_dinh.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)
    tkinter.Label(f_all_authen_lich_su_gia_dinh, text="Xem lịch sử theo hộ khẩu", font=font_header1,
                  justify=LEFT).grid(column=0, row=0, columnspan=2, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_authen_lich_su_gia_dinh, text="Nhập mã hộ khẩu", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    maHoKhau = tkinter.Entry(
        f_all_authen_lich_su_gia_dinh, font=font_content, width=20)
    maHoKhau.grid(column=1, row=1, sticky=W,
                  padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_lich_su_gia_dinh, text="Gửi", font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(maHoKhau.get(), errorMessage)).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_lich_su_gia_dinh, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=3, padx=padx,
                      pady=pady, sticky=N, columnspan=2)

    def submit(maHoKhau, errorMessage):
        errorCode, hoKhau, listCuDan = ChucNang.XemSoHoKhau(maHoKhau)
        if (errorCode):
            errorMessage['text'] = f"Số hộ khẩu: {maHoKhau} bị sai!. Vui lòng nhập lại"

        else:
            switch(frame=f_lich_su_bien_doi_theo_ho_khau, maHoKhau=maHoKhau)


def XemLichSuBienDoiTheoHoKhau(maHoKhau):
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = selected_bg
    f_all_lich_su_gia_dinh = tkinter.Frame(
        f_lich_su_bien_doi_theo_ho_khau, highlightbackground="black", highlightthickness=2)
    f_lich_su_bien_doi_theo_ho_khau.grid_columnconfigure(0, weight=1)
    f_lich_su_bien_doi_theo_ho_khau.grid_rowconfigure(0, weight=1)
    f_all_lich_su_gia_dinh.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_lich_su_gia_dinh.grid_columnconfigure(0, weight=1)
    f_all_lich_su_gia_dinh.grid_columnconfigure(1, weight=2)
    f_all_lich_su_gia_dinh.grid_columnconfigure(2, weight=4)
    f_all_lich_su_gia_dinh.grid_columnconfigure(3, weight=10)
    f_all_lich_su_gia_dinh.grid_columnconfigure(4, weight=2)
    f_all_lich_su_gia_dinh.grid_rowconfigure(0, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(1, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(2, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(3, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(4, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(5, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(6, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(7, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(8, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(9, weight=1)
    f_all_lich_su_gia_dinh.grid_rowconfigure(10, weight=1)

    errorCode, listLichSu = ChucNang.XemLichSuBienDoiNhanKhau(maHoKhau)

    if (listLichSu == 1):
        n = 0
    else:
        n = len(listLichSu)
        times = ceil(n/8)

    def showPage(i):
        if (n == 0):
            tkinter.Label(f_all_lich_su_gia_dinh, text="Lịch sử của hộ khẩu "+str(maHoKhau), font=font_header1,
                          justify=LEFT).grid(column=0, row=0, columnspan=5, padx=padx, pady=pady, sticky=N)
            tkinter.Label(f_all_lich_su_gia_dinh, text="Lịch sử trống", fg="red",
                          font=font_header3).grid(column=0, row=1, columnspan=5, sticky=N)
        else:
            # Không cho đi về trước page đầu tiên
            if (i <= 0):
                i = 0
            # Không cho đi quá page cuối
            elif (i >= times-1):
                i = times-1
            # Xóa dữ liệu cũ
            for widget in f_all_lich_su_gia_dinh.winfo_children():
                widget.destroy()
            # Hiện thông tin page thứ i
            XemLichSu(i)

    def XemLichSu(i):
        tkinter.Label(f_all_lich_su_gia_dinh, text="Lịch sử của hộ khẩu "+str(maHoKhau), font=font_header1,
                      justify=LEFT).grid(column=0, row=0, columnspan=5, padx=padx, pady=pady, sticky=N)

        tkinter.Label(f_all_lich_su_gia_dinh, text="ID", font=font_content,
                      anchor=W, justify=LEFT).grid(column=0, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_lich_su_gia_dinh, text="Ngày", font=font_content,
                      anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_lich_su_gia_dinh, text="Kiểu biến đổi", font=font_content,
                      anchor=W, justify=LEFT).grid(column=2, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_lich_su_gia_dinh, text="Nội dung", font=font_content,
                      anchor=W, justify=LEFT).grid(column=3, row=1, columnspan=1, sticky=NW)
        tkinter.Label(f_all_lich_su_gia_dinh, text="Mã hộ khẩu", font=font_content,
                      anchor=W, justify=LEFT).grid(column=4, row=1, columnspan=1, sticky=NW)

        for j in range(8):
            if (i*8 + j >= n):
                break
            tkinter.Label(f_all_lich_su_gia_dinh, text=listLichSu[i*8 + j].MaBienDoi, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=35).grid(column=0, row=j+2, columnspan=1, sticky=N)
            tkinter.Label(f_all_lich_su_gia_dinh, text=listLichSu[i*8 + j].Ngay, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=70).grid(column=1, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_lich_su_gia_dinh, text=listLichSu[i*8 + j].KieuBienDoi, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=140).grid(column=2, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_lich_su_gia_dinh, text=listLichSu[i*8 + j].NoiDungBienDoi,
                          font=font_content_mini, anchor=W, justify=LEFT, wraplength=350).grid(column=3, row=j+2, columnspan=1, sticky=NW)
            tkinter.Label(f_all_lich_su_gia_dinh, text=listLichSu[i*8 + j].MaSo, font=font_content_mini,
                          anchor=W, justify=LEFT, wraplength=70).grid(column=4, row=j+2, columnspan=1, sticky=NW)
        if (i != 0):
            tkinter.Button(
                f_all_lich_su_gia_dinh, text="Trang trước",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i-1)).grid(column=0, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)
        if (i != times-1):
            tkinter.Button(
                f_all_lich_su_gia_dinh, text="Trang sau",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i+1)).grid(column=4, row=10, sticky=E, padx=padx, pady=pady, columnspan=1)

    if (errorCode == 1):
        switch(f_trang_chu)
    else:
        showPage(0)


'''Thống kê'''


def ThongKe():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = selected_bg
    btn_lich_su_bg = win_bg
    f_all_thong_ke = tkinter.Frame(
        f_thong_ke, highlightbackground="black", highlightthickness=2)
    f_thong_ke.grid_columnconfigure(0, weight=1)
    f_thong_ke.grid_rowconfigure(0, weight=1)
    f_all_thong_ke.grid(column=0, row=0, sticky='news', padx=10, pady=10)
    tkinter.Label(f_all_thong_ke, text="Thống kê", font=font_header1, justify=LEFT).grid(
        column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_thong_ke, text="Chọn yêu cầu của bạn: ", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Thống kê theo giới tính", "Thống kê theo độ tuổi",
              "Thống kê tạm trú tạm vắng")
    chosed = StringVar(f_all_thong_ke)
    dropDownTamVang = ttk.OptionMenu(
        f_all_thong_ke, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownTamVang['menu'].configure(font=('Arial', 12))
    dropDownTamVang.grid(column=1, row=1, sticky=W,
                         padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_thong_ke, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def submit(chose):
        if (chose == "Thống kê theo giới tính"):
            switch(f_thong_ke_theo_gioi_tinh)
        elif (chose == "Thống kê theo độ tuổi"):
            switch(f_thong_ke_theo_do_tuoi)
        elif (chose == "Thống kê tạm trú tạm vắng"):
            switch(f_thong_ke_tam_tru_tam_vang)


def ThongKeTheoDoTuoi():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = selected_bg
    btn_lich_su_bg = win_bg
    f_all_thong_ke_theo_do_tuoi = tkinter.Frame(
        f_thong_ke_theo_do_tuoi, highlightbackground="black", highlightthickness=2, bg="white")
    f_thong_ke_theo_do_tuoi.grid_columnconfigure(0, weight=1)
    f_thong_ke_theo_do_tuoi.grid_rowconfigure(0, weight=1)

    f_all_thong_ke_theo_do_tuoi.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_thong_ke_theo_do_tuoi.grid_columnconfigure(0, weight=1)
    f_all_thong_ke_theo_do_tuoi.grid_rowconfigure(0, weight=1)
    f_all_thong_ke_theo_do_tuoi.grid_rowconfigure(1, weight=10)

    tkinter.Label(f_all_thong_ke_theo_do_tuoi, text="Thống kê theo độ tuổi", font=font_header1, bg="white",
                  anchor=N, justify=CENTER).grid(column=0, row=0, columnspan=1, sticky=N)

    f = Figure(figsize=(5, 4), dpi=100)
    ax = f.add_subplot(111)

    data = ChucNang.ThongKeTheoDoTuoi()

    feild = ["Mầm non", "Mẫu giáo", "Cấp 1", "Cấp 2", "Cấp 3",
             "Lao động", "Nghỉ hưu"]  # the x locations for the groups
    width = .5

    ax.bar(feild, data, width)
    ax.set_title('Thống kê theo độ tuổi')

    for i, v in enumerate(data):
        ax.text(i-0.05, v+0.5, str(v), color="black")

    canvas = FigureCanvasTkAgg(f, master=f_all_thong_ke_theo_do_tuoi)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=1, columnspan=1, sticky='news')


def ThongKeTheoGioiTinh():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = selected_bg
    btn_lich_su_bg = win_bg
    MaleColor = "blue"
    FemaleColor = "orange"
    f_all_thong_ke_theo_gioi_tinh = tkinter.Frame(
        f_thong_ke_theo_gioi_tinh, highlightbackground="black", highlightthickness=2, bg="white")
    f_thong_ke_theo_gioi_tinh.grid_columnconfigure(0, weight=1)
    f_thong_ke_theo_gioi_tinh.grid_rowconfigure(0, weight=1)

    f_all_thong_ke_theo_gioi_tinh.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_thong_ke_theo_gioi_tinh.grid_columnconfigure(0, weight=10)
    f_all_thong_ke_theo_gioi_tinh.grid_columnconfigure(1, weight=1)
    f_all_thong_ke_theo_gioi_tinh.grid_columnconfigure(2, weight=1)
    f_all_thong_ke_theo_gioi_tinh.grid_columnconfigure(3, weight=1)
    f_all_thong_ke_theo_gioi_tinh.grid_rowconfigure(0, weight=1)
    f_all_thong_ke_theo_gioi_tinh.grid_rowconfigure(1, weight=1)
    f_all_thong_ke_theo_gioi_tinh.grid_rowconfigure(2, weight=1)
    f_all_thong_ke_theo_gioi_tinh.grid_rowconfigure(3, weight=1)
    f_all_thong_ke_theo_gioi_tinh.grid_rowconfigure(4, weight=10)

    data = ChucNang.ThongKeGioiTinh()

    tkinter.Label(f_all_thong_ke_theo_gioi_tinh, text="Thống kê theo giới tính", font=font_header1, bg="white",
                  anchor=N, justify=CENTER).grid(column=0, row=0, columnspan=4, sticky=N)
    tkinter.Label(f_all_thong_ke_theo_gioi_tinh, font=font_content,
                  text="Số lượng: ", bg='white').grid(column=1, row=1, columnspan=3, sticky=W)
    tkinter.Label(f_all_thong_ke_theo_gioi_tinh, font=font_content, text="", bg=MaleColor,
                  height=1, width=4).grid(column=1, row=2, columnspan=1, sticky=E)
    tkinter.Label(f_all_thong_ke_theo_gioi_tinh, font=font_content, text=data[0], bg="white",
                  height=1, width=4).grid(column=2, row=2, columnspan=1, sticky=W)

    tkinter.Label(f_all_thong_ke_theo_gioi_tinh, font=font_content, text="", bg=FemaleColor,
                  height=1, width=4).grid(column=1, row=3, columnspan=1, sticky=E)
    tkinter.Label(f_all_thong_ke_theo_gioi_tinh, font=font_content, text=data[1], bg="white",
                  height=1, width=4).grid(column=2, row=3, columnspan=1, sticky=W)
    label = ["Nam", "Nữ"]
    f = Figure()  # create a figure object
    ax = f.add_subplot(111)  # add an Axes to the figure
    ax.pie(data, radius=1, labels=label, colors=[MaleColor, FemaleColor],
           autopct='%0.2f%%', shadow=True)

    chart1 = FigureCanvasTkAgg(f, master=f_all_thong_ke_theo_gioi_tinh)
    chart1.get_tk_widget().grid(column=0, row=4, columnspan=4, sticky='news')


def ThongKeTamTruTamVang():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = win_bg
    btn_thong_ke_bg = selected_bg
    btn_lich_su_bg = win_bg
    TamTruColor = "blue"
    TamVangColor = "orange"
    f_all_thong_ke_tam_tru_tam_vang = tkinter.Frame(
        f_thong_ke_tam_tru_tam_vang, highlightbackground="black", highlightthickness=2, bg="white")
    f_thong_ke_tam_tru_tam_vang.grid_columnconfigure(0, weight=1)
    f_thong_ke_tam_tru_tam_vang.grid_rowconfigure(0, weight=1)

    f_all_thong_ke_tam_tru_tam_vang.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_thong_ke_tam_tru_tam_vang.grid_columnconfigure(0, weight=10)
    f_all_thong_ke_tam_tru_tam_vang.grid_columnconfigure(1, weight=1)
    f_all_thong_ke_tam_tru_tam_vang.grid_columnconfigure(2, weight=1)
    f_all_thong_ke_tam_tru_tam_vang.grid_columnconfigure(3, weight=1)
    f_all_thong_ke_tam_tru_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_thong_ke_tam_tru_tam_vang.grid_rowconfigure(1, weight=1)
    f_all_thong_ke_tam_tru_tam_vang.grid_rowconfigure(2, weight=1)
    f_all_thong_ke_tam_tru_tam_vang.grid_rowconfigure(3, weight=1)
    f_all_thong_ke_tam_tru_tam_vang.grid_rowconfigure(4, weight=10)

    data = ChucNang.ThongKeTamtruTamVang()

    tkinter.Label(f_all_thong_ke_tam_tru_tam_vang, text="Thống kê tạm trú tạm vắng", font=font_header1, bg="white",
                  anchor=N, justify=CENTER).grid(column=0, row=0, columnspan=4, sticky=N)
    tkinter.Label(f_all_thong_ke_tam_tru_tam_vang, font=font_content,
                  text="Số lượng: ", bg='white').grid(column=1, row=1, columnspan=3, sticky=W)
    tkinter.Label(f_all_thong_ke_tam_tru_tam_vang, font=font_content, text="", bg=TamTruColor,
                  height=1, width=4).grid(column=1, row=2, columnspan=1, sticky=E)
    tkinter.Label(f_all_thong_ke_tam_tru_tam_vang, font=font_content, text=data[0], bg="white",
                  height=1, width=4).grid(column=2, row=2, columnspan=1, sticky=W)

    tkinter.Label(f_all_thong_ke_tam_tru_tam_vang, font=font_content, text="", bg=TamVangColor,
                  height=1, width=4).grid(column=1, row=3, columnspan=1, sticky=E)
    tkinter.Label(f_all_thong_ke_tam_tru_tam_vang, font=font_content, text=data[1], bg="white",
                  height=1, width=4).grid(column=2, row=3, columnspan=1, sticky=W)
    label = ["Tạm trú", "Tạm vắng"]
    f = Figure()  # create a figure object
    ax = f.add_subplot(111)  # add an Axes to the figure
    ax.pie(data, radius=1, labels=label, colors=[TamTruColor, TamVangColor],
           autopct='%0.2f%%', shadow=True)

    chart1 = FigureCanvasTkAgg(f, master=f_all_thong_ke_tam_tru_tam_vang)
    chart1.get_tk_widget().grid(column=0, row=4, columnspan=4, sticky='news')


'''Kiến nghị'''


def KienNghi():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = selected_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_all_kien_nghi = tkinter.Frame(
        f_kien_nghi, highlightbackground="black", highlightthickness=2)
    f_kien_nghi.grid_columnconfigure(0, weight=1)
    f_kien_nghi.grid_rowconfigure(0, weight=1)
    f_all_kien_nghi.grid(column=0, row=0, sticky='news', padx=10, pady=10)

    tkinter.Label(f_all_kien_nghi, text="Kiến nghị", font=font_header1, justify=LEFT).grid(
        column=0, row=0, columnspan=1, padx=padx, pady=pady, sticky=W)

    tkinter.Label(
        f_all_kien_nghi, text="Chọn yêu cầu của bạn: ", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Tạo kiến nghị", "Xem kiến nghị", "Kiến nghị đã xử lý")
    chosed = StringVar(f_all_kien_nghi)
    dropDownKienNghi = ttk.OptionMenu(
        f_all_kien_nghi, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownKienNghi['menu'].configure(font=('Arial', 12))
    dropDownKienNghi.grid(column=1, row=1, sticky=W,
                          padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_kien_nghi, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def submit(chose):
        if (chose == "Tạo kiến nghị"):
            switch(f_tao_kien_nghi)
        elif (chose == "Kiến nghị đã xử lý"):
            Data = ChucNang.GetTraLoiKienNghi()
            XemKienNghi(Data, False)

        elif (chose == "Xem kiến nghị"):
            TrangThai = "Chưa xử lý"
            if (ID == 2):
                TrangThai = "Chưa xử lý"
            elif (ID == 1):
                TrangThai = "Mới ghi nhận"
            errorCode, Data = ChucNang.XemToanBoKienNghiTheoTrangThai(
                TrangThai)

            XemKienNghi(Data, True)

# HoTen, CCCD, NoiDung, NgayKN: datetime.datetime, PhanLoai


def TaoKienNghi():
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = selected_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg
    f_all_tao_kien_nghi = tkinter.Frame(
        f_tao_kien_nghi, highlightbackground="black", highlightthickness=2)
    f_tao_kien_nghi.grid_columnconfigure(0, weight=1)
    f_tao_kien_nghi.grid_rowconfigure(0, weight=1)
    f_all_tao_kien_nghi.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_tao_kien_nghi.grid_columnconfigure(0, weight=1)
    f_all_tao_kien_nghi.grid_columnconfigure(1, weight=1)
    f_all_tao_kien_nghi.grid_columnconfigure(2, weight=1)
    f_all_tao_kien_nghi.grid_columnconfigure(3, weight=1)
    # row 0
    tkinter.Label(f_all_tao_kien_nghi, text="Đơn kiến nghị", font=font_header1).grid(
        column=0, row=0, padx=padx, pady=pady, columnspan=4)
    tkinter.Label(f_all_tao_kien_nghi, text="Họ và tên:", font=font_content,
                  anchor=W, justify=LEFT).grid(column=0, row=1, columnspan=1, sticky=NW, padx=padx, pady=pady)
    hoVaTen = tkinter.Entry(f_all_tao_kien_nghi, font=font_content, width=60)
    hoVaTen.grid(column=1, row=1, columnspan=3,
                 sticky=NW, padx=padx, pady=pady)

    tkinter.Label(f_all_tao_kien_nghi, text="CCCD:", font=font_content,
                  anchor=W, justify=LEFT).grid(column=0, row=2, columnspan=1, sticky=NW, padx=padx, pady=pady)
    CCCD = tkinter.Entry(f_all_tao_kien_nghi, font=font_content, width=20)
    CCCD.grid(column=1, row=2, columnspan=1, sticky=NW, padx=padx, pady=pady)

    tkinter.Label(f_all_tao_kien_nghi, text="Nội dung:", font=font_content,
                  anchor=W, justify=LEFT).grid(column=0, row=3, columnspan=1, sticky=NW, padx=padx, pady=pady)
    noiDung = tkinter.Text(f_all_tao_kien_nghi,
                           font=font_content_mini, width=75, height=15, wrap=WORD)
    noiDung.grid(column=1, row=3, columnspan=3,
                 sticky=NW, padx=padx, pady=pady)

    tkinter.Label(f_all_tao_kien_nghi, text="Phân loại:", font=font_content,
                  anchor=W, justify=LEFT).grid(column=0, row=4, columnspan=1, sticky=NW, padx=padx, pady=pady)
    phanLoai = tkinter.Entry(f_all_tao_kien_nghi, font=font_content, width=60)
    phanLoai.grid(column=1, row=4, columnspan=3,
                  sticky=NW, padx=padx, pady=pady)

    ngayKN = DateEntry(f_all_tao_kien_nghi, font=font_content)

    tkinter.Button(f_all_tao_kien_nghi, text="Gửi", font=font_header3, fg="white", bg="blue",
                   cursor='hand2', command=lambda: submit()).grid(column=0, row=5, columnspan=4, padx=padx, pady=pady)

    errorMessage = tkinter.Label(
        f_all_tao_kien_nghi, text="", font=font_content, fg="red", justify=CENTER, anchor=N)
    errorMessage.grid(column=0, row=6, columnspan=4)

    def submit():
        if (hoVaTen.get() == "" or CCCD.get() == "" or noiDung.get(
                "1.0", 'end-1c') == "" or phanLoai.get() == ""):
            errorMessage['text'] = "Vui lòng điền đầy đủ thông tin!"
            return

        errorCode = ChucNang.TaoDonKienNghi(hoVaTen.get(), CCCD.get(), noiDung.get(
            "1.0", 'end-1c'), ngayKN.get_date().strftime("%m/%d/%y"), phanLoai.get())[0]

        if (errorCode == 1):
            errorMessage['text'] = "Vui lòng kiểm tra lại họ tên, CCCD!"
            return
        elif (errorCode == 0):
            messagebox.showinfo("", "Đã gửi đơn kiến nghị")
            switch(f_trang_chu)


# Data =[[CuDan, KienNghi]]

cnt = 0


def XemKienNghi(Data, tuongTac):
    global cnt
    for f in frames:
        for widget in f.winfo_children():
            widget.destroy()
    f_xem_kien_nghi.tkraise()
    global btn_trang_chu_bg, btn_ho_khau_bg, btn_kien_nghi_bg, btn_thong_ke_bg, btn_lich_su_bg
    btn_trang_chu_bg = win_bg
    btn_ho_khau_bg = win_bg
    btn_kien_nghi_bg = selected_bg
    btn_thong_ke_bg = win_bg
    btn_lich_su_bg = win_bg

    listVar = []
    listMaKienNghi = []
    listHoTen = []
    listCCCD = []
    cnt = 0

    f_all_xem_kien_nghi = tkinter.Frame(
        f_xem_kien_nghi, highlightbackground="black", highlightthickness=2)
    f_xem_kien_nghi.grid_columnconfigure(0, weight=1)
    f_xem_kien_nghi.grid_rowconfigure(0, weight=1)
    f_all_xem_kien_nghi.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_xem_kien_nghi.grid_columnconfigure(0, weight=2)
    f_all_xem_kien_nghi.grid_columnconfigure(1, weight=2)
    f_all_xem_kien_nghi.grid_columnconfigure(2, weight=5)
    f_all_xem_kien_nghi.grid_columnconfigure(3, weight=2)
    f_all_xem_kien_nghi.grid_columnconfigure(4, weight=2)
    f_all_xem_kien_nghi.grid_rowconfigure(0, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(1, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(2, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(3, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(4, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(5, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(6, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(7, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(8, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(9, weight=1)
    f_all_xem_kien_nghi.grid_rowconfigure(10, weight=1)

    # def view(CuDan, DanhSachKienNghi):
    #     for widget in f_all_xem_kien_nghi.winfo_children():
    #         widget.destroy()
    n = len(Data)
    times = ceil(n/8)

    def showPage(i):
        if (n == 0):

            tkinter.Label(f_all_xem_kien_nghi, text="Không có data", fg="red",
                          font=font_header1).grid(column=0, row=0, columnspan=5)
        else:
            # Không cho đi về trước nhân khẩu đầu tiên
            if (i <= 0):
                i = 0
            # Không cho đi quá nhân khẩu cuối
            elif (i >= times-1):
                i = times-1
            # Xóa dữ liệu cũ
            for widget in f_all_xem_kien_nghi.winfo_children():
                widget.destroy()
            # Hiện thông tin nhân khẩu thứ i
            KienNghiInfo(i)

# 'MaKienNghi', 'ID', 'CCCD', 'NoiDung', 'NgayKN', 'PhanLoai', 'TrangThai'

    def KienNghiInfo(i):
        # Header
        if (tuongTac):
            tkinter.Label(f_all_xem_kien_nghi, text="Họ và tên", font=font_content,
                          anchor=W, justify=LEFT).grid(column=0, row=0, columnspan=1, sticky=W)
            tkinter.Label(f_all_xem_kien_nghi, text="CCCD", font=font_content,
                          anchor=W, justify=LEFT).grid(column=1, row=0, columnspan=1, sticky=W)
            tkinter.Label(f_all_xem_kien_nghi, text="Nội Dung", font=font_content,
                          anchor=W, justify=LEFT).grid(column=2, row=0, columnspan=1, sticky=W)
            tkinter.Label(f_all_xem_kien_nghi, text="Trạng thái", font=font_content,
                          anchor=W, justify=LEFT).grid(column=3, row=0, columnspan=1, sticky=W)
            if (ID == 2):
                tkinter.Label(f_all_xem_kien_nghi, text="Trả lời", font=font_content,
                              anchor=W, justify=LEFT).grid(column=4, row=0, columnspan=1, sticky=W)
            if (ID == 1):
                tkinter.Label(f_all_xem_kien_nghi, text="Chọn để gộp", font=font_content,
                              anchor=W, justify=LEFT).grid(column=4, row=0, columnspan=1, sticky=W)
        else:
            tkinter.Label(f_all_xem_kien_nghi, text="Họ và tên", font=font_content,
                          anchor=W, justify=LEFT).grid(column=0, row=0, columnspan=1, sticky=W)
            tkinter.Label(f_all_xem_kien_nghi, text="CCCD", font=font_content,
                          anchor=W, justify=LEFT).grid(column=1, row=0, columnspan=1, sticky=W)
            tkinter.Label(f_all_xem_kien_nghi, text="Nội Dung", font=font_content,
                          anchor=W, justify=LEFT).grid(column=2, row=0, columnspan=1, sticky=W)
            tkinter.Label(f_all_xem_kien_nghi, text="Nội dung trả lời", font=font_content,
                          anchor=W, justify=LEFT).grid(column=3, row=0, columnspan=1, sticky=W)
            tkinter.Label(f_all_xem_kien_nghi, text="Đã thông báo", font=font_content,
                          anchor=W, justify=LEFT).grid(column=4, row=0, columnspan=1, sticky=W)
        # Body
        for j in range(8):
            if (i*8 + j >= n):
                break
            if (tuongTac):
                tkinter.Label(f_all_xem_kien_nghi, text=Data[i*8+j][0].HoTen.replace(",", "\n"), font=font_content_mini,
                              anchor=W, justify=LEFT, wraplength=140).grid(column=0, row=j+1, columnspan=1, sticky=NW)
                tkinter.Label(f_all_xem_kien_nghi, text=Data[i*8+j][0].CCCD.replace(",", "\n"), font=font_content_mini,
                              anchor=W, justify=LEFT, wraplength=140).grid(column=1, row=j+1, columnspan=1, sticky=NW)
                tkinter.Label(f_all_xem_kien_nghi, text=Data[i*8 + j][1].NoiDung,
                              font=font_content_mini, anchor=W, justify=LEFT, wraplength=350).grid(column=2, row=j+1, columnspan=1, sticky=NW)
                tkinter.Label(f_all_xem_kien_nghi, text=Data[i*8 + j][1].TrangThai, font=font_content_mini,
                              anchor=W, justify=LEFT, wraplength=140).grid(column=3, row=j+1, columnspan=1, sticky=NW)
                if ID == 2:
                    tkinter.Button(f_all_xem_kien_nghi, text="Trả lời", fg="white", bg="blue", cursor='hand2',
                                   font=font_content_mini, command=lambda data=i*8 + j: TraLoiKienNghi(Data, data, tuongTac)).grid(column=4, row=j+1, columnspan=1, sticky=NW)
                elif ID == 1:
                    listVar.append(IntVar())
                    tkinter.Checkbutton(f_all_xem_kien_nghi, text="",
                                        font=font_content, cursor='hand2', variable=listVar[i*8+j], onvalue=1, offvalue=0, command=lambda data=i*8+j: choseMerge(data)).grid(column=4, row=j+1, columnspan=1, sticky=NW)
            else:
                tkinter.Label(f_all_xem_kien_nghi, text=Data[i*8+j][0].HoTen.replace(",", "\n"), font=font_content_mini,
                              anchor=W, justify=LEFT, wraplength=140).grid(column=0, row=j+1, columnspan=1, sticky=NW)
                tkinter.Label(f_all_xem_kien_nghi, text=Data[i*8+j][0].CCCD.replace(",", "\n"), font=font_content_mini,
                              anchor=W, justify=LEFT, wraplength=140).grid(column=1, row=j+1, columnspan=1, sticky=NW)
                tkinter.Label(f_all_xem_kien_nghi, text=Data[i*8 + j][1].NoiDung,
                              font=font_content_mini, anchor=W, justify=LEFT, wraplength=350).grid(column=2, row=j+1, columnspan=1, sticky=NW)
                tkinter.Label(f_all_xem_kien_nghi, text=Data[i*8 + j][2].NoiDung, font=font_content_mini,
                              anchor=W, justify=LEFT, wraplength=140).grid(column=3, row=j+1, columnspan=1, sticky=NW)
                listVar.append(IntVar())
                tkinter.Checkbutton(f_all_xem_kien_nghi, text="",
                                    font=font_content, cursor='hand2', variable=listVar[i*8+j], onvalue=1, offvalue=0, command=lambda data=i*8+j: changeStatus(data)).grid(column=4, row=j+1, columnspan=1, sticky=NW)
        if (i != 0):
            tkinter.Button(
                f_all_xem_kien_nghi, text="Trang trước",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i-1)).grid(column=0, row=9, sticky=W, padx=padx, pady=pady, columnspan=1)
        if (i != times-1):
            tkinter.Button(
                f_all_xem_kien_nghi, text="Trang sau",  font=font_header3+" bold", fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPage(i+1)).grid(column=4, row=9, sticky=E, padx=padx, pady=pady, columnspan=1)
        btn = tkinter.Button(f_all_xem_kien_nghi, text="",
                             justify=CENTER, anchor=N, font=font_content, bg="blue", fg="white", cursor='hand2', command=lambda: submit())
        btn.grid(column=0, row=10, columnspan=5, sticky=N)

        def choseMerge(index):
            global cnt
            if (listVar[index].get() == 1):
                cnt += 1
                listMaKienNghi.append(Data[index][1].MaKienNghi)
                listHoTen.append(Data[index][0].HoTen)
                listCCCD.append(Data[index][0].CCCD)
            else:
                try:
                    ite = listMaKienNghi.index(Data[index][1].MaKienNghi)
                    listMaKienNghi.pop(ite)
                    listHoTen.pop(ite)
                    listCCCD.pop(ite)
                    cnt -= 1
                except:
                    pass
            if (cnt >= 2):
                btn["text"] = "Gộp"
            else:
                btn["text"] = "Gửi"

        if (tuongTac == False or ID == 2):
            btn['text'] = "OK"
        else:
            btn['text'] = 'Gửi'

        def changeStatus(data):
            pass

        def submit():
            # Xem kiến nghị cần trả lời or gửi lên cấp trên
            if (tuongTac):
                global cnt
                if ((tuongTac == False) or ID == 2):
                    switch(f_trang_chu)
                elif (ID == 1):
                    if (cnt >= 2):
                        ChucNang.GopKienNghi(
                            listMaKienNghi, listHoTen, listCCCD)
                        errorCode, Data1 = ChucNang.XemToanBoKienNghiTheoTrangThai(
                            "Mới ghi nhận")
                        messagebox.showinfo("", "Đã gộp")
                        XemKienNghi(Data1, True)
                    else:
                        for i in Data:
                            ChucNang.ThayDoiTrangThai(
                                i[1].MaKienNghi, "Chưa xử lý")
                        switch(f_trang_chu)
            # Xem kiến nghị đã được trả lời
            else:
                for i in range(n):
                    # đã thông báo và người dân lên làm việc
                    if (listVar[i].get()):
                        ChucNang.ThayDoiTrangThai(
                            Data[i][1].MaKienNghi, "Đã thông báo")
                switch(f_trang_chu)

    showPage(0)


def TraLoiKienNghi(Data, index, tuongTac):
    f_tra_loi_kien_nghi.tkraise()

    f_all_tra_loi_kien_nghi = tkinter.Frame(
        f_tra_loi_kien_nghi, highlightbackground="black", highlightthickness=2)

    f_tra_loi_kien_nghi.grid_columnconfigure(0, weight=1)
    f_tra_loi_kien_nghi.grid_rowconfigure(0, weight=1)
    f_all_tra_loi_kien_nghi.grid(
        column=0, row=0, sticky='news', padx=10, pady=10)

    f_all_tra_loi_kien_nghi.grid_columnconfigure(0, weight=2)
    f_all_tra_loi_kien_nghi.grid_columnconfigure(1, weight=2)
    f_all_tra_loi_kien_nghi.grid_columnconfigure(2, weight=4)
    f_all_tra_loi_kien_nghi.grid_rowconfigure(0, weight=10)
    f_all_tra_loi_kien_nghi.grid_rowconfigure(1, weight=10)
    f_all_tra_loi_kien_nghi.grid_rowconfigure(2, weight=10)
    f_all_tra_loi_kien_nghi.grid_rowconfigure(3, weight=50)
    f_all_tra_loi_kien_nghi.grid_rowconfigure(4, weight=1)
    f_all_tra_loi_kien_nghi.grid_rowconfigure(5, weight=50)
    f_all_tra_loi_kien_nghi.grid_rowconfigure(6, weight=10)
    f_all_tra_loi_kien_nghi.grid_rowconfigure(7, weight=10)

    tkinter.Button(f_all_tra_loi_kien_nghi, text="trở lại", font=font_content, fg="white", bg="blue", cursor='hand2',
                   command=lambda: GoBack()).grid(column=0, row=0, columnspan=2, sticky=NW)
    tkinter.Label(f_all_tra_loi_kien_nghi, text="Họ và tên: " +
                  Data[index][0].HoTen, font=font_content, anchor=NW, justify=LEFT).grid(column=0, row=1, columnspan=2, sticky=NW)
    tkinter.Label(f_all_tra_loi_kien_nghi, text="CCCD: " +
                  Data[index][0].CCCD, font=font_content, anchor=NW, justify=LEFT).grid(column=2, row=1, columnspan=1, sticky=NW)
    tkinter.Label(f_all_tra_loi_kien_nghi, text="Mã kiến nghị: " +
                  str(Data[index][1].MaKienNghi), font=font_content, anchor=NW, justify=LEFT).grid(column=0, row=2, columnspan=2, sticky=NW)
    tkinter.Label(f_all_tra_loi_kien_nghi, text="Nội dung: " +
                  Data[index][1].NoiDung, wraplength=600, font=font_content, anchor=NW, justify=LEFT).grid(column=0, row=3, columnspan=3, sticky=NW)
    tkinter.Label(f_all_tra_loi_kien_nghi, text="Ngày kiến nghị: " +
                  (Data[index][1].NgayKN).strftime("%m/%d/%y"), font=font_content, anchor=NW, justify=LEFT).grid(column=0, row=4, columnspan=3, sticky=NW)

    ttk.Separator(f_all_tra_loi_kien_nghi, orient=HORIZONTAL).grid(
        column=0, row=5, columnspan=3, sticky=EW)

    tkinter.Label(f_all_tra_loi_kien_nghi, text="Trả lời: ", font=font_content,
                  anchor=W, justify=LEFT). grid(column=0, row=6, columnspan=1, sticky=NW)
    traLoi = tkinter.Text(f_all_tra_loi_kien_nghi,
                          font=font_content_mini, height=15, width=100, wrap=WORD)
    traLoi.grid(column=1, row=6, columnspan=2, sticky=NW)
    tkinter.Button(f_all_tra_loi_kien_nghi, text="Gửi", font=font_content, cursor='hand2',
                   fg="white", bg="blue", command=lambda: submit()).grid(column=0, row=7, columnspan=3, sticky=N)

    errMessage = tkinter.Label(
        f_all_tra_loi_kien_nghi, text="", font=font_content, fg="red", justify=CENTER)
    errMessage.grid(column=0, row=8, columnspan=3)

    def GoBack():
        f_xem_kien_nghi.tkraise()
        for f in f_tra_loi_kien_nghi.winfo_children():
            f.destroy()

    def submit():
        content = traLoi.get("1.0", 'end-1c')
        if (content == ""):
            errMessage['text'] = "Chưa có nội dung trả lời!"
        else:
            ChucNang.TraLoiKienNghi(Data[index][1].MaKienNghi, content)
            Data.pop(index)
            messagebox.showinfo("", "Đã trả lời!")
            XemKienNghi(Data, tuongTac)


"""----------------------------------------------------------------------------------------------"""


def LogIn():
    f_log_in = tkinter.Frame(root, bg="white", padx=150, pady=30)
    f_log_in.place(relx=0, rely=0, relheight=1, relwidth=1,
                   anchor=NW)
    f_log_in.tkraise()
    f_log_in.grid_columnconfigure(0, weight=1)
    f_log_in.grid_columnconfigure(1, weight=1)

    f_log_in.grid_rowconfigure(0, weight=30)
    f_log_in.grid_rowconfigure(1, weight=1)
    f_log_in.grid_rowconfigure(2, weight=20)
    f_log_in.grid_rowconfigure(3, weight=10)
    f_log_in.grid_rowconfigure(4, weight=10)
    f_log_in.grid_rowconfigure(5, weight=20)
    f_log_in.grid_rowconfigure(6, weight=1)
    f_log_in.grid_rowconfigure(7, weight=50)

    tkinter.Label(f_log_in, text="", bg="white", image=logoLogin, anchor=E).grid(
        column=0, row=0, columnspan=1, padx=15, pady=5, sticky=SE)
    tkinter.Label(f_log_in, text="Quản lý", font="Quicksand 25 bold",
                  fg='red', bg="white", justify=LEFT, anchor=W).grid(column=1, row=0, columnspan=1, padx=15, pady=25, sticky=SW)

    # horizontal separator
    ttk.Separator(f_log_in, orient=HORIZONTAL).grid(
        column=0, row=1, columnspan=2, sticky=EW)

    tkinter.Label(f_log_in, text="Nhập thông tin tài khoản", font=font_header2, bg="white", anchor=W, justify=LEFT).grid(
        column=0, row=2, columnspan=2, padx=180, pady=5, sticky=SW)
    userName = tkinter.Entry(f_log_in, font=font_content, bg="white", width=60)
    userName.insert(0, 'username')
    userName.bind("<FocusIn>", lambda args: userName.delete('0', 'end'))
    userName.grid(
        column=0, row=3, columnspan=2, padx=180, pady=5, sticky=NW)

    password = tkinter.Entry(f_log_in, font=font_content, bg="white", width=60)
    password.insert(0, 'password')
    password.bind("<FocusIn>", lambda args: password.delete('0', 'end'))
    password.grid(
        column=0, row=4, columnspan=2, padx=180, pady=5, sticky=NW)
    tkinter.Button(f_log_in, text="Đăng nhập", font=font_header2, bg="blue", fg="white", cursor='hand2',
                   command=lambda: submit(userName.get(), password.get())).grid(row=5, column=0, columnspan=2, padx=180, sticky=NW)
    ttk.Separator(f_log_in, orient=HORIZONTAL).grid(
        column=0, row=6, columnspan=2, sticky=EW)

    errorMessage = tkinter.Label(
        f_log_in, text="", font=font_header2, fg="red", bg="white", justify=CENTER)
    errorMessage.grid(column=0, row=7, columnspan=2)

    def submit(tendangnhap, matkhau):
        global ID
        ID = ChucNang.DangNhap(tendangnhap, matkhau)
        if (ID == 0):
            errorMessage["text"] = "Thông tin đăng nhập không đúng"

        else:
            switch(frame=f_trang_chu)
            f_log_in.destroy()


LogIn()
# switch(f_trang_chu)
root.mainloop()
