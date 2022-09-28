from win32gui import *
from win32con import *
from win32api import *
import time


hwnd_title = dict()

def foo(hwnd, mouse):


    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:GetWindowText(hwnd)})   #获取句柄辞典

        for h, t in hwnd_title.items():
            if t. __contains__('YesPlayMusic') is True:
                #print(h)


                alpha =100                                  #透明度 100=50%
                GetWindowLong(h, GWL_EXSTYLE)
                SetWindowLong(h, GWL_EXSTYLE, WS_EX_LAYERED)
                try:
                    SetLayeredWindowAttributes(h, 0, alpha, LWA_ALPHA) #设置半透明
                except:
                    pass


while(1):
    EnumWindows(foo, 0)
    time.sleep(1)
