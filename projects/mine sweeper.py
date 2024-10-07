
import pygame
import random as r
l=500
check=0
mouseup=True
mousedown=False
pickupDist=5
b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y,b5x,b5y,b6x,b6y,b7x,b7y,b8x,b8y,b9x,b9y=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
screen=pygame.display.set_mode((l,l))
num=1
g=0
running=True
screen.fill((255,255,255))
x=0
y=0
while not x==l:
    pygame.draw.line(screen,(0,0,255,),(x,0),(x,l))
    pygame.draw.line(screen,(255,0,0,),(0,x),(l,x))
    
    x+=10
x=0
while running:

    mousex, mousey = pygame.mouse.get_pos()
    while not num==10:
        xpos=r.randint(1,50)
        xpos= xpos*10
        ypos=r.randint(1,50)
        ypos= ypos*10
        
        
        if num==1:
            b1x,b1y=(xpos-5,ypos-5)
        elif num==2:
            b2x,b2y=(xpos-5,ypos-5)
        elif num==3:
            b3x,b3y=(xpos-5,ypos-5)            
        elif num==4:
            b4x,b4y=(xpos-5,ypos-5)
        elif num==5:
            b5x,b5y=(xpos-5,ypos-5) 
        elif num==6:
            b6x,b6y=(xpos-5,ypos-5) 
        elif num==7:
            b7x,b7y=(xpos-5,ypos-5) 
        elif num==8:
            b8x,b8y=(xpos-5,ypos-5)             
        elif num==9:
            b9x,b9y=(xpos-5,ypos-5)
        num+=1
        
    if mousedown:
        if (mousex-b1x)<pickupDist and (mousex-b1x)>-pickupDist and (mousey-b1y)<pickupDist and (mousey-b1y)>-pickupDist:
            pygame.draw.circle(screen,(255,0,0),(b1x,b1y),(10))
        elif (mousex-b2x)<pickupDist and (mousex-b2x)>-pickupDist and (mousey-b2y)<pickupDist and (mousey-b2y)>-pickupDist:
            pygame.draw.circle(screen,(255,0,0),(b2x,b2y),(10))
        elif (mousex-b3x)<pickupDist and (mousex-b3x)>-pickupDist and (mousey-b3y)<pickupDist and (mousey-b3y)>-pickupDist:
            pygame.draw.circle(screen,(255,0,0),(b3x,b3y),(10))
        elif (mousex-b4x)<pickupDist and (mousex-b4x)>-pickupDist and (mousey-b4y)<pickupDist and (mousey-b4y)>-pickupDist:
            pygame.draw.circle(screen,(255,0,0),(b4x,b4y),(10))
        elif (mousex-b5x)<pickupDist and (mousex-b5x)>-pickupDist and (mousey-b5y)<pickupDist and (mousey-b5y)>-pickupDist:
            pygame.draw.circle(screen,(255,0,0),(b5x,b5y),(10))
        elif (mousex-b6x)<pickupDist and (mousex-b6x)>-pickupDist and (mousey-b6y)<pickupDist and (mousey-b6y)>-pickupDist:
            pygame.draw.circle(screen,(255,0,0),(b6x,b6y),(10))
        elif (mousex-b7x)<pickupDist and (mousex-b7x)>-pickupDist and (mousey-b7y)<pickupDist and (mousey-b7y)>-pickupDist:
            pygame.draw.circle(screen,(255,0,0),(b7x,b7y),(10))
        elif (mousex-b8x)<pickupDist and (mousex-b8x)>-pickupDist and (mousey-b8y)<pickupDist and (mousey-b8y)>-pickupDist:
            pygame.draw.circle(screen,(255,0,0),(b8x,b8y),(10))
        elif (mousex-b9x)<pickupDist and (mousex-b9x)>-pickupDist and (mousey-b9y)<pickupDist and (mousey-b9y)>-pickupDist:
            pygame.draw.circle(screen,(255,0,0),(b9x,b9y),(10))
        if mousedown:

            pygame.draw.polygon(screen,(110,110,110),((b1x,b1y),(b2x,b2y),(b3x,b3y),(b4x,b4y),(b5x,b5y),(b6x,b6y),(b7x,b7y),(b8x,b8y),(b9x,b9y)),(2))
            pygame.draw.circle(screen,(0,255,0),(b1x,b1y),(5))

    while g<1:
        if (x-b1x)==0  and (y-b1y)==0:
            pygame.draw.polygon(screen,(123,23,23),((x-5,y-5),(x-5,y+5),(x+5,y+5),(x+5,y-5)))
            g+=1
        x+=5
        if x>l:
            x=0
            y+=1
        if y>l:
            y=0
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown=True
            mouseup=False
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown=False
            mouseup=True

    
    print(mouseup,mousex,mousey,g)        
    pygame.display.flip()