
import webbrowser,win32api, win32con , time , keyboard 
from PIL import ImageGrab



webbrowser.open('https://aternos.org/server/',2,True)
time.sleep(15)

def click(x,y):

    win32api.SetCursorPos((x,y))
    #px=ImageGrab.grab().load()
    #colour = px[x,y]
    #while not colour==(31, 215, 141) or (29,198,130):
        #print(colour)
        #time.sleep(.5)
    time.sleep(5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    print("open")

    time.sleep(5)

    keyboard.press('alt')
    keyboard.press('f4')
    keyboard.release('f4')
    keyboard.release('alt')


click(700,550)