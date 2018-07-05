import Find_All_Handler
import win32gui, win32api, win32con
import time
from gtools import *

def get_hwnd_child(fhwnd):
    hwndChildList = []
    win32gui.EnumChildWindows(fhwnd, lambda hwnd, param: param.append(hwnd), hwndChildList)
    return hwndChildList


main_handle = find_windows(title='东方财富终端')[0]
process = win32process.GetWindowThreadProcessId(main_handle)[1]
handles = find_windows(process=process, class_name='#32770', top_level_only=True, visible=True, title='')
print(handles)
handle = handles[0]
rect = win32gui.GetWindowRect(handle)
win32gui.MoveWindow(handle,0,0,rect[2]-rect[0],756,True)


