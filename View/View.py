import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import config.config as config
import tkinter
import os
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
import ChucNang

dirname = os.path.dirname(__file__)
win_bg = config.win_bg
btn_home_bg = win_bg
btn_family_bg = win_bg
btn_demand_bg = win_bg

padx = 10
pady = 7

font_header1 = "Arial 20 bold"
font_header2 = "Arial 16 bold"
font_header3 = "Arial 14 bold"
font_content = "Arial 12 bold"


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
logoIconLogin = Image.open(pathLogoLogin)
logoLogin = logoIconLogin.resize(
    (100, 100), Image.ANTIALIAS)
logoLogin = ImageTk.PhotoImage(logoLogin)
# Nav Bar
pathLogo = os.path.join(
    dirname, 'config\\image\\icon_homepage.png')
logoIcon = Image.open(pathLogo)
logo = logoIcon.resize(
    (60, 60), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
# ---------------
pathNavHomePageIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_home.png')
navHomePageImage = Image.open(pathNavHomePageIcon)
navHomePageImage = navHomePageImage.resize(
    (30, 30), Image.ANTIALIAS)
navHomePageImage = ImageTk.PhotoImage(navHomePageImage)
# -------------------------
pathNavFamilyIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_family.png')
navFamilyImage = Image.open(pathNavFamilyIcon)
navFamilyImage = navFamilyImage.resize(
    (30, 30), Image.ANTIALIAS)
navFamilyImage = ImageTk.PhotoImage(navFamilyImage)
# -------------------------
pathNavDemandIcon = os.path.join(
    dirname, 'config\\image\\icon_nav_demand.png')
navDemandImage = Image.open(pathNavDemandIcon)
navDemandImage = navDemandImage.resize(
    (30, 30), Image.ANTIALIAS)
navDemandImage = ImageTk.PhotoImage(navDemandImage)
# -------------------------
pathHelpIcon = os.path.join(
    dirname, 'config\\image\\icon_help.png')
helpImage = Image.open(pathHelpIcon)
helpImage = helpImage.resize(
    (30, 30), Image.ANTIALIAS)
helpImage = ImageTk.PhotoImage(helpImage)
# ------------------------
pathSettingIcon = os.path.join(
    dirname, 'config\\image\\icon_setting.png')
settingImage = Image.open(pathSettingIcon)
settingImage = settingImage.resize(
    (30, 30), Image.ANTIALIAS)
settingImage = ImageTk.PhotoImage(settingImage)

'''HOME'''
# -- load icon schedule
pathSchedule = os.path.join(
    dirname, 'config\\image\\icon_schedule.png')
scheduleImage = Image.open(pathSchedule)
scheduleImage = scheduleImage.resize(
    (16, 16), Image.ANTIALIAS)
scheduleImage = ImageTk.PhotoImage(scheduleImage)
# ------------------------
# changePerson
pathChangePerson = os.path.join(
    dirname, 'config\\image\\change_person_button.png')
changePersonImage = Image.open(pathChangePerson)
changePersonImage = changePersonImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
changePersonImage = ImageTk.PhotoImage(changePersonImage)
# -------------------------
# viewMyInfo
pathViewMyInfo = os.path.join(
    dirname, 'config\\image\\view_my_info_button.png')
viewMyInfoImage = Image.open(pathViewMyInfo)
viewMyInfoImage = viewMyInfoImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
viewMyInfoImage = ImageTk.PhotoImage(viewMyInfoImage)
# ------------------------
# tách khẩu
pathTachKhau = os.path.join(
    dirname, 'config\\image\\tach_khau_button.png')
tachKhauImage = Image.open(pathTachKhau)
tachKhauImage = tachKhauImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tachKhauImage = ImageTk.PhotoImage(tachKhauImage)
# ------------------------
# tạm trú
pathTamTru = os.path.join(
    dirname, 'config\\image\\tam_tru_button.png')
tamTruImage = Image.open(pathTamTru)
tamTruImage = tamTruImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tamTruImage = ImageTk.PhotoImage(tamTruImage)
# ------------------------
# tạm vắng
pathTamVang = os.path.join(
    dirname, 'config\\image\\tam_vang_button.png')
tamVangImage = Image.open(pathTamVang)
tamVangImage = tamVangImage.resize(
    (config.button_w, config.button_h), Image.ANTIALIAS)
tamVangImage = ImageTk.PhotoImage(tamVangImage)
# ---------------------

# Config style cho drop down menu
someStyle = ttk.Style()
someStyle.configure('DropDownStyle.TMenubutton',
                    font=('Arial', 12, "bold"))


def switch(frame, data=[], maHoKhau="", hoKhau=(), listCuDan=[], maQuanLy=1):
    def destroy_all_frame():
        for f in frames:
            for widget in f.winfo_children():
                widget.destroy()
    global btn_home_bg, btn_family_bg, btn_demand_bg
    # home
    if (frame == f_home):
        destroy_all_frame()
        btn_home_bg = config.selected_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        Home()
    # xem hộ khẩu
    elif (frame == f_authen_family):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = config.selected_bg
        btn_demand_bg = win_bg
        ViewAuthenFamily()
    elif (frame == f_family):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = config.selected_bg
        btn_demand_bg = win_bg
        ViewFamily(hoKhau, listCuDan)
    # thêm nhân khẩu mới
    elif (frame == f_add_person):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AddPerson()
    # thay đổi nhân khẩu
    elif (frame == f_authen_change):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        ViewAuthenChange()
    elif (frame == f_change_person):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        ChangePerson()
    # thay đổi chủ hộ
    elif (frame == f_authen_change_host_person):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        ViewAuthenChangeHostPerson()
    elif (frame == f_change_host_person):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        ChangeHostPerson(maHoKhau=maHoKhau, hoKhau=hoKhau, listCuDan=listCuDan)
    elif (frame == f_authen_tach_khau):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        ViewAuthenTachKhau()
    elif (frame == f_tach_khau):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        TachKhau(maHoKhau=maHoKhau, hoKhau=hoKhau, listCuDan=listCuDan)
    elif (frame == f_tam_tru):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        TamTru()
    elif (frame == f_tao_giay_tam_tru):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        TaoGiayTamTru()
    elif (frame == f_authen_xem_giay_tam_tru):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AuthenXemGiayTamTru()
    elif (frame == f_xem_giay_tam_tru):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        XemGiayTamTru(thongTinGiayTamTru=data)
    elif (frame == f_tam_vang):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        TamVang()
    elif (frame == f_tao_giay_tam_vang):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        TaoGiayTamVang()
    elif (frame == f_authen_xem_giay_tam_vang):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AuthenXemGiayTamVang()
    elif (frame == f_xem_giay_tam_vang):
        destroy_all_frame()

        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        XemGiayTamVang(thongTinGiayTamVang=data)
    Nav()
    frame.tkraise()


# Tạo các frame sẵn để nâng lên khi cần xuất hiện

f_home = tkinter.Frame(root)

f_authen_family = tkinter.Frame(root)
f_family = tkinter.Frame(root)

f_add_person = tkinter.Frame(root)

f_authen_change = tkinter.Frame(root)
f_change_person = tkinter.Frame(root)

f_authen_change_host_person = tkinter.Frame(root)
f_change_host_person = tkinter.Frame(root)

f_authen_tach_khau = tkinter.Frame(root)
f_tach_khau = tkinter.Frame(root)

f_tam_tru = tkinter.Frame(root)
f_tao_giay_tam_tru = tkinter.Frame(root)
f_authen_xem_giay_tam_tru = tkinter.Frame(root)
f_xem_giay_tam_tru = tkinter.Frame(root)

f_tam_vang = tkinter.Frame(root)
f_tao_giay_tam_vang = tkinter.Frame(root)
f_authen_xem_giay_tam_vang = tkinter.Frame(root)
f_xem_giay_tam_vang = tkinter.Frame(root)
# set các frame chồng lên nhau.
frames = (f_home, f_authen_family, f_family, f_add_person, f_authen_change, f_change_person,  f_authen_change_host_person,
          f_change_host_person, f_authen_tach_khau, f_tach_khau, f_tam_tru, f_tao_giay_tam_tru, f_authen_xem_giay_tam_tru, f_xem_giay_tam_tru, f_tam_vang, f_tao_giay_tam_vang, f_authen_xem_giay_tam_vang, f_xem_giay_tam_vang)
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
    labelLogoApp = tkinter.Label(topFrameNav, image=logo,
                                 anchor=CENTER, bg=win_bg, padx=5)
    labelLogoApp.place(relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    # 1.2 App name
    labelAppName = tkinter.Label(
        topFrameNav, text="Quản lý", font=font_header1, anchor=W, bg=win_bg, padx=5)
    labelAppName.place(relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
    # ------------------------
    # 2.Middle
    middleFrameNav = tkinter.Frame(nav_bar, bg=win_bg, pady=20)
    middleFrameNav.place(relx=0, rely=0.15, relheight=0.6,
                         relwidth=1, anchor=NW)
    # 2.1 Home Butotn
    homeFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_home_bg, padx=5, pady=0)
    homeFrame_middle_nav.place(
        relx=0, rely=0, relheight=0.1, relwidth=1, anchor=NW)

    labelIcon_home = tkinter.Label(homeFrame_middle_nav, image=navHomePageImage, bg=btn_home_bg,
                                   anchor=E, padx=5)
    labelIcon_home.place(relx=0, rely=0, relheight=1,
                         relwidth=0.3, anchor=NW)
    labelText_home = tkinter.Button(
        homeFrame_middle_nav, text="Trang chủ", font=font_header3, anchor=W, bg=btn_home_bg, borderwidth=0, cursor="hand2", command=lambda: switch(f_home))
    labelText_home.place(relx=1, rely=0, relheight=1,
                         relwidth=0.7, anchor=NE)

    # 2.2 Family Button

    familyFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_family_bg, padx=5, pady=0)
    familyFrame_middle_nav.place(
        relx=0, rely=0.1, relheight=0.1, relwidth=1, anchor=NW)

    labelIcon_family = tkinter.Label(familyFrame_middle_nav, image=navFamilyImage, bg=btn_family_bg,
                                     anchor=E, padx=5)
    labelIcon_family.place(
        relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    labelText_family = tkinter.Button(
        familyFrame_middle_nav, text="Family", font=font_header3, anchor=W, bg=btn_family_bg, borderwidth=0, cursor="hand2", command=lambda: switch(f_authen_family))
    labelText_family.place(
        relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
    # 2.3 Demand Button

    demandFrame_middle_nav = tkinter.Frame(
        middleFrameNav, bg=btn_demand_bg, padx=5, pady=0)
    demandFrame_middle_nav.place(
        relx=0, rely=0.2, relheight=0.1, relwidth=1, anchor=NW)

    labelIcon_demand = tkinter.Label(demandFrame_middle_nav, image=navDemandImage, bg=btn_demand_bg,
                                     anchor=E, padx=5)
    labelIcon_demand.place(
        relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    labelText_demand = tkinter.Button(
        demandFrame_middle_nav, text="Kiến Nghị", font=font_header3, anchor=W, bg=btn_demand_bg, borderwidth=0, cursor="hand2", command="")
    labelText_demand.place(
        relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)
    # 3. Button
    bottomFrame_nav = tkinter.Frame(nav_bar, bg=win_bg, padx=10, pady=20)
    bottomFrame_nav.place(relx=0, rely=1, relheight=0.25,
                          relwidth=1, anchor=SW)
    # 3.1 Support
    helpFrame_bottom_nav = tkinter.Frame(
        bottomFrame_nav, bg=win_bg, padx=5, pady=0)
    helpFrame_bottom_nav.place(
        relx=0, rely=0, relheight=0.3, relwidth=1, anchor=NW)

    labelIcon_help = tkinter.Label(helpFrame_bottom_nav, text="", image=helpImage, bg=win_bg,
                                   anchor=E, padx=5)
    labelIcon_help.place(relx=0, rely=0, relheight=1,
                         relwidth=0.3, anchor=NW)
    labelText_help = tkinter.Button(
        helpFrame_bottom_nav, text="Help", font=font_header3, anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command="")
    labelText_help.place(relx=1, rely=0, relheight=1,
                         relwidth=0.7, anchor=NE)
    # 3.2 Setting
    settingFrame_bottom_nav = tkinter.Frame(
        bottomFrame_nav, bg=win_bg, padx=5, pady=0)
    settingFrame_bottom_nav.place(
        relx=0, rely=0.3, relheight=0.3, relwidth=1, anchor=NW)

    labelIcon_setting = tkinter.Label(settingFrame_bottom_nav, image=settingImage, bg=win_bg,
                                      anchor=E, padx=5)
    labelIcon_setting.place(
        relx=0, rely=0, relheight=1, relwidth=0.3, anchor=NW)
    labelText_setting = tkinter.Button(
        settingFrame_bottom_nav, text="Đăng xuất", font=font_header3, anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command=lambda: LogIn())
    labelText_setting.place(
        relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)


'''End Nav Bar'''
# ---------------------------------------------------------------------------------------------------------------------------------
"""Start Home"""

# HomeView


def Home():
    # Create a child frame to destroy when no use parent frame
    f_all_home = tkinter.Frame(f_home)
    f_home.grid_columnconfigure(0, weight=1)
    f_home.grid_rowconfigure(0, weight=1)
    f_all_home.grid(column=0, row=0, sticky='news')

    topFrame_home = tkinter.Frame(f_all_home, bg=win_bg, pady=20, padx=5)
    topFrame_home.place(
        relx=0, rely=0, relheight=0.15, relwidth=1, anchor=NW)
    tkinter.Label(topFrame_home, text="Trang chủ", font=font_header1, bg=win_bg,
                  justify=LEFT, anchor=CENTER).grid(column=0, row=0, sticky=W)
    tkinter.Label(topFrame_home, text="", image=scheduleImage, bg=win_bg,
                  justify=LEFT, anchor=E).grid(column=1, row=0, sticky=W)
    tkinter.Label(topFrame_home, text=config.currentDate, font="Arial 10", bg=win_bg,
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
    labelText_request = tkinter.Label(
        requestFrame_bottom_home, text="Gửi yêu cầu", font=font_header2, anchor=W, padx=20, pady=10, bg=win_bg)
    labelText_request.place(relx=0, rely=0, relwidth=1, anchor=NW)
    # ---------------------------------------
    # thay đổi nhân khẩu
    buttonChangePerson = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=changePersonImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_authen_change))
    buttonChangePerson.place(
        relx=0.1, rely=0.1, relwidth=0.8, relheight=0.07, anchor=NW)
    # -------------------------------------------
    # tách khẩu
    buttonTachKhau = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tachKhauImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_authen_tach_khau))
    buttonTachKhau.place(
        relx=0.1, rely=0.18, relwidth=0.8, relheight=0.07, anchor=NW)
    # ---------------------------------------------
    # tạm trú
    buttonTamTru = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tamTruImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_tam_tru))
    buttonTamTru.place(
        relx=0.1, rely=0.26, relwidth=0.8, relheight=0.07, anchor=NW)
    # ------------------------------------------------
    # tạm vắng
    buttonTamVang = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tamVangImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_tam_vang))
    buttonTamVang.place(
        relx=0.1, rely=0.34, relwidth=0.8, relheight=0.07, anchor=NW)

    # ------------------------------------------------

    # RESPONSE
    responseFrame_bottom_home = tkinter.Frame(
        bottomFrame_home, bg=win_bg)
    responseFrame_bottom_home.place(
        relx=1, rely=0, relheight=1, relwidth=0.5, anchor=NE)

    # label
    labelText_request = tkinter.Label(
        responseFrame_bottom_home, text="Phản hồi kiến nghị", font="Arial 16 bold", anchor=W, padx=20, pady=10, bg=win_bg)
    labelText_request.place(relx=0, rely=0, relwidth=1, anchor=NW)

    # subFrame kiến nghị
    response_demand_frame = tkinter.Frame(
        responseFrame_bottom_home, bg=config.response_demand_bg, borderwidth=1)
    response_demand_frame.place(
        relx=0.05, rely=0.1, relheight=0.85, relwidth=0.9, anchor=NW)

    for i in range(0, len(config.list_kien_nghi)):
        tkinter.Label(response_demand_frame,
                      text=config.list_kien_nghi[i][0], font="Arial 14 bold", fg="black", wraplength=300, bg=config.response_demand_bg, anchor=W, justify=LEFT).grid(column=0, row=3*i+0, padx=5, pady=5, sticky=W)
        tkinter.Label(response_demand_frame,
                      text=config.list_kien_nghi[i][1], font="Arial 12", fg="black", wraplength=300, bg=config.response_demand_bg, anchor=W, justify=LEFT).grid(column=0, row=3*i+1, padx=5, pady=5, sticky=W)

        ttk.Separator(response_demand_frame, orient=HORIZONTAL).grid(
            column=0, row=3*i+2, ipadx=500, pady=5)


