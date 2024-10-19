
import pygame
#colour
black = (0,0,0)#1
white = (255,255,255)#2
red = (255,0,0)#3
orange = (255,125,0)#4
yellow = (255,255,0)#5
lime = (128,255,0)#6
green = (0,255,0)#7
cyan = (0,255,128)#8
light_blue = (0,255,255)#9
blue = (0,0,255)#10
violet = (127,0,255)#11
purple = (255,0,255)#12
pink = (255,153,204)#13
gray = (125,125,125)#14
brown = (51,24,0)#15
colour_list = [black,white,red,orange,yellow,lime,green,cyan,light_blue,blue,violet,purple,pink,gray,brown]
def mouse_pos_local(w):
    i=0
    z=0
    mousex,mousey=pygame.mouse.get_pos()
    i=int((mousex/w))
    z=int((mousey/w))
    return i,z
#pygame.draw.polygon(screen,hid[int(b[z]-a[i])],((i*100,z*100),(i*100,z*100+100),(i*100+100,z*100+100),(i*100+100,z*100)))
#pygame.draw.polygon(screen,hid[int(a[i]-b[z])],((i*100,z*100),(i*100,z*100+100),(i*100+100,z*100+100),(i*100+100,z*100)))