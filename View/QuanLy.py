from tkinter import *
from tkinter import ttk
import config.config as config
import tkinter
import os
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
import connectDB

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


def switch(frame, hostId=""):
    for f in frames:
        for widget in f.winfo_children():
            widget.destroy()
    global btn_home_bg, btn_family_bg, btn_demand_bg
    if (frame == f_home):
        btn_home_bg = config.selected_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        Home()
    elif (frame == f_family):
        btn_home_bg = win_bg
        btn_family_bg = config.selected_bg
        btn_demand_bg = win_bg
        ViewFamily(hostId)
    elif (frame == f_authen_change):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AuthenChange()
    elif (frame == f_authen_family):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AuthenFamily()
    elif (frame == f_add_person):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AddPerson(hostId)
    elif (frame == f_authen_fix_info):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AuthenFixInfo()
    elif (frame == f_fix_info):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        FixInfo(hostId)  # HostId ~ CCCD
    elif (frame == f_change_host_person):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        ChangeHostPerson(hostId)
    elif (frame == f_authen_view_my_info):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AuthenViewMyInfo()
    elif (frame == f_view_my_info):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        ViewMyInfo(hostId)  # HostId ~ CCCD
    elif (frame == f_authen_tach_khau):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        AuthenTachKhau()
    elif (frame == f_tach_khau):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        TachKhau(hostId)
    elif (frame == f_tam_tru):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        TamTru()
    elif (frame == f_tam_vang):
        btn_home_bg = win_bg
        btn_family_bg = win_bg
        btn_demand_bg = win_bg
        TamVang()
    Nav()
    frame.tkraise()

# Kiểm tra xem 1 sổ hộ khẩu có tồn tại hay không theo số hộ khẩu


def CheckHostId(hostId):
    # getAllHoKhau trả về 1 list các tupple chứa các trường => đưa hostId vào 1 tupple để so sánh
    hostId = (hostId,)
    allHostId = connectDB.getAllHoKhau()
    if (hostId in allHostId):
        return True
    return False


def AuthenticationChange(hostId, message, chosed):
    # Nếu hộ khẩu tồn tại => Chuyển tới các chức năng theo yêu cầu
    if (CheckHostId(hostId)):
        if (chosed == "Thêm nhân khẩu"):
            switch(f_add_person, hostId)
        elif (chosed == "Sửa thông tin nhân khẩu"):
            switch(f_authen_fix_info)
        elif (chosed == "Thay đổi chủ hộ"):
            switch(f_change_host_person, hostId)
        else:
            switch(f_home)
    # Hộ khẩu không tồn tại => Xuất thông báo
    else:
        message['text'] = f"Số hộ khẩu: {hostId} bị sai!. Vui lòng nhập lại"


def AuthenticationFamily(hostId, message):
    if (CheckHostId(hostId)):
        switch(f_family, hostId)
    else:
        message['text'] = f"Số hộ khẩu: {hostId} bị sai!. Vui lòng nhập lại"

# Kiểm tra xem 1 người có tồn tại hay không theo CCCD


def CheckPerson(CCCD):
    if (len(connectDB.getCUDAN(CCCD)) == 0):
        return False
    return True
# Sử dụng để hiện thông báo hoặc chuyển màn hình khi xem thông tin


def AuthenticationFixInfo(CCCD, message):
    if (CheckPerson(CCCD)):
        switch(f_fix_info, CCCD)
    else:
        message['text'] = f"Không tồn tại CCCD: {CCCD}!. Vui lòng nhập lại"


def AuthenticationViewMyInfo(CCCD, message):
    if (CheckPerson(CCCD)):
        switch(f_view_my_info, CCCD)
    else:
        message['text'] = f"Không tồn tại CCCD: {CCCD}!. Vui lòng nhập lại"

# Chuyển màn hình hoặc hiện thông báo


def AuthenticationTachKhau(hostId, message):
    if (CheckHostId(hostId)):
        switch(f_tach_khau, hostId)
    else:
        message['text'] = f"Số hộ khẩu: {hostId} bị sai!. Vui lòng nhập lại"


# Config style cho drop down menu
someStyle = ttk.Style()
someStyle.configure('DropDownStyle.TMenubutton',
                    font=('Arial', 12, "bold"))
'''Load IMAGE'''
# Nav Bar
pathLogo = os.path.join(
    dirname, 'config\\image\\icon_homepage.png')
logoIcon = Image.open(pathLogo)
logoIcon = logoIcon.resize(
    (60, 60), Image.ANTIALIAS)
logoIcon = ImageTk.PhotoImage(logoIcon)
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

# Tạo các frame sẵn để nâng lên khi cần xuất hiện
f_home = tkinter.Frame(root)
f_family = tkinter.Frame(root)
f_authen_change = tkinter.Frame(root)
f_authen_family = tkinter.Frame(root)
f_add_person = tkinter.Frame(root)
f_authen_fix_info = tkinter.Frame(root)
f_fix_info = tkinter.Frame(root)
f_change_host_person = tkinter.Frame(root)
f_authen_view_my_info = tkinter.Frame(root)
f_view_my_info = tkinter.Frame(root)
f_authen_tach_khau = tkinter.Frame(root)
f_tach_khau = tkinter.Frame(root)
f_tam_tru = tkinter.Frame(root)
f_tam_vang = tkinter.Frame(root)
# set các frame chồng lên nhau.
frames = (f_home, f_family, f_authen_change, f_authen_family, f_add_person, f_authen_fix_info,
          f_fix_info, f_change_host_person, f_authen_view_my_info, f_view_my_info, f_authen_tach_khau, f_tach_khau, f_tam_tru, f_tam_vang)
for f in frames:
    f.place(relx=1, rely=0, relheight=1, relwidth=0.8, anchor=NE)

# separator in root
win_separator = ttk.Separator(root, orient=VERTICAL)
win_separator.place(relx=0.199, rely=0, relheight=1, anchor=NW)
# nav_bar
nav_bar = tkinter.Frame(root, bg=win_bg)
nav_bar.place(relx=0, rely=0, relheight=1, relwidth=0.198, anchor=NW)


'''Code Nav Bar'''


def Nav():
    # 1.Top
    topFrameNav = tkinter.Frame(nav_bar, padx=10, pady=5, bg=win_bg)
    topFrameNav.place(relx=0, rely=0, relwidth=1, relheight=0.15, anchor=NW)
    # 1.1 In top nav
    labelLogoApp = tkinter.Label(topFrameNav, image=logoIcon,
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
        settingFrame_bottom_nav, text="Setting", font=font_header3, anchor=W, bg=win_bg, borderwidth=0, cursor="hand2", command="")
    labelText_setting.place(
        relx=1, rely=0, relheight=1, relwidth=0.7, anchor=NE)


'''End Nav Bar'''
# ---------------------------------------------------------------------------------------------------------------------------------
"""Start Home"""


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

    buttonChangePerson = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=changePersonImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_authen_change))
    buttonChangePerson.place(
        relx=0.1, rely=0.1, relwidth=0.8, relheight=0.07, anchor=NW)
    # -----------------------------------------

    buttonViewMyInfo = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=viewMyInfoImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_authen_view_my_info))
    buttonViewMyInfo.place(
        relx=0.1, rely=0.18, relwidth=0.8, relheight=0.07, anchor=NW)
    # -------------------------------------------

    buttonTachKhau = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tachKhauImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_authen_tach_khau))
    buttonTachKhau.place(
        relx=0.1, rely=0.26, relwidth=0.8, relheight=0.07, anchor=NW)
    # ---------------------------------------------

    buttonTamTru = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tamTruImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_tam_tru))
    buttonTamTru.place(
        relx=0.1, rely=0.34, relwidth=0.8, relheight=0.07, anchor=NW)
    # ------------------------------------------------

    buttonTamVang = tkinter.Button(
        requestFrame_bottom_home, cursor="hand2", image=tamVangImage, borderwidth=0, bg=win_bg, command=lambda: switch(f_tam_vang))
    buttonTamVang.place(
        relx=0.1, rely=0.42, relwidth=0.8, relheight=0.07, anchor=NW)

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


