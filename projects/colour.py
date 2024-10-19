
import pygame


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (255,125,0)
yellow = (255,255,0)
lime = (128,255,0)
green = (0,255,0)
cyan = (0,255,128)
light_blue = (0,255,255)
blue = (0,0,255)
violet = (127,0,255)
purple = (255,0,255)
pink = (255,153,204)
gray = (125,125,125)
brown = (51,24,0)

def mouse_pos_local(w):
    i=0
    z=0
    mousex,mousey=pygame.mouse.get_pos()
    i=int((mousex/w))
    z=int((mousey/w))
    return i,z
#pygame.draw.polygon(screen,hid[int(b[z]-a[i])],((i*100,z*100),(i*100,z*100+100),(i*100+100,z*100+100),(i*100+100,z*100)))
#pygame.draw.polygon(screen,hid[int(a[i]-b[z])],((i*100,z*100),(i*100,z*100+100),(i*100+100,z*100+100),(i*100+100,z*100)))