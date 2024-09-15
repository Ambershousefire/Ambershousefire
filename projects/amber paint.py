
import pygame

l=1000
w=500
global r,b,g
r=240
g=240
b=240
flip=True
y=250
x=500
xDir=0
yDir=0
delay=5
running=True
global screen 
screen=pygame.display.set_mode((l,w))
screen.fill((255,255,255))
cooler_colour=False
while running: 
    colour=((r),(g),(b))
    pygame.draw.circle(screen,colour,(x,y),(3))
    if y>500:
        y=0
        
    elif y<0:
        y=500
       
    if x>1000:
        x=0
        
    elif x<0:
        x=1000
        
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
             running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    yDir = -1
                    xDir = 0
                if event.key == pygame.K_a:
                    yDir = 0
                    xDir = -1
                if event.key == pygame.K_s:
                    yDir = 1
                    xDir = 0
                if event.key == pygame.K_d:
                    yDir = 0
                    xDir = 1
                if event.key == pygame.K_UP:
                    r=10
                    g=10
                    b=10
                if event.key == pygame.K_DOWN:
                    if cooler_colour==False:
                        g+=10
                        if g==250:
                            g=0
                    else:
                        while running==True:
                            g+=1
                if event.key == pygame.K_LEFT:
                    if cooler_colour==False:
                        r+=10
                        if r==250:
                            r=0
                    else:
                        while running==True:
                            r+=1

                if event.key == pygame.K_RIGHT:
                    if cooler_colour==False:
                        b+=10
                        if b==250:
                            b=0
                    else:
                        while running==True:
                            b+=1
                        
                if event.key == pygame.K_e:
                    if flip:
                        screen.fill((0,0,0))
                        flip=False
                    else:
                        screen.fill((255,255,255))
                        flip=True
                if event.key == pygame.K_q:
                    cooler_colour=True
                if event.key == pygame.K_SPACE:
                    xDir=0
                    yDir=0
    x = x + (0.25*xDir)
    y = y + (0.25*yDir)  
    print(cooler_colour,flip,r,g,b,)                 
    pygame.display.flip()
pygame.quit()