"""END HOME"""
# -----------------------------------------------------------------------------------------------------------------------------------

"""Family Nav Bar"""

# Frame kiểm tra HostId for Family


def AuthenFamily():
    # Create a child frame to destroy when no use parent frame
    f_all_authen_family = tkinter.Frame(f_authen_family)
    f_authen_family.grid_columnconfigure(0, weight=1)
    f_authen_family.grid_rowconfigure(0, weight=1)
    f_all_authen_family.grid(column=0, row=0, sticky='news')
    f_all_authen_family.config(padx=10, pady=30)
    labelHostId = tkinter.Label(
        f_all_authen_family, text="Nhập mã hộ khẩu", font=font_content, anchor=W)
    labelHostId.grid(column=0, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)
    entryHostId = tkinter.Entry(
        f_all_authen_family, font=font_content, width=20)
    entryHostId.grid(column=1, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    buttonSubmit = tkinter.Button(
        f_all_authen_family, text="Gửi", font=font_content, relief='groove', cursor='hand2', command=lambda: AuthenticationFamily(entryHostId.get(), labelMessage))
    buttonSubmit.grid(column=0, row=1, padx=padx, pady=pady, columnspan=2)

    labelMessage = tkinter.Label(
        f_all_authen_family, text="", font=font_content, fg="red", anchor=W)
    labelMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)

# Frame Hiện thông tin gia đình


