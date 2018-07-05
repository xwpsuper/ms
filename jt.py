import time
from PIL import ImageGrab
import win32gui

handle = 0x51c02
win32gui.SetForegroundWindow(handle)
win32gui.SetActiveWindow(handle)
left, top, right, botton = win32gui.GetWindowRect(handle)
img = ImageGrab.grab((left, top, right, botton))
img.save('new.png', format='PNG')