
import pygame
import random as r
l=500
mouseup=True
mousedown=False
b1,b2,b3,b4,b5,b6,b7,b8,b9=0,0,0,0,0,0,0,0,0
screen=pygame.display.set_mode((l,l))
num=1
running=True
screen.fill((255,255,255))
x=0
y=0
while not x==l:
    pygame.draw.line(screen,(0,0,255,),(x,0),(x,l))
    pygame.draw.line(screen,(255,0,0,),(0,x),(l,x))
    
    x+=10
while running:
    mousex, mousey = pygame.mouse.get_pos()
    
    while not num==10:
        posx=r.randint(2,48)
        posx= posx*10
        posy=r.randint(2,48)
        posy= posy*10
        
        
        if num==1:
            b1=(posx+5,posy+5)
        elif num==2:
            b2=(posx+5,posy+5)
        elif num==3:
            b3=(posx+5,posy+5)            
        elif num==4:
            b4=(posx+5,posy+5)
        elif num==5:
            b5=(posx+5,posy+5) 
        elif num==6:
            b6=(posx+5,posy+5) 
        elif num==7:
            b7=(posx+5,posy+5) 
        elif num==8:
            b8=(posx+5,posy+5)             
        elif num==9:
            b9=(posx+5,posy+5)
        num+=1
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown=True
            mouseup=False
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown=False
            mouseup=True
            
    pygame.draw.circle(screen,(125,125,125),(b1),(5))
    pygame.draw.circle(screen,(125,125,125),(b2),(5))
    pygame.draw.circle(screen,(125,125,125),(b3),(5))
    pygame.draw.circle(screen,(125,125,125),(b4),(5))
    pygame.draw.circle(screen,(125,125,125),(b5),(5))
    pygame.draw.circle(screen,(125,125,125),(b6),(5))
    pygame.draw.circle(screen,(125,125,125),(b7),(5))
    pygame.draw.circle(screen,(125,125,125),(b8),(5))
    pygame.draw.circle(screen,(125,125,125),(b9),(5))

    
    print(b1,b2,b3,b4,b5,b6,b7,b8,b9,mouseup,mousex,mousey)        
    pygame.display.flip()