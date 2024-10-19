
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
def mouse_pos_relative(pos_box_size):
    i=0
    z=0
    mousex,mousey=pygame.mouse.get_pos()
    try:
        i=int((mousex/pos_box_size))
        z=int((mousey/pos_box_size))
    except:
        i=0
        z=0
    return i,z
def square(place,color,x,y,size):
    pygame.draw.polygon(place,color,((x*size,y*size),(x*size,y*size+size),(x*size+size,y*size+size),(x*size+size,y*size)))