'''Biến đổi nhân khẩu'''
# xác nhận loại biến đổi (thêm người, thay đổi nhân khẩu, thay đổi chủ hộ)


def ViewAuthenChange():
    # Create a child frame to destroy when no use parent frame
    f_all_authen_change = tkinter.Frame(f_authen_change)
    f_authen_change.grid_columnconfigure(0, weight=1)
    f_authen_change.grid_rowconfigure(0, weight=1)
    f_all_authen_change.grid(column=0, row=0, sticky='news')
    f_all_authen_change.config(padx=10, pady=30)

    tkinter.Label(
        f_all_authen_change, text="Chọn loại biến đổi: ", font=font_content, anchor=W).grid(column=0, row=0, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Thêm nhân khẩu mới", "Thay đổi nhân khẩu", "Thay đổi chủ hộ")
    chosed = StringVar(f_all_authen_change)
    dropDownGender = ttk.OptionMenu(
        f_all_authen_change, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownGender['menu'].configure(font=('Arial', 12))
    dropDownGender.grid(column=1, row=0, sticky=W,
                        padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_authen_change, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: Authen(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def Authen(chose):
        if (chose == "Thêm nhân khẩu mới"):
            switch(f_add_person)
        elif (chose == "Thay đổi nhân khẩu"):
            switch(f_change_person)
        elif (chose == "Thay đổi chủ hộ"):
            switch(f_authen_change_host_person)


# CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ


def AddPerson():
    # Create a child frame to destroy when no use parent frame
    f_all_add_person = tkinter.Frame(
        f_add_person, highlightbackground="black", highlightthickness=2)
    f_add_person.grid_columnconfigure(0, weight=1)
    f_add_person.grid_rowconfigure(0, weight=1)
    f_all_add_person.grid(column=0, row=0, sticky='news', padx=20, pady=20)

    f_all_add_person.grid_columnconfigure(0, weight=1)
    f_all_add_person.grid_columnconfigure(1, weight=1)
    f_all_add_person.grid_columnconfigure(2, weight=1)
    f_all_add_person.grid_columnconfigure(3, weight=1)

    # row 0
    tkinter.Label(
        f_all_add_person, text="Quan hệ với chủ hộ:", font=font_header3, anchor=W).grid(row=0, column=0, columnspan=2, padx=padx, pady=pady, sticky=W)
    quanHe = tkinter.Entry(f_all_add_person, font=font_content, width=40)
    quanHe.grid(row=0, column=2, padx=padx,
                pady=pady, sticky=W, columnspan=2)

    # row 1
    tkinter.Label(
        f_all_add_person, text="Họ và tên: ", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

    hoTen = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    hoTen.grid(column=1, row=1, padx=padx, pady=pady, columnspan=3)

    # row 2
    tkinter.Label(
        f_all_add_person, text="Bí danh(nếu có): ", font=font_content, anchor=W).grid(column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)

    biDanh = tkinter.Entry(
        f_all_add_person, font=font_content, width=20)
    biDanh.grid(column=1, row=2, padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_add_person, text="Nghề nghiệp: ", font=font_content, anchor=W).grid(column=2, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)

    ngheNghiep = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    ngheNghiep.grid(column=3, row=2, padx=padx, pady=pady, columnspan=1)

    # row 3
    tkinter.Label(
        f_all_add_person, text="Ngày sinh: ", font=font_content, anchor=W).grid(column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

    ngaySinh = DateEntry(f_all_add_person, font=font_content)
    ngaySinh.grid(column=1, row=3, sticky=W,
                  padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_add_person, text="Giới tính: ", font=font_content, anchor=W).grid(column=2, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Nam", "Nữ", "Khác")
    chosed = StringVar(f_all_add_person)

    dropDownGender = ttk.OptionMenu(
        f_all_add_person, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownGender['menu'].configure(font=('Arial', 12))
    dropDownGender.grid(column=3, row=3, sticky=W,
                        padx=padx, pady=pady, columnspan=1)

    # row 4
    tkinter.Label(
        f_all_add_person, text="Quê quán: ", font=font_content, anchor=W).grid(column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)

    queQuan = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    queQuan.grid(column=1, row=4, sticky=W,
                 padx=padx, pady=pady, columnspan=3)

    # row 5
    tkinter.Label(
        f_all_add_person, text="Số căn cước công dân:", anchor=W, font=font_content).grid(column=0, row=5, padx=padx, pady=pady, sticky=W, columnspan=1)

    CCCD = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    CCCD.grid(column=1, row=5, padx=padx,
              pady=pady, sticky=W, columnspan=1)

    tkinter.Label(
        f_all_add_person, text="Mã hộ khẩu: ", anchor=W, font=font_content).grid(column=2, row=5, padx=padx,
                                                                                 pady=pady, sticky=W, columnspan=1)

    maHoKhau = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    maHoKhau.grid(column=3, row=5, padx=padx,
                  pady=pady, sticky=W, columnspan=1)

    # row 6
    tkinter.Label(
        f_all_add_person, text="Dân tộc: ", font=font_content, anchor=W).grid(column=0, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)

    danToc = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    danToc.grid(column=1, row=6, sticky=W,
                padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_add_person, text="Quốc tịch: ", font=font_content, anchor=W).grid(column=2, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)
    quocTich = tkinter.Entry(
        f_all_add_person, font=font_content, width=20)
    quocTich.grid(column=3, row=6, sticky=W,
                  padx=padx, pady=pady, columnspan=1)

    # row 7
    tkinter.Label(
        f_all_add_person, text="Địa chỉ cũ:", font=font_content, anchor=W).grid(column=0, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)

    diaChiCu = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    diaChiCu.grid(
        column=1, row=7, padx=padx, pady=pady, columnspan=3)

    # row 8
    tkinter.Label(
        f_all_add_person, text="Ngày đăng ký thường trú: ", font=font_content, anchor=W).grid(column=0, row=8, sticky=W, padx=padx, pady=pady, columnspan=2)

    ngayDK = DateEntry(f_all_add_person, font=font_content)
    ngayDK.grid(column=2, row=8, sticky=W,
                padx=padx, pady=pady, columnspan=2)

    # row 10
    buttonSubmit = tkinter.Button(
        f_all_add_person, text="Gửi",  font=font_header3, fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: submit())
    buttonSubmit.grid(column=0, row=10, padx=padx, pady=pady, columnspan=4)

    def submit():
        # CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ
        ChucNang.ThemNhanKhauMoi(CCCD.get(),
                                 hoTen.get(),
                                 chosed.get(),
                                 ngaySinh.get_date().strftime("%m/%d/%y"),
                                 danToc.get(),
                                 quocTich.get(),
                                 ngheNghiep.get(),
                                 queQuan.get(),
                                 biDanh.get(),
                                 maHoKhau.get(),
                                 quanHe.get(),
                                 ngayDK.get_date().strftime("%m/%d/%y"),
                                 diaChiCu)
        messagebox.showinfo("", "Thêm nhân khẩu mới thành công!")
        switch(f_home)


def ChangePerson():
    # Create a child frame to destroy when no use parent frame
    f_all_change_person = tkinter.Frame(
        f_change_person, highlightbackground="black", highlightthickness=2)
    f_change_person.grid_columnconfigure(0, weight=1)
    f_change_person.grid_rowconfigure(0, weight=1)
    f_all_change_person.grid(column=0, row=0, sticky='news', padx=20, pady=20)

    f_all_change_person.grid_columnconfigure(0, weight=1)
    f_all_change_person.grid_columnconfigure(1, weight=1)
    f_all_change_person.grid_columnconfigure(2, weight=1)
    f_all_change_person.grid_columnconfigure(3, weight=1)

    # NgayChuyenDi, NoiChuyenDi, GhiChu, HoTen, CCCD, MaSo
    # row 0
    tkinter.Label(f_all_change_person, text="Thay đổi nhân khẩu",
                  font=font_header1, justify=CENTER).grid(column=0, row=0, columnspan=4)

    # row 1
    tkinter.Label(
        f_all_change_person, text="Họ và tên: ", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

    hoTen = tkinter.Entry(
        f_all_change_person, font=font_content, width=60)
    hoTen.grid(column=1, row=1, padx=padx, pady=pady, columnspan=3)

    # row 2
    tkinter.Label(
        f_all_change_person, text="Số căn cước công dân:", anchor=W, font=font_content).grid(column=0, row=2, padx=padx, pady=pady, sticky=W, columnspan=1)

    CCCD = tkinter.Entry(f_all_change_person, font=font_content, width=20)
    CCCD.grid(column=1, row=2, padx=padx,
              pady=pady, sticky=W, columnspan=1)

    tkinter.Label(
        f_all_change_person, text="Mã hộ khẩu: ", anchor=W, font=font_content).grid(column=2, row=2, padx=padx,
                                                                                    pady=pady, sticky=W, columnspan=1)

    maHoKhau = tkinter.Entry(f_all_change_person, font=font_content, width=20)
    maHoKhau.grid(column=3, row=2, padx=padx,
                  pady=pady, sticky=W, columnspan=1)
    # row 3
    tkinter.Label(
        f_all_change_person, text="Ngày chuyển đi: ", font=font_content, anchor=W).grid(column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

    ngayChuyenDi = DateEntry(f_all_change_person, font=font_content)
    ngayChuyenDi.grid(column=1, row=3, sticky=W,
                      padx=padx, pady=pady, columnspan=1)

    # row 4
    tkinter.Label(
        f_all_change_person, text="Nơi chuyển đi : ", font=font_content, anchor=W).grid(column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)

    noiChuyenDi = tkinter.Entry(
        f_all_change_person, font=font_content, width=60)
    noiChuyenDi.grid(column=1, row=4, padx=padx, pady=pady, columnspan=3)
    # row 5
    tkinter.Label(
        f_all_change_person, text="Ghi chú: ", font=font_content, anchor=W).grid(column=0, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    ghiChu = tkinter.Entry(
        f_all_change_person, font=font_content, width=60)
    ghiChu.grid(column=1, row=5, padx=padx, pady=pady, columnspan=3)
    # row 6
    tkinter.Button(
        f_all_change_person, text="Gửi",  font=font_header3, fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: submit()).grid(column=0, row=6, padx=padx, pady=pady, columnspan=4)

    # row 7
    errorMessage = tkinter.Label(
        f_all_change_person, text="", font=font_content, fg="red", justify=CENTER)
    errorMessage.grid(column=0, row=7, columnspan=4)

    def submit():
        # NgayChuyenDi, NoiChuyenDi, GhiChu, HoTen, CCCD, MaSo

        errorCode = ChucNang.ThayDoiNhanKhau(ngayChuyenDi.get(), noiChuyenDi.get(),
                                             ghiChu.get(), hoTen.get(), CCCD.get(), maHoKhau.get())

        if (errorCode == 0):
            messagebox.showinfo("", "Thay đổi nhân khẩu thành công!")
            switch(f_home)
        # errC = 1 trong trường hợp không tìm thấy dữ liệu
        elif (errorCode == 1):
            errorMessage['text'] = "Vui lòng kiểm tra lại CCCD, Họ tên, Mã hộ khẩu"
        # errC = 2 trong trường hợp chuyển đi mà không nhập nơi chuyển đi
        elif (errorCode == 2):
            errorMessage['text'] = "Vui lòng thêm nơi chuyển đi"


'''Thay đổi chủ hộ'''


def ViewAuthenChangeHostPerson():
    # Create a child frame to destroy when no use parent frame
    f_all_authen_change_host_person = tkinter.Frame(
        f_authen_change_host_person)
    f_authen_change_host_person.grid_columnconfigure(0, weight=1)
    f_authen_change_host_person.grid_rowconfigure(0, weight=1)
    f_all_authen_change_host_person.grid(column=0, row=0, sticky='news')
    f_all_authen_change_host_person.config(padx=10, pady=30)
    tkinter.Label(
        f_all_authen_change_host_person, text="Nhập mã hộ khẩu", font=font_content, anchor=W).grid(column=0, row=0, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryHostId = tkinter.Entry(
        f_all_authen_change_host_person, font=font_content, width=20)
    entryHostId.grid(column=1, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_change_host_person, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: Authen(entryHostId.get(), errorMessage)).grid(column=0, row=1, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_change_host_person, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)

    def Authen(maHoKhau, errorMessage):
        errorCode, hoKhau, listCuDan = ChucNang.XemSoHoKhau(maHoKhau)
        if (errorCode):
            errorMessage['text'] = f"Số hộ khẩu: {maHoKhau} bị sai!. Vui lòng nhập lại"

        else:
            switch(frame=f_change_host_person, maHoKhau=maHoKhau,
                   hoKhau=hoKhau, listCuDan=listCuDan)

# Thông tin nhân khẩu:
# ID ,CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú


def ChangeHostPerson(maHoKhau, hoKhau, listCuDan):
    n = len(listCuDan)
    # Create a child frame to destroy when no use parent frame
    f_all_change_host_person = tkinter.Frame(
        f_change_host_person, highlightbackground="black", highlightthickness=2)
    f_change_host_person.grid_columnconfigure(0, weight=1)
    f_change_host_person.grid_rowconfigure(0, weight=1)
    f_all_change_host_person.grid(
        column=0, row=0, sticky='news', padx=20, pady=20)

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

    tkinter.Button(f_all_change_host_person, text="Gửi",  font=font_header3, fg="white", bg="blue",
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
            switch(f_home)


'''Tách khẩu'''


def ViewAuthenTachKhau():
    # Create a child frame to destroy when no use parent frame
    f_all_authen_tach_khau = tkinter.Frame(
        f_authen_tach_khau)
    f_authen_tach_khau.grid_columnconfigure(0, weight=1)
    f_authen_tach_khau.grid_rowconfigure(0, weight=1)
    f_all_authen_tach_khau.grid(column=0, row=0, sticky='news')
    f_all_authen_tach_khau.config(padx=10, pady=30)
    tkinter.Label(
        f_all_authen_tach_khau, text="Nhập mã hộ khẩu", font=font_content, anchor=W).grid(column=0, row=0, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryHostId = tkinter.Entry(
        f_all_authen_tach_khau, font=font_content, width=20)
    entryHostId.grid(column=1, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_tach_khau, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: Authen(entryHostId.get(), errorMessage)).grid(column=0, row=1, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_tach_khau, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)

    def Authen(maHoKhau, errorMessage):
        errorCode, hoKhau, listCuDan = ChucNang.XemSoHoKhau(maHoKhau)
        if (errorCode):
            errorMessage['text'] = f"Số hộ khẩu: {maHoKhau} bị sai!. Vui lòng nhập lại"

        else:
            switch(frame=f_tach_khau, maHoKhau=maHoKhau,
                   hoKhau=hoKhau, listCuDan=listCuDan)

# Thông tin nhân khẩu:
# ID ,CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú


def TachKhau(maHoKhau, hoKhau, listCuDan):
    n = len(listCuDan)
    # Create a child frame to destroy when no use parent frame
    f_all_tach_khau = tkinter.Frame(
        f_tach_khau, highlightbackground="black", highlightthickness=2)
    f_tach_khau.grid_columnconfigure(0, weight=1)
    f_tach_khau.grid_rowconfigure(0, weight=1)
    f_all_tach_khau.grid(
        column=0, row=0, sticky='news', padx=20, pady=20)

    f_all_tach_khau.grid_columnconfigure(0, weight=1)
    f_all_tach_khau.grid_columnconfigure(1, weight=1)
    f_all_tach_khau.grid_columnconfigure(2, weight=1)
    f_all_tach_khau.grid_columnconfigure(3, weight=1)

    for i in range(n+7):
        f_all_tach_khau.grid_rowconfigure(i, weight=1)

    tkinter.Label(
        f_all_tach_khau, text="Tách khẩu", font=font_header1, justify=CENTER).grid(column=0, row=0, columnspan=3)

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

    tkinter.Label(f_all_tach_khau, text="Nhập địa chỉ hộ khẩu mới: ",
                  font=font_content, anchor=W, justify=LEFT).grid(column=0, row=2+n, sticky=W, columnspan=4)
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

    tkinter.Button(f_all_tach_khau, text="Gửi",  font=font_header3, fg="white", bg="blue",
                   command=lambda: submit()).grid(column=0, row=5+n, columnspan=3)
    errorMessage = tkinter.Label(f_all_tach_khau, text="", font=font_content,
                                 fg="red", justify=CENTER)
    errorMessage.grid(column=0, row=6+n, columnspan=3)

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
            ChucNang.TachHoKhau(hoKhauOld, hoKhauNew)
            messagebox.showinfo("", "Tách khẩu thành công"),
            switch(f_home)


'''Tạm trú'''


def TamTru():
    f_all_tam_tru = tkinter.Frame(f_tam_tru)
    f_tam_tru.grid_columnconfigure(0, weight=1)
    f_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_tam_tru.grid(column=0, row=0, sticky='news')
    f_all_tam_tru.config(padx=10, pady=30)

    tkinter.Label(
        f_all_tam_tru, text="Chọn yêu cầu của bạn: ", font=font_content, anchor=W).grid(column=0, row=0, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Tạo giấy tạm trú", "Xem giấy tạm trú")
    chosed = StringVar(f_all_tam_tru)
    dropDownTamTru = ttk.OptionMenu(
        f_all_tam_tru, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownTamTru['menu'].configure(font=('Arial', 12))
    dropDownTamTru.grid(column=1, row=0, sticky=W,
                        padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_tam_tru, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: Authen(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def Authen(chose):
        if (chose == "Tạo giấy tạm trú"):
            switch(f_tao_giay_tam_tru)
        elif (chose == "Xem giấy tạm trú"):
            switch(f_authen_xem_giay_tam_tru)


# HoTen, CCCD, QueQuan, DiaChiThuongTru, NgayBatDau: datetime.datetime, NgayKetThuc: datetime.datetime, LyDo, NgayLamDon: datetime.datetime

def TaoGiayTamTru():
    # Create a child frame to destroy when no use parent frame
    f_all_tao_giay_tam_tru = tkinter.Frame(
        f_tao_giay_tam_tru, highlightbackground="black", highlightthickness=2)
    f_tao_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_tao_giay_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_tao_giay_tam_tru.grid(
        column=0, row=0, sticky='news', padx=20, pady=20)

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
                            font=font_content)
    hoVaTen.grid(column=1, row=1, sticky=W,
                 padx=padx, pady=pady, columnspan=3)
    # row 2
    tkinter.Label(f_all_tao_giay_tam_tru, text="CCCD:", font=font_content, anchor=W).grid(
        column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    CCCD = tkinter.Entry(f_all_tao_giay_tam_tru, font=font_content, width=20)
    CCCD.grid(column=1, row=2, sticky=W,
              padx=padx, pady=pady, columnspan=1)

    # row 3
    tkinter.Label(f_all_tao_giay_tam_tru, text="Quê quán:", font=font_content, anchor=W).grid(
        column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)
    queQuan = tkinter.Entry(f_all_tao_giay_tam_tru,
                            font=font_content, width=60)
    queQuan.grid(column=1, row=3, sticky=W,
                 padx=padx, pady=pady, columnspan=3)

    # row 4
    tkinter.Label(f_all_tao_giay_tam_tru, text="Địa chỉ thường trú:", font=font_content, anchor=W).grid(
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
        if (hoVaTen.get() == "" or CCCD.get() == "" or queQuan.get() == "" or thuongTru.get() == "" or lyDo.get("1.0", 'end-1c') == ""):
            errorMessage['text'] = "Vui lòng điền đầy đủ các trường!"
            return
        errorCode = ChucNang.CapGiayTamTru(hoVaTen.get(), CCCD.get(), queQuan.get(), thuongTru.get(), tuNgay.get_date().strftime(
            "%m/%d/%y"), denNgay.get_date().strftime("%m/%d/%y"), lyDo.get("1.0", 'end-1c'), ngayLamDon.get_date().strftime("%m/%d/%y"))
        if (errorCode == 0):
            messagebox.showinfo("", "Đã hoàn thành đơn tạm trú")
            switch(f_home)
        elif (errorCode == 1):
            errorMessage['text'] = "Vui lòng kiểm tra lại thông tin!"
            return


def AuthenXemGiayTamTru():
    f_all_authen_xem_giay_tam_tru = tkinter.Frame(
        f_authen_xem_giay_tam_tru)
    f_authen_xem_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_authen_xem_giay_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_authen_xem_giay_tam_tru.grid(column=0, row=0, sticky='news')
    f_all_authen_xem_giay_tam_tru.config(padx=10, pady=30)
    tkinter.Label(
        f_all_authen_xem_giay_tam_tru, text="Họ và tên:", font=font_content, anchor=W).grid(column=0, row=0, sticky=W, padx=padx, pady=pady, columnspan=1)
    hoVaTen = tkinter.Entry(
        f_all_authen_xem_giay_tam_tru, font=font_content, width=20)
    hoVaTen.grid(column=1, row=0, sticky=W,
                 padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_authen_xem_giay_tam_tru, text="CCCD:", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    CCCD = tkinter.Entry(
        f_all_authen_xem_giay_tam_tru, font=font_content, width=20)
    CCCD.grid(column=1, row=1, sticky=W,
              padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_xem_giay_tam_tru, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit()).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_xem_giay_tam_tru, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)

    def submit():
        if (hoVaTen.get() == "" or CCCD.get() == ""):
            errorMessage['text'] = "Vui lòng nhập đầy đủ thông tin!"
            return

        errorCode, thongTinGiayTamTru = ChucNang.XemGiayTamTru(
            hoVaTen.get(), CCCD.get())
        if (errorCode):
            errorMessage['text'] = "Thông tin bị sai!. Vui lòng nhập lại"

        else:
            switch(frame=f_xem_giay_tam_tru, data=thongTinGiayTamTru)

# MaGiayTamTru, HoTen, CCCD, Tu, Den, LyDo, NgayLamDon


def XemGiayTamTru(thongTinGiayTamTru):
    # Create a child frame to destroy when no use parent frame
    f_all_xem_giay_tam_tru = tkinter.Frame(
        f_xem_giay_tam_tru, highlightbackground="black", highlightthickness=2)
    f_xem_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_xem_giay_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_xem_giay_tam_tru.grid(
        column=0, row=0, sticky='news', padx=10, pady=5)

    f_all_xem_giay_tam_tru.grid_columnconfigure(0, weight=1)
    f_all_xem_giay_tam_tru.grid_columnconfigure(1, weight=1)
    f_all_xem_giay_tam_tru.grid_columnconfigure(2, weight=1)
    f_all_xem_giay_tam_tru.grid_columnconfigure(3, weight=1)
    # row 0
    tkinter.Label(f_all_xem_giay_tam_tru, text=f"Đơn xin tạm trú mã {thongTinGiayTamTru.MaGiayTamTru}", font=font_header1).grid(
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

    # # row 3
    # tkinter.Label(f_all_xem_giay_tam_tru, text="Quê quán:", font=font_content, anchor=W).grid(
    #     column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)
    # tkinter.Label(f_all_xem_giay_tam_tru, text=thongTinGiayTamTru.QueQuan,
    #               font=font_content, anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=3, padx=padx, pady=pady, sticky=W)

    # # row 4
    # tkinter.Label(f_all_xem_giay_tam_tru, text="Địa chỉ thường trú:", font=font_content, anchor=W).grid(
    #     column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)
    # tkinter.Label(f_all_xem_giay_tam_tru, text=thongTinGiayTamTru.HoTen,
    #               font=font_content, anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=3, padx=padx, pady=pady, sticky=W)

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

    tkinter.Button(f_all_xem_giay_tam_tru, text="Về trang chủ", font=font_header3, fg="white", bg="blue", relief='groove',
                   cursor='hand2', command=lambda: switch(f_home)).grid(column=0, row=9, columnspan=4, padx=padx, pady=pady)


'''Tạm vắng'''


def TamVang():
    f_all_tam_vang = tkinter.Frame(f_tam_vang)
    f_tam_vang.grid_columnconfigure(0, weight=1)
    f_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_tam_vang.grid(column=0, row=0, sticky='news')
    f_all_tam_vang.config(padx=10, pady=30)

    tkinter.Label(
        f_all_tam_vang, text="Chọn yêu cầu của bạn: ", font=font_content, anchor=W).grid(column=0, row=0, sticky=W, padx=padx, pady=pady, columnspan=1)

    option = ("Tạo giấy tạm vắng", "Xem giấy tạm vắng")
    chosed = StringVar(f_all_tam_vang)
    dropDownTamVang = ttk.OptionMenu(
        f_all_tam_vang, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownTamVang['menu'].configure(font=('Arial', 12))
    dropDownTamVang.grid(column=1, row=0, sticky=W,
                         padx=padx, pady=pady, columnspan=1)
    tkinter.Button(
        f_all_tam_vang, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: Authen(chosed.get())).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    def Authen(chose):
        if (chose == "Tạo giấy tạm vắng"):
            switch(f_tao_giay_tam_vang)
        elif (chose == "Xem giấy tạm vắng"):
            switch(f_authen_xem_giay_tam_vang)


# HoTen, CCCD, NoiTamVang, NgayBatDau: datetime.datetime, NgayKetThuc: datetime.datetime, LyDo, NgayLamDon: datetime.datetime

def TaoGiayTamVang():
    # Create a child frame to destroy when no use parent frame
    f_all_tao_giay_tam_vang = tkinter.Frame(
        f_tao_giay_tam_vang, highlightbackground="black", highlightthickness=2)
    f_tao_giay_tam_vang.grid_columnconfigure(0, weight=1)
    f_tao_giay_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_tao_giay_tam_vang.grid(
        column=0, row=0, sticky='news', padx=20, pady=20)

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

    # # row 4
    # tkinter.Label(f_all_tao_giay_tam_vang, text="Địa chỉ thường trú:", font=font_content, anchor=W).grid(
    #     column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)
    # thuongTru = tkinter.Entry(f_all_tao_giay_tam_vang,
    #                           font=font_content, width=60)
    # thuongTru.grid(column=1, row=4, sticky=W,
    #                padx=padx, pady=pady, columnspan=3)

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
            switch(f_home)
        elif (errorCode == 1):
            errorMessage['text'] = "Vui lòng kiểm tra lại thông tin!"
            return


def AuthenXemGiayTamVang():
    f_all_authen_xem_giay_tam_vang = tkinter.Frame(
        f_authen_xem_giay_tam_vang)
    f_authen_xem_giay_tam_vang.grid_columnconfigure(0, weight=1)
    f_authen_xem_giay_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_authen_xem_giay_tam_vang.grid(column=0, row=0, sticky='news')
    f_all_authen_xem_giay_tam_vang.config(padx=10, pady=30)
    tkinter.Label(
        f_all_authen_xem_giay_tam_vang, text="Họ và tên:", font=font_content, anchor=W).grid(column=0, row=0, sticky=W, padx=padx, pady=pady, columnspan=1)
    hoVaTen = tkinter.Entry(
        f_all_authen_xem_giay_tam_vang, font=font_content, width=20)
    hoVaTen.grid(column=1, row=0, sticky=W,
                 padx=padx, pady=pady, columnspan=1)

    tkinter.Label(
        f_all_authen_xem_giay_tam_vang, text="CCCD:", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    CCCD = tkinter.Entry(
        f_all_authen_xem_giay_tam_vang, font=font_content, width=20)
    CCCD.grid(column=1, row=1, sticky=W,
              padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_xem_giay_tam_vang, text="Gửi",  font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: submit()).grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_xem_giay_tam_vang, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)

    def submit():
        if (hoVaTen.get() == "" or CCCD.get() == ""):
            errorMessage['text'] = "Vui lòng nhập đầy đủ thông tin!"
            return

        errorCode, thongTinGiayTamVang = ChucNang.XemGiayTamVang(
            hoVaTen.get(), CCCD.get())
        if (errorCode):
            errorMessage['text'] = "Thông tin bị sai!. Vui lòng nhập lại"

        else:
            switch(frame=f_xem_giay_tam_vang, data=thongTinGiayTamVang)


# MaGiayTamVang, HoTen, CCCD, NoiTamVang ,Tu, Den, LyDo, NgayLamDon

def XemGiayTamVang(thongTinGiayTamVang):
    # Create a child frame to destroy when no use parent frame
    f_all_xem_giay_tam_vang = tkinter.Frame(
        f_xem_giay_tam_vang, highlightbackground="black", highlightthickness=2)
    f_xem_giay_tam_vang.grid_columnconfigure(0, weight=1)
    f_xem_giay_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_xem_giay_tam_vang.grid(
        column=0, row=0, sticky='news', padx=10, pady=5)

    f_all_xem_giay_tam_vang.grid_columnconfigure(0, weight=1)
    f_all_xem_giay_tam_vang.grid_columnconfigure(1, weight=1)
    f_all_xem_giay_tam_vang.grid_columnconfigure(2, weight=1)
    f_all_xem_giay_tam_vang.grid_columnconfigure(3, weight=1)
    # row 0
    tkinter.Label(f_all_xem_giay_tam_vang, text=f"Đơn xin tạm vắng mã {thongTinGiayTamVang.MaGiayTamVang}", font=font_header1).grid(
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

    # # row 4
    # tkinter.Label(f_all_xem_giay_tam_vang, text="Địa chỉ thường trú:", font=font_content, anchor=W).grid(
    #     column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)
    # tkinter.Label(f_all_xem_giay_tam_vang, text=thongTinGiayTamVang.HoTen,
    #               font=font_content, anchor=W, justify=LEFT).grid(column=1, row=1, columnspan=3, padx=padx, pady=pady, sticky=W)

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

    tkinter.Button(f_all_xem_giay_tam_vang, text="Về trang chủ", font=font_header3, fg="white", bg="blue", relief='groove',
                   cursor='hand2', command=lambda: switch(f_home)).grid(column=0, row=9, columnspan=4, padx=padx, pady=pady)


"""END HOME"""

# ------------------------------------------------------------------------------------------------------------------------------------

"""Family <=> Xem hộ khẩu"""
# Giao diện check mã hộ khẩu (hostId)


def ViewAuthenFamily():
    # Create a child frame to destroy when no use parent frame
    f_all_authen_family = tkinter.Frame(
        f_authen_family)
    f_authen_family.grid_columnconfigure(0, weight=1)
    f_authen_family.grid_rowconfigure(0, weight=1)
    f_all_authen_family.grid(column=0, row=0, sticky='news')
    f_all_authen_family.config(padx=10, pady=30)
    tkinter.Label(
        f_all_authen_family, text="Nhập mã hộ khẩu", font=font_content, anchor=W).grid(column=0, row=0, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryHostId = tkinter.Entry(
        f_all_authen_family, font=font_content, width=20)
    entryHostId.grid(column=1, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    tkinter.Button(
        f_all_authen_family, text="Gửi", font=font_header3, fg="white", bg="blue", relief='groove', cursor='hand2', command=lambda: Authen(entryHostId.get(), errorMessage)).grid(column=0, row=1, padx=padx, pady=pady, columnspan=2)

    errorMessage = tkinter.Label(
        f_all_authen_family, text="", font=font_content, fg="red", anchor=W)
    errorMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)

    def Authen(hostId, errorMessage):
        errorCode, hoKhau, listCuDan = ChucNang.XemSoHoKhau(hostId)
        if (errorCode):
            errorMessage['text'] = f"Số hộ khẩu: {hostId} bị sai!. Vui lòng nhập lại"

        else:
            switch(frame=f_family, maHoKhau=hostId,
                   hoKhau=hoKhau, listCuDan=listCuDan)

# Thông tin nhân khẩu:
# ID ,CCCD, Hoten, GioiTinh, NgaySinh, DanToc, QuocTich, NgheNghiep, QueQuan, BiDanh, Mã sổ , QuanHe, Ngày đăng kí thường trú, dịa chỉ cũ, Ngày chuyển đi, nơi chuyển đi, ghi chú
# Giao diện xem nhân khẩu


def ViewFamily(hoKhau, listCuDan):
    n = len(listCuDan)
    # Create a child frame to destroy when no use parent frame
    f_all_view_family = tkinter.Frame(
        f_family, highlightbackground="black", highlightthickness=2)
    f_family.grid_columnconfigure(0, weight=1)
    f_family.grid_rowconfigure(0, weight=1)
    f_all_view_family.grid(
        column=0, row=0, sticky='news', padx=20, pady=20)
    f_all_view_family.grid_columnconfigure(0, weight=1)
    f_all_view_family.grid_columnconfigure(1, weight=1)
    f_all_view_family.grid_columnconfigure(2, weight=1)
    f_all_view_family.grid_columnconfigure(3, weight=1)

    def showPerson(i):
        if (n == 0):
            f_all_view_family.grid_columnconfigure(0, weight=1)
            f_all_view_family.grid_rowconfigure(0, weight=1)
            f_all_view_family.grid_columnconfigure(4, weight=0)

            tkinter.Label(f_all_view_family, text="Không có data", fg="red",
                          font=font_header1).grid(column=0, row=0)
        else:
            # Không cho đi về trước nhân khẩu đầu tiên
            if (i <= 0):
                i = 0
            # Không cho đi quá nhân khẩu cuối
            elif (i >= n-1):
                i = n-1
            # Xóa dữ liệu cũ
            for widget in f_all_view_family.winfo_children():
                widget.destroy()
            # Hiện thông tin nhân khẩu thứ i
            PersonInfo(i)

    def PersonInfo(i):
        # row 0
        tkinter.Label(
            f_all_view_family, text="Quan hệ với chủ hộ:", font=font_header3, anchor=W).grid(row=0, column=0, columnspan=2, padx=padx, pady=pady, sticky=W)
        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][11], font=font_content).grid(row=0, column=2, padx=padx, pady=pady, sticky=W, columnspan=2)

        # row 1
        tkinter.Label(
            f_all_view_family, text="Họ và tên:", font=font_content, anchor=W).grid(column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][2], font=font_content).grid(column=1, row=1, padx=padx, pady=pady, columnspan=3, sticky=W)

        # row 2
        tkinter.Label(
            f_all_view_family, text="Bí danh(Nếu có):", font=font_content, anchor=W).grid(column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][9], font=font_content).grid(column=1, row=2, padx=padx, pady=pady, columnspan=1, sticky=W)

        tkinter.Label(
            f_all_view_family, text="Nghề nghiệp : ", font=font_content, anchor=W).grid(column=2, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][7], font=font_content, justify=LEFT).grid(column=3, row=2, padx=padx, pady=pady, columnspan=1, sticky=W)

        # row 3
        tkinter.Label(
            f_all_view_family, text="Ngày sinh: ", font=font_content, anchor=W).grid(column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

        Label(
            f_all_view_family, anchor=W, text=listCuDan[i][4], font=font_content).grid(column=1, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, text="Giới tính: ", font=font_content, anchor=W).grid(column=2, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

        Label(
            f_all_view_family, anchor=W, text=listCuDan[i][3], font=font_content).grid(column=3, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)

        # row 4
        tkinter.Label(
            f_all_view_family, text="Quê quán: ", font=font_content, anchor=W).grid(column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][8], font=font_content).grid(column=1, row=4, sticky=W, padx=padx, pady=pady, columnspan=3)

        # row 5
        tkinter.Label(
            f_all_view_family, text="Số căn cước công dân: ", anchor=W, font=font_content).grid(column=0, row=5, padx=padx, pady=pady, sticky=W, columnspan=2)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][1], font=font_content).grid(column=2, row=5, padx=padx, pady=pady, sticky=W, columnspan=2)

        # row 6
        tkinter.Label(
            f_all_view_family, text="Dân tộc: ", font=font_content, anchor=W).grid(column=0, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][5], font=font_content).grid(column=1, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, text="Quốc tịch: ", font=font_content, anchor=W).grid(column=2, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)
        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][6], font=font_content).grid(column=3, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)

        # row 7
        tkinter.Label(
            f_all_view_family, text="Địa chỉ cũ:", font=font_content, anchor=W).grid(column=0, row=7, sticky=W, padx=padx, pady=pady, columnspan=2)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][13], font=font_content).grid(column=1, row=7, padx=padx, pady=pady, columnspan=3, sticky=W)

        # row 8
        tkinter.Label(
            f_all_view_family, text="Ngày đăng ký thường trú:", font=font_content, anchor=W).grid(column=0, row=8, sticky=W, padx=padx, pady=pady, columnspan=2)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][12], font=font_content).grid(column=2, row=8, padx=padx, pady=pady, columnspan=2, sticky=W)

        # row 9
        tkinter.Label(
            f_all_view_family, text="Ngày chuyển đi:", font=font_content, anchor=W).grid(column=0, row=9, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][14], font=font_content).grid(column=1, row=9, padx=padx, pady=pady, columnspan=3, sticky=W)

        # row 10
        tkinter.Label(
            f_all_view_family, text="Nơi chuyển đi:", font=font_content, anchor=W).grid(column=0, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][15], font=font_content).grid(column=1, row=10, padx=padx, pady=pady, columnspan=3, sticky=W)
        # row 11
        tkinter.Label(
            f_all_view_family, text="Ghi chú:", font=font_content, anchor=W).grid(column=0, row=11, sticky=W, padx=padx, pady=pady, columnspan=1)

        tkinter.Label(
            f_all_view_family, anchor=W, text=listCuDan[i][16], font=font_content).grid(column=1, row=11, padx=padx, pady=pady, columnspan=3, sticky=W)
        # row 12
        if (i != 0):
            tkinter.Button(
                f_all_view_family, text="Trang trước",  font=font_header3, fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPerson(i-1)).grid(column=0, row=12, sticky=W, padx=padx, pady=pady, columnspan=1)
        if (i != n-1):
            tkinter.Button(
                f_all_view_family, text="Trang sau",  font=font_header3, fg="white", bg="blue", relief="groove", cursor='hand2', command=lambda: showPerson(i+1)).grid(column=3, row=12, sticky=E, padx=padx, pady=pady, columnspan=1)

    showPerson(0)


"""END FAMILY"""


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
    tkinter.Button(f_log_in, text="Đăng nhập", font=font_header2, bg="blue", fg="white",
                   command=lambda: submit(userName.get(), password.get())).grid(row=5, column=0, columnspan=2, padx=180, sticky=NW)
    ttk.Separator(f_log_in, orient=HORIZONTAL).grid(
        column=0, row=6, columnspan=2, sticky=EW)

    errorMessage = tkinter.Label(
        f_log_in, text="", font=font_header2, fg="red", bg="white", justify=CENTER)
    errorMessage.grid(column=0, row=7, columnspan=2)

    def submit(tendangnhap, matkhau):
        maQuanLy = ChucNang.DangNhap(tendangnhap, matkhau)
        if (maQuanLy == 0):
            errorMessage["text"] = "Thông tin đăng nhập không đúng"

        else:
            switch(frame=f_home, maQuanLy=maQuanLy)
            f_log_in.destroy()


LogIn()
root.mainloop()