def ViewFamily(hostId):
    datas = connectDB.getHoKhau(hostId)
    n = len(datas)
    # Create a child frame to destroy when no use parent frame
    f_all_view_family = tkinter.Frame(
        f_family, highlightbackground="black", highlightthickness=2)
    f_family.grid_columnconfigure(0, weight=1)
    f_family.grid_rowconfigure(0, weight=1)
    f_all_view_family.grid(
        column=0, row=0, sticky='news', padx=50, pady=20)

    f_all_view_family.grid_columnconfigure(4, weight=1)

    def showPerson(i):
        if (n == 0):
            f_all_view_family.grid_columnconfigure(0, weight=1)
            f_all_view_family.grid_rowconfigure(0, weight=1)
            f_all_view_family.grid_columnconfigure(4, weight=0)

            tkinter.Label(f_all_view_family, text="Không có data", fg="red",
                          font=font_header1).grid(column=0, row=0)
        else:
            if (i <= 0):
                i = 0
            elif (i >= n-1):
                i = n-1
            for widget in f_all_view_family.winfo_children():
                widget.destroy()
            PersonInfo(i)

    def PersonInfo(i):
        # row 0
        labelRelationShip = tkinter.Label(f_all_view_family, text="Quan hệ với chủ hộ:",
                                          font=font_header3, anchor=W)
        labelRelationShip.grid(row=0, column=0, columnspan=2,
                               padx=padx, pady=pady, sticky=W)
        labelShowRelationShip = tkinter.Label(
            f_all_view_family, anchor=W, text=datas[i][0], font=font_content)
        labelShowRelationShip.grid(row=0, column=2, padx=padx,
                                   pady=pady, sticky=W, columnspan=2)

        # row 1
        labelFullName = tkinter.Label(
            f_all_view_family, text="Họ và tên: ", font=font_content, anchor=W)
        labelFullName.grid(column=0, row=1, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

        labelShowFullName = tkinter.Label(
            f_all_view_family, anchor=W, text=datas[i][1], font=font_content)
        labelShowFullName.grid(column=1, row=1, padx=padx,
                               pady=pady, columnspan=3, sticky=W)

        # row 2
        labelOtherName = tkinter.Label(
            f_all_view_family, text="Họ và tên gọi khác(Nếu có): ", font=font_content, anchor=W)
        labelOtherName.grid(column=0, row=2, sticky=W,
                            padx=padx, pady=pady, columnspan=2)

        labelShowOtherName = tkinter.Label(
            f_all_view_family, anchor=W, text=datas[i][2], font=font_content)
        labelShowOtherName.grid(column=2, row=2, padx=padx,
                                pady=pady, columnspan=2, sticky=W)

        # row 3
        labelBirthDay = tkinter.Label(
            f_all_view_family, text="Ngày sinh: ", font=font_content, anchor=W)
        labelBirthDay.grid(column=0, row=3, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

        labelShowBirthDay = Label(
            f_all_view_family, anchor=W, text=datas[i][3], font=font_content)
        labelShowBirthDay.grid(column=1, row=3, sticky=W,
                               padx=padx, pady=pady, columnspan=1)

        labelGender = tkinter.Label(
            f_all_view_family, text="Giới tính: ", font=font_content, anchor=W)
        labelGender.grid(column=2, row=3, sticky=W,
                         padx=padx, pady=pady, columnspan=1)

        labelShowGender = Label(
            f_all_view_family, anchor=W, text=datas[i][4], font=font_content)
        labelShowGender.grid(column=3, row=3, sticky=W,
                             padx=padx, pady=pady, columnspan=1)

        # row 4
        labelRealAddress = tkinter.Label(
            f_all_view_family, text="Nguyên quán: ", font=font_content, anchor=W)
        labelRealAddress.grid(column=0, row=4, sticky=W,
                              padx=padx, pady=pady, columnspan=1)

        labelShowRealAddress = tkinter.Label(
            f_all_view_family, anchor=W, text=datas[i][5], font=font_content)
        labelShowRealAddress.grid(column=1, row=4, sticky=W,
                                  padx=padx, pady=pady, columnspan=3)

        # row 5
        labelCCCD = tkinter.Label(
            f_all_view_family, text="Số căn cước công dân: ", anchor=W, font=font_content)
        labelCCCD.grid(column=0, row=5, padx=padx,
                       pady=pady, sticky=W, columnspan=2)

        labelShowCCCD = tkinter.Label(
            f_all_view_family, anchor=W, text=datas[i][6], font=font_content)
        labelShowCCCD.grid(column=2, row=5, padx=padx,
                           pady=pady, sticky=W, columnspan=2)

        # row 6
        labelEthnic = tkinter.Label(
            f_all_view_family, text="Dân tộc: ", font=font_content, anchor=W)
        labelEthnic.grid(column=0, row=6, sticky=W,
                         padx=padx, pady=pady, columnspan=1)

        labelShowEthnic = tkinter.Label(
            f_all_view_family, anchor=W, text=datas[i][7], font=font_content)
        labelShowEthnic.grid(column=1, row=6, sticky=W,
                             padx=padx, pady=pady, columnspan=1)

        labelNationality = tkinter.Label(
            f_all_view_family, text="Quốc tịch: ", font=font_content, anchor=W)
        labelNationality.grid(column=2, row=6, sticky=W,
                              padx=padx, pady=pady, columnspan=1)
        labelShowNationality = tkinter.Label(
            f_all_view_family, anchor=W, text=datas[i][8], font=font_content)
        labelShowNationality.grid(column=3, row=6, sticky=W,
                                  padx=padx, pady=pady, columnspan=1)

        # row 7
        labelJob = tkinter.Label(
            f_all_view_family, text="Nghề nghiệp, nơi làm việc: ", font=font_content, anchor=W)
        labelJob.grid(column=0, row=7, sticky=W,
                      padx=padx, pady=pady, columnspan=2)

        labelShowJob = tkinter.Label(
            f_all_view_family, anchor=W, text=datas[i][9], font=font_content)
        labelShowJob.grid(column=2, row=7, padx=padx,
                          pady=pady, columnspan=2, sticky=W)

        # row 8
        labelCurrentAddress = tkinter.Label(
            f_all_view_family, text="Nơi thường trú trước khi chuyển đến:", font=font_content, anchor=W)
        labelCurrentAddress.grid(column=0, row=8, sticky=W,
                                 padx=padx, pady=pady, columnspan=2)

        labelShowCurrentAddress = tkinter.Label(
            f_all_view_family, anchor=W, text=datas[i][10], font=font_content)
        labelShowCurrentAddress.grid(
            column=2, row=8, padx=padx, pady=pady, columnspan=2, sticky=W)
        # row 10
        buttonPrePage = tkinter.Button(
            f_all_view_family, text="Trang trước", font=font_content, relief="groove", cursor='hand2', command=lambda: showPerson(i-1))
        buttonPrePage.grid(column=0, row=9, sticky=W,
                           padx=padx, pady=pady, columnspan=2)

        buttonAfterPage = tkinter.Button(
            f_all_view_family, text="Trang sau", font=font_content, relief="groove", cursor='hand2', command=lambda: showPerson(i+1))
        buttonAfterPage.grid(column=2, row=9, sticky=E,
                             padx=padx, pady=pady, columnspan=2)

    showPerson(0)


"""End Family Nav bar"""
# ---------------------------------------------------------------------------------------------------------------------------------------
"""Thêm nhân khẩu"""


def AuthenChange():
    # Create a child frame to destroy when no use parent frame
    f_all_authen = tkinter.Frame(f_authen_change)
    f_authen_change.grid_columnconfigure(0, weight=1)
    f_authen_change.grid_rowconfigure(0, weight=1)
    f_all_authen.grid(column=0, row=0, sticky='news')
    f_all_authen.config(padx=10, pady=30)
    labelHostId = tkinter.Label(
        f_all_authen, text="Nhập mã hộ khẩu", font=font_content, anchor=W)
    labelHostId.grid(column=0, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)
    entryHostId = tkinter.Entry(f_all_authen, font=font_content, width=20)
    entryHostId.grid(column=1, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    labelGender = tkinter.Label(
        f_all_authen, text="Chọn loại biến đổi: ", font=font_content, anchor=W)
    labelGender.grid(column=0, row=1, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    option = ("Thêm nhân khẩu", "Sửa thông tin nhân khẩu", "Thay đổi chủ hộ")
    chosed = StringVar(f_all_authen)

    dropDownGender = ttk.OptionMenu(
        f_all_authen, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownGender['menu'].configure(font=('Arial', 12))
    dropDownGender.grid(column=1, row=1, sticky=W,
                        padx=padx, pady=pady, columnspan=1)

    buttonSubmit = tkinter.Button(
        f_all_authen, text="Gửi", font=font_content, relief='groove', cursor='hand2', command=lambda: AuthenticationChange(entryHostId.get(), labelMessage, chosed.get()))
    buttonSubmit.grid(column=0, row=2, padx=padx, pady=pady, columnspan=2)

    labelMessage = tkinter.Label(
        f_all_authen, text="", font=font_content, fg="red", anchor=W)
    labelMessage.grid(column=0, row=3, padx=padx,
                      pady=pady, sticky=W, columnspan=2)


def AddPerson(hostId):
    # Create a child frame to destroy when no use parent frame
    f_all_add_person = tkinter.Frame(
        f_add_person, highlightbackground="black", highlightthickness=2)
    f_add_person.grid_columnconfigure(0, weight=1)
    f_add_person.grid_rowconfigure(0, weight=1)
    f_all_add_person.grid(column=0, row=0, sticky='news', padx=20, pady=20)

    f_all_add_person.grid_columnconfigure(0, weight=1)

    # row 0
    labelRelationShip = tkinter.Label(f_all_add_person, text="Quan hệ với chủ hộ:",
                                      font=font_header3, anchor=W)
    labelRelationShip.grid(row=0, column=0, columnspan=2,
                           padx=padx, pady=pady, sticky=W)
    entryRelationShip = tkinter.Entry(
        f_all_add_person, font=font_content, width=40)
    entryRelationShip.grid(row=0, column=2, padx=padx,
                           pady=pady, sticky=W, columnspan=2)

    # row 1
    labelFullName = tkinter.Label(
        f_all_add_person, text="Họ và tên: ", font=font_content, anchor=W)
    labelFullName.grid(column=0, row=1, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    entryFullName = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    entryFullName.grid(column=1, row=1, padx=padx, pady=pady, columnspan=3)

    # row 2
    labelOtherName = tkinter.Label(
        f_all_add_person, text="Họ và tên gọi khác(Nếu có): ", font=font_content, anchor=W)
    labelOtherName.grid(column=0, row=2, sticky=W,
                        padx=padx, pady=pady, columnspan=2)

    entryOtherName = tkinter.Entry(
        f_all_add_person, font=font_content, width=40)
    entryOtherName.grid(column=2, row=2, padx=padx, pady=pady, columnspan=2)

    # row 3
    labelBirthDay = tkinter.Label(
        f_all_add_person, text="Ngày sinh: ", font=font_content, anchor=W)
    labelBirthDay.grid(column=0, row=3, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    dateEntryBirthDay = DateEntry(f_all_add_person, font=font_content)
    dateEntryBirthDay.grid(column=1, row=3, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

    labelGender = tkinter.Label(
        f_all_add_person, text="Giới tính: ", font=font_content, anchor=W)
    labelGender.grid(column=2, row=3, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    option = ("Male", "Female", "Other")
    chosed = StringVar(f_all_add_person)

    dropDownGender = ttk.OptionMenu(
        f_all_add_person, chosed, option[0], *option, style='DropDownStyle.TMenubutton')
    dropDownGender['menu'].configure(font=('Arial', 12))
    dropDownGender.grid(column=3, row=3, sticky=W,
                        padx=padx, pady=pady, columnspan=1)

    # row 4
    labelRealAddress = tkinter.Label(
        f_all_add_person, text="Nguyên quán: ", font=font_content, anchor=W)
    labelRealAddress.grid(column=0, row=4, sticky=W,
                          padx=padx, pady=pady, columnspan=1)

    entryRealAddress = tkinter.Entry(
        f_all_add_person, font=font_content, width=60)
    entryRealAddress.grid(column=1, row=4, sticky=W,
                          padx=padx, pady=pady, columnspan=3)

    # row 5
    labelCCCD = tkinter.Label(
        f_all_add_person, text="Số căn cước công dân: ", anchor=W, font=font_content)
    labelCCCD.grid(column=0, row=5, padx=padx,
                   pady=pady, sticky=W, columnspan=2)

    entryCCCD = tkinter.Entry(f_all_add_person, font=font_content, width=40)
    entryCCCD.grid(column=2, row=5, padx=padx,
                   pady=pady, sticky=W, columnspan=2)

    # row 6
    labelEthnic = tkinter.Label(
        f_all_add_person, text="Dân tộc: ", font=font_content, anchor=W)
    labelEthnic.grid(column=0, row=6, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    entryEthnic = tkinter.Entry(f_all_add_person, font=font_content, width=20)
    entryEthnic.grid(column=1, row=6, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    labelNationality = tkinter.Label(
        f_all_add_person, text="Quốc tịch: ", font=font_content, anchor=W)
    labelNationality.grid(column=2, row=6, sticky=W,
                          padx=padx, pady=pady, columnspan=1)
    entryNationality = tkinter.Entry(
        f_all_add_person, font=font_content, width=20)
    entryNationality.grid(column=3, row=6, sticky=W,
                          padx=padx, pady=pady, columnspan=1)

    # row 7
    labelJob = tkinter.Label(
        f_all_add_person, text="Nghề nghiệp, nơi làm việc: ", font=font_content, anchor=W)
    labelJob.grid(column=0, row=7, sticky=W,
                  padx=padx, pady=pady, columnspan=2)

    entryJob = tkinter.Entry(f_all_add_person, font=font_content, width=40)
    entryJob.grid(column=2, row=7, padx=padx, pady=pady, columnspan=2)

    # row 8
    labelCurrentAddress = tkinter.Label(
        f_all_add_person, text="Nơi thường trú trước khi chuyển đến:", font=font_content, anchor=W)
    labelCurrentAddress.grid(column=0, row=8, sticky=W,
                             padx=padx, pady=pady, columnspan=2)

    entryCurrentAddress = tkinter.Entry(
        f_all_add_person, font=font_content, width=40)
    entryCurrentAddress.grid(
        column=2, row=8, padx=padx, pady=pady, columnspan=2)

    # row 9
    labelCurrentDate = tkinter.Label(
        f_all_add_person, text="Hôm nay: ", font=font_content, anchor=W)
    labelCurrentDate.grid(column=0, row=9, sticky=W,
                          padx=padx, pady=pady, columnspan=1)

    dateEntryCurrentDate = DateEntry(f_all_add_person, font=font_content)
    dateEntryCurrentDate.grid(column=1, row=9, sticky=W,
                              padx=padx, pady=pady, columnspan=1)

    def submit():
        datas = (
            entryRelationShip.get(),
            entryFullName.get(),
            entryOtherName.get(),
            dateEntryBirthDay.get_date().strftime("%m/%d/%y"),
            chosed.get(),
            entryRealAddress.get(),
            entryCCCD.get(),
            entryEthnic.get(),
            entryNationality.get(),
            entryJob.get(),
            entryCurrentAddress.get(),
            dateEntryCurrentDate.get_date().strftime("%m/%d/%y"),
            hostId
        )
        connectDB.InsertTable(datas)
        switch(f_home)

    # row 10
    buttonSubmit = tkinter.Button(
        f_all_add_person, text="Gửi", font=font_content, relief="groove", cursor='hand2', command=submit)
    buttonSubmit.grid(column=0, row=10, padx=padx, pady=pady, columnspan=4)


"""End thêm nhân khẩu"""
# ---------------------------------------------------------------------------------------------------------------------------------------
"""Start sửa thông tin"""


def AuthenFixInfo():
    # Create a child frame to destroy when no use parent frame
    f_all_authen_fix_info = tkinter.Frame(f_authen_fix_info)
    f_authen_fix_info.grid_columnconfigure(0, weight=1)
    f_authen_fix_info.grid_rowconfigure(0, weight=1)
    f_all_authen_fix_info.grid(column=0, row=0, sticky='news')
    f_all_authen_fix_info.config(padx=10, pady=30)
    labelCCCD = tkinter.Label(
        f_all_authen_fix_info, text="Nhập CCCD:", font=font_content, anchor=W)
    labelCCCD.grid(column=0, row=0, sticky=W,
                   padx=padx, pady=pady, columnspan=1)
    entryCCCD = tkinter.Entry(
        f_all_authen_fix_info, font=font_content, width=20)
    entryCCCD.grid(column=1, row=0, sticky=W,
                   padx=padx, pady=pady, columnspan=1)

    buttonSubmit = tkinter.Button(
        f_all_authen_fix_info, text="Gửi", font=font_content, relief='groove', cursor='hand2', command=lambda: AuthenticationFixInfo(entryCCCD.get(), labelMessage))
    buttonSubmit.grid(column=0, row=1, padx=padx, pady=pady, columnspan=2)

    labelMessage = tkinter.Label(
        f_all_authen_fix_info, text="", font=font_content, fg="red", anchor=W)
    labelMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)


def FixInfo(CCCD):
    datas = connectDB.getPerson(CCCD)[0]
    # Create a child frame to destroy when no use parent frame
    f_all_fix_info = tkinter.Frame(
        f_fix_info, highlightbackground="black", highlightthickness=2)
    f_fix_info.grid_columnconfigure(0, weight=1)
    f_fix_info.grid_rowconfigure(0, weight=1)
    f_all_fix_info.grid(column=0, row=0, sticky='news', padx=20, pady=20)

    f_all_fix_info.grid_columnconfigure(0, weight=1)

    # row 0
    labelRelationShip = tkinter.Label(f_all_fix_info, text="Quan hệ với chủ hộ:",
                                      font=font_header3, anchor=W)
    labelRelationShip.grid(row=0, column=0, columnspan=2,
                           padx=padx, pady=pady, sticky=W)
    entryRelationShip = tkinter.Entry(
        f_all_fix_info, font=font_content, width=40)
    entryRelationShip.grid(row=0, column=2, padx=padx,
                           pady=pady, sticky=W, columnspan=2)
    entryRelationShip.insert(0, datas[0])

    # row 1
    labelFullName = tkinter.Label(
        f_all_fix_info, text="Họ và tên: ", font=font_content, anchor=W)
    labelFullName.grid(column=0, row=1, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    entryFullName = tkinter.Entry(
        f_all_fix_info, font=font_content, width=60)
    entryFullName.grid(column=1, row=1, padx=padx, pady=pady, columnspan=3)
    entryFullName.insert(0, datas[1])
    # row 2
    labelOtherName = tkinter.Label(
        f_all_fix_info, text="Họ và tên gọi khác(Nếu có): ", font=font_content, anchor=W)
    labelOtherName.grid(column=0, row=2, sticky=W,
                        padx=padx, pady=pady, columnspan=2)

    entryOtherName = tkinter.Entry(
        f_all_fix_info, font=font_content, width=40)
    entryOtherName.grid(column=2, row=2, padx=padx, pady=pady, columnspan=2)
    entryOtherName.insert(0, datas[2])
    # row 3
    date = datas[3].split("-")
    labelBirthDay = tkinter.Label(
        f_all_fix_info, text="Ngày sinh: ", font=font_content,  anchor=W)
    labelBirthDay.grid(column=0, row=3, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    dateEntryBirthDay = DateEntry(
        f_all_fix_info, font=font_content, month=int(date[0]), day=int(date[1]), year=int(date[2]),)
    dateEntryBirthDay.grid(column=1, row=3, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

    # --------------------------
    labelGender = tkinter.Label(
        f_all_fix_info, text="Giới tính: ", font=font_content, anchor=W)
    labelGender.grid(column=2, row=3, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    option = ("Male", "Female",  "Other")
    chosed = StringVar(f_all_fix_info)
    # (frame, biến chọn, default, option, style)
    dropDownGender = ttk.OptionMenu(
        f_all_fix_info, chosed, datas[4], *option, style='DropDownStyle.TMenubutton')
    dropDownGender['menu'].configure(font=('Arial', 12))
    dropDownGender.grid(column=3, row=3, sticky=W,
                        padx=padx, pady=pady, columnspan=1)

    # row 4
    labelRealAddress = tkinter.Label(
        f_all_fix_info, text="Nguyên quán: ", font=font_content, anchor=W)
    labelRealAddress.grid(column=0, row=4, sticky=W,
                          padx=padx, pady=pady, columnspan=1)

    entryRealAddress = tkinter.Entry(
        f_all_fix_info, font=font_content, width=60)
    entryRealAddress.grid(column=1, row=4, sticky=W,
                          padx=padx, pady=pady, columnspan=3)
    entryRealAddress.insert(0, datas[5])
    # row 5
    labelCCCD = tkinter.Label(
        f_all_fix_info, text="Số căn cước công dân: ", anchor=W, font=font_content)
    labelCCCD.grid(column=0, row=5, padx=padx,
                   pady=pady, sticky=W, columnspan=2)

    entryCCCD = tkinter.Entry(f_all_fix_info, font=font_content, width=40)
    entryCCCD.grid(column=2, row=5, padx=padx,
                   pady=pady, sticky=W, columnspan=2)
    entryCCCD.insert(0, datas[6])
    # row 6
    labelEthnic = tkinter.Label(
        f_all_fix_info, text="Dân tộc: ", font=font_content, anchor=W)
    labelEthnic.grid(column=0, row=6, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    entryEthnic = tkinter.Entry(f_all_fix_info, font=font_content, width=20)
    entryEthnic.grid(column=1, row=6, sticky=W,
                     padx=padx, pady=pady, columnspan=1)
    entryEthnic.insert(0, datas[7])
    # -----------------------
    labelNationality = tkinter.Label(
        f_all_fix_info, text="Quốc tịch: ", font=font_content, anchor=W)
    labelNationality.grid(column=2, row=6, sticky=W,
                          padx=padx, pady=pady, columnspan=1)
    entryNationality = tkinter.Entry(
        f_all_fix_info, font=font_content, width=20)
    entryNationality.grid(column=3, row=6, sticky=W,
                          padx=padx, pady=pady, columnspan=1)
    entryNationality.insert(0, datas[8])
    # row 7
    labelJob = tkinter.Label(
        f_all_fix_info, text="Nghề nghiệp, nơi làm việc: ", font=font_content, anchor=W)
    labelJob.grid(column=0, row=7, sticky=W,
                  padx=padx, pady=pady, columnspan=2)

    entryJob = tkinter.Entry(f_all_fix_info, font=font_content, width=40)
    entryJob.grid(column=2, row=7, padx=padx, pady=pady, columnspan=2)
    entryJob.insert(0, datas[9])
    # row 8
    labelCurrentAddress = tkinter.Label(
        f_all_fix_info, text="Nơi thường trú trước khi chuyển đến:", font=font_content, anchor=W)
    labelCurrentAddress.grid(column=0, row=8, sticky=W,
                             padx=padx, pady=pady, columnspan=2)

    entryCurrentAddress = tkinter.Entry(
        f_all_fix_info, font=font_content, width=40)
    entryCurrentAddress.grid(
        column=2, row=8, padx=padx, pady=pady, columnspan=2)
    entryCurrentAddress.insert(0, datas[10])
    # row 9
    labelCurrentDate = tkinter.Label(
        f_all_fix_info, text="Hôm nay: ", font=font_content, anchor=W)
    labelCurrentDate.grid(column=0, row=9, sticky=W,
                          padx=padx, pady=pady, columnspan=1)

    dateEntryCurrentDate = DateEntry(f_all_fix_info, font=font_content)
    dateEntryCurrentDate.grid(column=1, row=9, sticky=W,
                              padx=padx, pady=pady, columnspan=1)

    def submit():
        datas = (
            entryRelationShip.get(),
            entryFullName.get(),
            entryOtherName.get(),
            dateEntryBirthDay.get_date().strftime("%m/%d/%y"),
            chosed.get(),
            entryRealAddress.get(),
            entryCCCD.get(),
            entryEthnic.get(),
            entryNationality.get(),
            entryJob.get(),
            entryCurrentAddress.get(),
            dateEntryCurrentDate.get_date().strftime("%m/%d/%y"),
            CCCD
            # hostId
        )
        connectDB.UpdateTableCUDAN(datas)
        switch(f_home)

    # row 10
    buttonSubmit = tkinter.Button(
        f_all_fix_info, text="Gửi", font=font_content, relief="groove", cursor='hand2', command=submit)
    buttonSubmit.grid(column=0, row=10, padx=padx, pady=pady, columnspan=4)

    '''
    Get số hộ khẩu và CCCD => CHECK 
    => XUẤT HIỆN THÔNG TIN (GIỐNG THÊM NHÂN KHẨU)
    '''


"""End sửa thông tin"""
# ------------------------------------------------------------------------------------------------------------------------------------------
"""Start sửa chủ hộ"""


def ChangeHostPerson(hostId):
    # Create a child frame to destroy when no use parent frame
    f_all_change_host_person = tkinter.Frame(
        f_change_host_person, highlightbackground="black", highlightthickness=2)
    f_change_host_person.grid_columnconfigure(0, weight=1)
    f_change_host_person.grid_rowconfigure(0, weight=1)
    f_all_change_host_person.grid(
        column=0, row=0, sticky='news', padx=20, pady=20)

    f_all_change_host_person.grid_columnconfigure(0, weight=1)

    tkinter.Label(f_all_change_host_person, text="Change Host",
                  font=font_content).grid(column=0, row=0)


"""End sửa chủ hộ"""
# -------------------------------------------------------------------------------------------------------------------------------------
"""Start xem thông tin cá nhân"""


def AuthenViewMyInfo():
    # Create a child frame to destroy when no use parent frame
    f_all_authen_my_info = tkinter.Frame(f_authen_view_my_info)
    f_authen_view_my_info.grid_columnconfigure(0, weight=1)
    f_authen_view_my_info.grid_rowconfigure(0, weight=1)
    f_all_authen_my_info.grid(column=0, row=0, sticky='news')
    f_all_authen_my_info.config(padx=10, pady=30)
    labelCCCD = tkinter.Label(
        f_all_authen_my_info, text="Nhập CCCD:", font=font_content, anchor=W)
    labelCCCD.grid(column=0, row=0, sticky=W,
                   padx=padx, pady=pady, columnspan=1)
    entryCCCD = tkinter.Entry(
        f_all_authen_my_info, font=font_content, width=20)
    entryCCCD.grid(column=1, row=0, sticky=W,
                   padx=padx, pady=pady, columnspan=1)

    buttonSubmit = tkinter.Button(
        f_all_authen_my_info, text="Gửi", font=font_content, relief='groove', cursor='hand2', command=lambda: AuthenticationViewMyInfo(entryCCCD.get(), labelMessage))
    buttonSubmit.grid(column=0, row=1, padx=padx, pady=pady, columnspan=2)

    labelMessage = tkinter.Label(
        f_all_authen_my_info, text="", font=font_content, fg="red", anchor=W)
    labelMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)


def ViewMyInfo(CCCD):
    datas = connectDB.getCUDAN(CCCD)[0]
    # Create a child frame to destroy when no use parent frame
    f_all_view_my_info = tkinter.Frame(
        f_view_my_info, highlightbackground="black", highlightthickness=2)
    f_view_my_info.grid_columnconfigure(0, weight=1)
    f_view_my_info.grid_rowconfigure(0, weight=1)
    f_all_view_my_info.grid(
        column=0, row=0, sticky='news', padx=50, pady=20)

    f_all_view_my_info.grid_columnconfigure(4, weight=1)

    # row 0
    labelRelationShip = tkinter.Label(f_all_view_my_info, text="Quan hệ với chủ hộ:",
                                      font=font_header3, anchor=W)
    labelRelationShip.grid(row=0, column=0, columnspan=2,
                           padx=padx, pady=pady, sticky=W)
    labelShowRelationShip = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[0], font=font_content)
    labelShowRelationShip.grid(row=0, column=2, padx=padx,
                               pady=pady, sticky=W, columnspan=2)

    # row 1
    labelFullName = tkinter.Label(
        f_all_view_my_info, text="Họ và tên: ", font=font_content, anchor=W)
    labelFullName.grid(column=0, row=1, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    labelShowFullName = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[1], font=font_content)
    labelShowFullName.grid(column=1, row=1, padx=padx,
                           pady=pady, columnspan=3, sticky=W)

    # row 2
    labelOtherName = tkinter.Label(
        f_all_view_my_info, text="Họ và tên gọi khác(Nếu có): ", font=font_content, anchor=W)
    labelOtherName.grid(column=0, row=2, sticky=W,
                        padx=padx, pady=pady, columnspan=2)

    labelShowOtherName = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[2], font=font_content)
    labelShowOtherName.grid(column=2, row=2, padx=padx,
                            pady=pady, columnspan=2, sticky=W)

    # row 3
    labelBirthDay = tkinter.Label(
        f_all_view_my_info, text="Ngày sinh: ", font=font_content, anchor=W)
    labelBirthDay.grid(column=0, row=3, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    labelShowBirthDay = Label(
        f_all_view_my_info, anchor=W, text=datas[3], font=font_content)
    labelShowBirthDay.grid(column=1, row=3, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

    labelGender = tkinter.Label(
        f_all_view_my_info, text="Giới tính: ", font=font_content, anchor=W)
    labelGender.grid(column=2, row=3, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    labelShowGender = Label(
        f_all_view_my_info, anchor=W, text=datas[4], font=font_content)
    labelShowGender.grid(column=3, row=3, sticky=W,
                         padx=padx, pady=pady, columnspan=1)

    # row 4
    labelRealAddress = tkinter.Label(
        f_all_view_my_info, text="Nguyên quán: ", font=font_content, anchor=W)
    labelRealAddress.grid(column=0, row=4, sticky=W,
                          padx=padx, pady=pady, columnspan=1)

    labelShowRealAddress = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[5], font=font_content)
    labelShowRealAddress.grid(column=1, row=4, sticky=W,
                              padx=padx, pady=pady, columnspan=3)

    # row 5
    labelCCCD = tkinter.Label(
        f_all_view_my_info, text="Số căn cước công dân: ", anchor=W, font=font_content)
    labelCCCD.grid(column=0, row=5, padx=padx,
                   pady=pady, sticky=W, columnspan=2)

    labelShowCCCD = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[6], font=font_content)
    labelShowCCCD.grid(column=2, row=5, padx=padx,
                       pady=pady, sticky=W, columnspan=2)

    # row 6
    labelEthnic = tkinter.Label(
        f_all_view_my_info, text="Dân tộc: ", font=font_content, anchor=W)
    labelEthnic.grid(column=0, row=6, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    labelShowEthnic = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[7], font=font_content)
    labelShowEthnic.grid(column=1, row=6, sticky=W,
                         padx=padx, pady=pady, columnspan=1)

    labelNationality = tkinter.Label(
        f_all_view_my_info, text="Quốc tịch: ", font=font_content, anchor=W)
    labelNationality.grid(column=2, row=6, sticky=W,
                          padx=padx, pady=pady, columnspan=1)
    labelShowNationality = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[8], font=font_content)
    labelShowNationality.grid(column=3, row=6, sticky=W,
                              padx=padx, pady=pady, columnspan=1)

    # row 7
    labelJob = tkinter.Label(
        f_all_view_my_info, text="Nghề nghiệp, nơi làm việc: ", font=font_content, anchor=W)
    labelJob.grid(column=0, row=7, sticky=W,
                  padx=padx, pady=pady, columnspan=2)

    labelShowJob = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[9], font=font_content)
    labelShowJob.grid(column=2, row=7, padx=padx,
                      pady=pady, columnspan=2, sticky=W)

    # row 8
    labelCurrentAddress = tkinter.Label(
        f_all_view_my_info, text="Nơi thường trú trước khi chuyển đến:", font=font_content, anchor=W)
    labelCurrentAddress.grid(column=0, row=8, sticky=W,
                             padx=padx, pady=pady, columnspan=2)

    labelShowCurrentAddress = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[10], font=font_content)
    labelShowCurrentAddress.grid(
        column=2, row=8, padx=padx, pady=pady, columnspan=2, sticky=W)
    # row 9
    labelHoKhauId = tkinter.Label(
        f_all_view_my_info, text="Số Hộ Khẩu: ", font=font_content, anchor=W)
    labelHoKhauId.grid(column=0, row=4, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    labelShowHoKhauId = tkinter.Label(
        f_all_view_my_info, anchor=W, text=datas[11], font=font_content)
    labelShowHoKhauId.grid(column=1, row=4, sticky=W,
                           padx=padx, pady=pady, columnspan=3)


"""End xem thông tin cá nhân"""
# --------------------------------------------------------------------------------------------------------------------------------------------


def AuthenTachKhau():
    # Create a child frame to destroy when no use parent frame
    f_all_authen_tach_khau = tkinter.Frame(f_authen_tach_khau)
    f_authen_tach_khau.grid_columnconfigure(0, weight=1)
    f_authen_tach_khau.grid_rowconfigure(0, weight=1)
    f_all_authen_tach_khau.grid(column=0, row=0, sticky='news')
    f_all_authen_tach_khau.config(padx=10, pady=30)
    labelHostId = tkinter.Label(
        f_all_authen_tach_khau, text="Nhập mã hộ khẩu", font=font_content, anchor=W)
    labelHostId.grid(column=0, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)
    entryHostId = tkinter.Entry(
        f_all_authen_tach_khau, font=font_content, width=20)
    entryHostId.grid(column=1, row=0, sticky=W,
                     padx=padx, pady=pady, columnspan=1)

    buttonSubmit = tkinter.Button(
        f_all_authen_tach_khau, text="Gửi", font=font_content, relief='groove', cursor='hand2', command=lambda: AuthenticationTachKhau(entryHostId.get(), labelMessage))
    buttonSubmit.grid(column=0, row=1, padx=padx, pady=pady, columnspan=2)

    labelMessage = tkinter.Label(
        f_all_authen_tach_khau, text="", font=font_content, fg="red", anchor=W)
    labelMessage.grid(column=0, row=2, padx=padx,
                      pady=pady, sticky=W, columnspan=2)


def TachKhau(hostId):
    datas = connectDB.getHoKhau(hostId)
    n = len(datas)

    # Create a child frame to destroy when no use parent frame
    f_all_tach_khau = tkinter.Frame(
        f_tach_khau, highlightbackground="black", highlightthickness=2)
    f_tach_khau.grid_columnconfigure(0, weight=1)
    f_tach_khau.grid_rowconfigure(0, weight=1)
    f_all_tach_khau.grid(
        column=0, row=0, sticky='news', padx=50, pady=20)

    f_all_tach_khau.grid_columnconfigure(4, weight=1)

    def showDetail(i):
        if (n == 0):
            f_all_tach_khau.grid_columnconfigure(0, weight=1)
            f_all_tach_khau.grid_rowconfigure(0, weight=1)
            f_all_tach_khau.grid_columnconfigure(4, weight=0)

            tkinter.Label(f_all_tach_khau, text="Không có data", fg="red",
                          font=font_header1).grid(column=0, row=0)
        else:
            if (i <= 0):
                i = 0
            elif (i >= n-1):
                i = n-1
            for widget in f_all_tach_khau.winfo_children():
                widget.destroy()
            Detail(i)

    def Detail(i):
        # row 0
        labelRelationShip = tkinter.Label(f_all_tach_khau, text="Quan hệ với chủ hộ:",
                                          font=font_header3, anchor=W)
        labelRelationShip.grid(row=0, column=0, columnspan=2,
                               padx=padx, pady=pady, sticky=W)
        labelShowRelationShip = tkinter.Label(
            f_all_tach_khau, anchor=W, text=datas[i][0], font=font_content)
        labelShowRelationShip.grid(row=0, column=2, padx=padx,
                                   pady=pady, sticky=W, columnspan=2)

        # row 1
        labelFullName = tkinter.Label(
            f_all_tach_khau, text="Họ và tên: ", font=font_content, anchor=W)
        labelFullName.grid(column=0, row=1, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

        labelShowFullName = tkinter.Label(
            f_all_tach_khau, anchor=W, text=datas[i][1], font=font_content)
        labelShowFullName.grid(column=1, row=1, padx=padx,
                               pady=pady, columnspan=3, sticky=W)

        # row 2
        labelOtherName = tkinter.Label(
            f_all_tach_khau, text="Họ và tên gọi khác(Nếu có): ", font=font_content, anchor=W)
        labelOtherName.grid(column=0, row=2, sticky=W,
                            padx=padx, pady=pady, columnspan=2)

        labelShowOtherName = tkinter.Label(
            f_all_tach_khau, anchor=W, text=datas[i][2], font=font_content)
        labelShowOtherName.grid(column=2, row=2, padx=padx,
                                pady=pady, columnspan=2, sticky=W)

        # row 3
        labelBirthDay = tkinter.Label(
            f_all_tach_khau, text="Ngày sinh: ", font=font_content, anchor=W)
        labelBirthDay.grid(column=0, row=3, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

        labelShowBirthDay = Label(
            f_all_tach_khau, anchor=W, text=datas[i][3], font=font_content)
        labelShowBirthDay.grid(column=1, row=3, sticky=W,
                               padx=padx, pady=pady, columnspan=1)

        labelGender = tkinter.Label(
            f_all_tach_khau, text="Giới tính: ", font=font_content, anchor=W)
        labelGender.grid(column=2, row=3, sticky=W,
                         padx=padx, pady=pady, columnspan=1)

        labelShowGender = Label(
            f_all_tach_khau, anchor=W, text=datas[i][4], font=font_content)
        labelShowGender.grid(column=3, row=3, sticky=W,
                             padx=padx, pady=pady, columnspan=1)

        # row 4
        labelRealAddress = tkinter.Label(
            f_all_tach_khau, text="Nguyên quán: ", font=font_content, anchor=W)
        labelRealAddress.grid(column=0, row=4, sticky=W,
                              padx=padx, pady=pady, columnspan=1)

        labelShowRealAddress = tkinter.Label(
            f_all_tach_khau, anchor=W, text=datas[i][5], font=font_content)
        labelShowRealAddress.grid(column=1, row=4, sticky=W,
                                  padx=padx, pady=pady, columnspan=3)

        # row 5
        labelCCCD = tkinter.Label(
            f_all_tach_khau, text="Số căn cước công dân: ", anchor=W, font=font_content)
        labelCCCD.grid(column=0, row=5, padx=padx,
                       pady=pady, sticky=W, columnspan=2)

        labelShowCCCD = tkinter.Label(
            f_all_tach_khau, anchor=W, text=datas[i][6], font=font_content)
        labelShowCCCD.grid(column=2, row=5, padx=padx,
                           pady=pady, sticky=W, columnspan=2)

        # row 6
        labelEthnic = tkinter.Label(
            f_all_tach_khau, text="Dân tộc: ", font=font_content, anchor=W)
        labelEthnic.grid(column=0, row=6, sticky=W,
                         padx=padx, pady=pady, columnspan=1)

        labelShowEthnic = tkinter.Label(
            f_all_tach_khau, anchor=W, text=datas[i][7], font=font_content)
        labelShowEthnic.grid(column=1, row=6, sticky=W,
                             padx=padx, pady=pady, columnspan=1)

        labelNationality = tkinter.Label(
            f_all_tach_khau, text="Quốc tịch: ", font=font_content, anchor=W)
        labelNationality.grid(column=2, row=6, sticky=W,
                              padx=padx, pady=pady, columnspan=1)
        labelShowNationality = tkinter.Label(
            f_all_tach_khau, anchor=W, text=datas[i][8], font=font_content)
        labelShowNationality.grid(column=3, row=6, sticky=W,
                                  padx=padx, pady=pady, columnspan=1)

        # row 7
        labelJob = tkinter.Label(
            f_all_tach_khau, text="Nghề nghiệp, nơi làm việc: ", font=font_content, anchor=W)
        labelJob.grid(column=0, row=7, sticky=W,
                      padx=padx, pady=pady, columnspan=2)

        labelShowJob = tkinter.Label(
            f_all_tach_khau, anchor=W, text=datas[i][9], font=font_content)
        labelShowJob.grid(column=2, row=7, padx=padx,
                          pady=pady, columnspan=2, sticky=W)

        # row 8
        labelCurrentAddress = tkinter.Label(
            f_all_tach_khau, text="Nơi thường trú trước khi chuyển đến:", font=font_content, anchor=W)
        labelCurrentAddress.grid(column=0, row=8, sticky=W,
                                 padx=padx, pady=pady, columnspan=2)

        labelShowCurrentAddress = tkinter.Label(
            f_all_tach_khau, anchor=W, text=datas[i][10], font=font_content)
        labelShowCurrentAddress.grid(
            column=2, row=8, padx=padx, pady=pady, columnspan=2, sticky=W)

        # row 9
        var = tkinter.IntVar()
        labelAccept = tkinter.Label(
            f_all_tach_khau, text="Quan hệ mới:", font=font_content, anchor=W)
        entryAccept = tkinter.Entry(f_all_tach_khau, font=font_content,
                                    width=20)

        def showEntry():
            if (var.get() == 1):
                entryAccept.grid(column=2, row=10, columnspan=1)
                labelAccept.grid(column=1, row=10, columnspan=1)
            else:
                entryAccept.grid_remove()
                labelAccept.grid_remove()
        acceptTacKhau = tkinter.Checkbutton(f_all_tach_khau, text="Chọn để tách khẩu",
                                            font=font_content, cursor='hand2', variable=var, onvalue=1, offvalue=0, command=showEntry)
        acceptTacKhau.grid(column=0, row=9, columnspan=4)

        # row 10
        buttonPrePage = tkinter.Button(
            f_all_tach_khau, text="Trang trước", font=font_content, relief="groove", cursor='hand2', command=lambda: showDetail(i-1))
        buttonPrePage.grid(column=0, row=10, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

        buttonAfterPage = tkinter.Button(
            f_all_tach_khau, text="Trang sau", font=font_content, relief="groove", cursor='hand2', command=lambda: showDetail(i+1))
        buttonAfterPage.grid(column=4, row=10, sticky=E,
                             padx=padx, pady=pady, columnspan=1)

    showDetail(0)
# ---------------------------------------------------------------------------------------------------------------------------------------------


def TamTru():
    # Create a child frame to destroy when no use parent frame
    f_all_tam_tru = tkinter.Frame(
        f_tam_tru, highlightbackground="black", highlightthickness=2)
    f_tam_tru.grid_columnconfigure(0, weight=1)
    f_tam_tru.grid_rowconfigure(0, weight=1)
    f_all_tam_tru.grid(column=0, row=0, sticky='news', padx=20, pady=10)

    f_all_tam_tru.grid_columnconfigure(0, weight=1)
    # row 0
    tkinter.Label(f_all_tam_tru, text="Đơn xin tạm trú", font=font_header1).grid(
        column=0, row=0, padx=padx, pady=0, columnspan=4)
    # row 1
    tkinter.Label(f_all_tam_tru, text="Kính gửi: ", font=font_content, anchor=W).grid(
        column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    # row 2
    tkinter.Label(f_all_tam_tru, text="Công an quận:", font=font_content, anchor=W).grid(
        column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryPoliceQuan = tkinter.Entry(f_all_tam_tru, font=font_content, width=60)
    entryPoliceQuan.grid(column=1, row=2, sticky=W,
                         padx=padx, pady=pady, columnspan=3)
    # row 3
    tkinter.Label(f_all_tam_tru, text="Công an phường:", font=font_content, anchor=W).grid(
        column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryPolicePhuong = tkinter.Entry(
        f_all_tam_tru, font=font_content, width=60)
    entryPolicePhuong.grid(column=1, row=3, sticky=W,
                           padx=padx, pady=pady, columnspan=3)
    # row 4
    tkinter.Label(f_all_tam_tru, text="Tên tôi là:", font=font_content, anchor=W).grid(
        column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryFullName = tkinter.Entry(f_all_tam_tru, font=font_content, width=60)
    entryFullName.grid(column=1, row=4, sticky=W,
                       padx=padx, pady=pady, columnspan=3)
    # row 5
    tkinter.Label(f_all_tam_tru, text="Ngày sinh: ", font=font_content, anchor=W).grid(
        column=0, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    dateEntryBirthDay = DateEntry(f_all_tam_tru, font=font_content)
    dateEntryBirthDay.grid(column=1, row=5, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

    # row 6
    tkinter.Label(f_all_tam_tru, text="Quê quán:", font=font_content, anchor=W).grid(
        column=0, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryOldAddress = tkinter.Entry(f_all_tam_tru, font=font_content, width=60)
    entryOldAddress.grid(column=1, row=6, sticky=W,
                         padx=padx, pady=pady, columnspan=3)

    # row 7
    tkinter.Label(f_all_tam_tru, text="Số CCCD:", font=font_content, anchor=W).grid(
        column=0, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryCCCD = tkinter.Entry(f_all_tam_tru, font=font_content, width=20)
    entryCCCD.grid(column=1, row=7, sticky=W,
                   padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_tam_tru, text="Ngày cấp:", font=font_content, anchor=W).grid(
        column=2, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)
    dateEntryCCCD = tkinter.Entry(f_all_tam_tru, font=font_content, width=20)
    dateEntryCCCD.grid(column=3, row=7, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    # row 8
    tkinter.Label(f_all_tam_tru, text="Nơi cấp:", font=font_content, anchor=W).grid(
        column=0, row=8, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryAddressCCCD = tkinter.Entry(
        f_all_tam_tru, font=font_content, width=60)
    entryAddressCCCD.grid(column=1, row=8, sticky=W,
                          padx=padx, pady=pady, columnspan=3)

    # row 9
    tkinter.Label(f_all_tam_tru, text="Xin thường trú tại:", font=font_content, anchor=W).grid(
        column=0, row=9, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryCurrentAddress = tkinter.Entry(
        f_all_tam_tru, font=font_content, width=60)
    entryCurrentAddress.grid(column=1, row=9, sticky=W,
                             padx=padx, pady=pady, columnspan=3)

    # row 10
    tkinter.Label(f_all_tam_tru, text="Từ ngày: ", font=font_content, anchor=W).grid(
        column=0, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)

    dateDateFrom = DateEntry(f_all_tam_tru, font=font_content)
    dateDateFrom.grid(column=1, row=10, sticky=W,
                      padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_tam_tru, text="Đến ngày: ", font=font_content, anchor=W).grid(
        column=2, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)

    dateDateTo = DateEntry(f_all_tam_tru, font=font_content)
    dateDateTo.grid(column=3, row=10, sticky=W,
                    padx=padx, pady=pady, columnspan=1)

    # row 11
    tkinter.Label(f_all_tam_tru, text="Lý do:", font=font_content, anchor=W).grid(
        column=0, row=11, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryReason = tkinter.Text(
        f_all_tam_tru, font=font_content, width=60, height=3)
    entryReason.grid(column=1, row=11, sticky=W,
                     padx=padx, pady=pady, columnspan=3)

    # row 12
    tkinter.Label(f_all_tam_tru, text="Ngày làm đơn: ", font=font_content, anchor=W).grid(
        column=0, row=12, sticky=W, padx=padx, pady=pady, columnspan=1)

    dateCreateForm = DateEntry(f_all_tam_tru, font=font_content)
    dateCreateForm.grid(column=1, row=12, sticky=W,
                        padx=padx, pady=pady, columnspan=1)

    # row 13
    tkinter.Button(f_all_tam_tru, text="Xác nhận", font=font_content).grid(
        column=0, row=13, padx=padx, pady=pady, columnspan=4)

# --------------------------------------------------------------------------------------------------------------------------------------------


def TamVang():
    # Create a child frame to destroy when no use parent frame
    f_all_tam_vang = tkinter.Frame(
        f_tam_vang, highlightbackground="black", highlightthickness=2)
    f_tam_vang.grid_columnconfigure(0, weight=1)
    f_tam_vang.grid_rowconfigure(0, weight=1)
    f_all_tam_vang.grid(column=0, row=0, sticky='news', padx=20, pady=20)

    f_all_tam_vang.grid_columnconfigure(0, weight=1)

    # row 0
    tkinter.Label(f_all_tam_vang, text="Đơn xin tạm vắng", font=font_header1).grid(
        column=0, row=0, padx=padx, pady=0, columnspan=4)
    # row 1
    tkinter.Label(f_all_tam_vang, text="Kính gửi: ", font=font_content, anchor=W).grid(
        column=0, row=1, sticky=W, padx=padx, pady=pady, columnspan=1)
    # row 2
    tkinter.Label(f_all_tam_vang, text="Công an quận:", font=font_content, anchor=W).grid(
        column=0, row=2, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryPoliceQuan = tkinter.Entry(
        f_all_tam_vang, font=font_content, width=60)
    entryPoliceQuan.grid(column=1, row=2, sticky=W,
                         padx=padx, pady=pady, columnspan=3)
    # row 3
    tkinter.Label(f_all_tam_vang, text="Công an phường:", font=font_content, anchor=W).grid(
        column=0, row=3, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryPolicePhuong = tkinter.Entry(
        f_all_tam_vang, font=font_content, width=60)
    entryPolicePhuong.grid(column=1, row=3, sticky=W,
                           padx=padx, pady=pady, columnspan=3)
    # row 4
    tkinter.Label(f_all_tam_vang, text="Tên tôi là:", font=font_content, anchor=W).grid(
        column=0, row=4, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryFullName = tkinter.Entry(f_all_tam_vang, font=font_content, width=60)
    entryFullName.grid(column=1, row=4, sticky=W,
                       padx=padx, pady=pady, columnspan=3)
    # row 5
    tkinter.Label(f_all_tam_vang, text="Ngày sinh: ", font=font_content, anchor=W).grid(
        column=0, row=5, sticky=W, padx=padx, pady=pady, columnspan=1)

    dateEntryBirthDay = DateEntry(f_all_tam_vang, font=font_content)
    dateEntryBirthDay.grid(column=1, row=5, sticky=W,
                           padx=padx, pady=pady, columnspan=1)

    # row 6
    tkinter.Label(f_all_tam_vang, text="Quê quán:", font=font_content, anchor=W).grid(
        column=0, row=6, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryOldAddress = tkinter.Entry(
        f_all_tam_vang, font=font_content, width=60)
    entryOldAddress.grid(column=1, row=6, sticky=W,
                         padx=padx, pady=pady, columnspan=3)

    # row 7
    tkinter.Label(f_all_tam_vang, text="Số CCCD:", font=font_content, anchor=W).grid(
        column=0, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryCCCD = tkinter.Entry(f_all_tam_vang, font=font_content, width=20)
    entryCCCD.grid(column=1, row=7, sticky=W,
                   padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_tam_vang, text="Ngày cấp:", font=font_content, anchor=W).grid(
        column=2, row=7, sticky=W, padx=padx, pady=pady, columnspan=1)
    dateEntryCCCD = tkinter.Entry(f_all_tam_vang, font=font_content, width=20)
    dateEntryCCCD.grid(column=3, row=7, sticky=W,
                       padx=padx, pady=pady, columnspan=1)

    # row 8
    tkinter.Label(f_all_tam_vang, text="Nơi cấp:", font=font_content, anchor=W).grid(
        column=0, row=8, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryAddressCCCD = tkinter.Entry(
        f_all_tam_vang, font=font_content, width=60)
    entryAddressCCCD.grid(column=1, row=8, sticky=W,
                          padx=padx, pady=pady, columnspan=3)

    # row 9
    tkinter.Label(f_all_tam_vang, text="Xin tạm vắng tại:", font=font_content, anchor=W).grid(
        column=0, row=9, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryCurrentAddress = tkinter.Entry(
        f_all_tam_vang, font=font_content, width=60)
    entryCurrentAddress.grid(column=1, row=9, sticky=W,
                             padx=padx, pady=pady, columnspan=3)

    # row 10
    tkinter.Label(f_all_tam_vang, text="Từ ngày: ", font=font_content, anchor=W).grid(
        column=0, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)

    dateDateFrom = DateEntry(f_all_tam_vang, font=font_content)
    dateDateFrom.grid(column=1, row=10, sticky=W,
                      padx=padx, pady=pady, columnspan=1)

    tkinter.Label(f_all_tam_vang, text="Đến ngày: ", font=font_content, anchor=W).grid(
        column=2, row=10, sticky=W, padx=padx, pady=pady, columnspan=1)

    dateDateTo = DateEntry(f_all_tam_vang, font=font_content)
    dateDateTo.grid(column=3, row=10, sticky=W,
                    padx=padx, pady=pady, columnspan=1)

    # row 11
    tkinter.Label(f_all_tam_vang, text="Lý do:", font=font_content, anchor=W).grid(
        column=0, row=11, sticky=W, padx=padx, pady=pady, columnspan=1)
    entryReason = tkinter.Text(
        f_all_tam_vang, font=font_content, width=60, height=3)
    entryReason.grid(column=1, row=11, sticky=W,
                     padx=padx, pady=pady, columnspan=3)

    # row 12
    tkinter.Label(f_all_tam_vang, text="Ngày làm đơn: ", font=font_content, anchor=W).grid(
        column=0, row=12, sticky=W, padx=padx, pady=pady, columnspan=1)

    dateCreateForm = DateEntry(f_all_tam_vang, font=font_content)
    dateCreateForm.grid(column=1, row=12, sticky=W,
                        padx=padx, pady=pady, columnspan=1)

    # row 13
    tkinter.Button(f_all_tam_vang, text="Xác nhận", font=font_content).grid(
        column=0, row=13, padx=padx, pady=pady, columnspan=4)


switch(f_home)

root. mainloop()
