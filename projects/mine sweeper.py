
import pygame
import random as r
l=500
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
    
    x+=20
while running:
    while not num==10:
        posx=r.randint(1,49)
        posx= posx*10
        posy=r.randint(1,49)
        posy= posy*10
        
        
        if num==1:
            b1=(posx,posy)
        if num==2:
            b2=(posx,posy)
        if num==3:
            b3=(posx,posy)            
        if num==4:
            b4=(posx,posy)
        if num==5:
            b5=(posx,posy) 
        if num==6:
            b6=(posx,posy) 
        if num==7:
            b7=(posx,posy) 
        if num==8:
            b8=(posx,posy)             
        if num==9:
            b9=(posx,posy)
        num+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.draw.circle(screen,(125,125,125),(b1),(10))
    pygame.draw.circle(screen,(125,125,125),(b2),(10))
    pygame.draw.circle(screen,(125,125,125),(b3),(10))
    pygame.draw.circle(screen,(125,125,125),(b4),(10))
    pygame.draw.circle(screen,(125,125,125),(b5),(10))
    pygame.draw.circle(screen,(125,125,125),(b6),(10))
    pygame.draw.circle(screen,(125,125,125),(b7),(10))
    pygame.draw.circle(screen,(125,125,125),(b8),(10))
    pygame.draw.circle(screen,(125,125,125),(b9),(10))

    
    print(b1,b2,b3,b4,b5,b6,b7,b8,b9)        
    pygame.display.flip()