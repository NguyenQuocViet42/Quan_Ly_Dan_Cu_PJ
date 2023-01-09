from datetime import date
from tkinter import *
import tkinter
import os
from PIL import ImageTk, Image
'''
kiến nghị: demand
yêu cầu: request
phản hồi: response
'''
dirname = os.path.dirname(__file__)


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


# window
win_h = 700
win_w = 1000

win_bg = _from_rgb((255, 255, 255))
selected_bg = "lightblue"


# leftFrame_win


# rightFrame_win

# button
button_w = int(0.22*win_w)
button_h = int(0.2*button_w)

# response_demand
response_demand_bg = _from_rgb((230, 230, 230))

# Test
list_kien_nghi = [
    ["title1 dài hơn 20 ký tự ở đây, dàichhnef vẻ vẫn hơi ngắn",
        "conten1 conten1 conten1conten1conten1 conten1 conten1 conten1 conten1 conten1 conten1"],
    ["title2", "Nhập môn công nghệ phần mềm"]
]

map_weekday = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
map_month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December ",
}
today = date.today()
currentDate = map_weekday[today.weekday(
)]+", " + map_month[today.month] + str(today.day) + ", "+str(today.year)
