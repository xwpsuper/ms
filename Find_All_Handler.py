import win32gui


#生成一级子句柄列表
def get_hwnd_child(fhwnd):
    hwndChildList = []
    win32gui.EnumChildWindows(fhwnd, lambda hwnd, param: param.append(hwnd), hwndChildList)
    return hwndChildList

root_handler = get_hwnd_child(0)

#生成父句柄下的所有子句柄
def search_allchwnd(hwnd=0):
    L = get_hwnd_child(hwnd)
    l0 = []
    while True:
        l1 = []
        for chwnd in L:
            try:
                l = get_hwnd_child(chwnd)
                l1 += l
            except:
                pass
        if l1 == []:
            return l0 + L
        else:
            l0 += l1
            L = l1

#根据类名，标题查找句柄
def find_handler(clsname,title):
    M = []
    for handler in search_allchwnd():
        if win32gui.GetClassName(handler) == clsname and title == None:
            M.append(handler)
        elif win32gui.GetWindowText(handler) == title and clsname == None:
            M.append(handler)
        elif win32gui.GetClassName(handler) == clsname and win32gui.GetWindowText(handler) == title:
            M.append(handler)
        else:
            pass
    if len(M) == 0:
        return 'NOT FIND'
    else:
        return M




