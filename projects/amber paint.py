
import pygame

l=1000
w=500
global r,b,g
r=0
g=0
b=0
MouseDown=False
flip=True
y=250
x=500
xDir=0
yDir=0
delay=5
running=True
rc=False
gc=False
bc=False
togle=True
Filler=False
z=0
xmouse=0
ymouse=0
global screen 
screen=pygame.display.set_mode((l,w))
screen.fill((255,255,255))
cooler_colour=False
while running: 

    colour=((r),(g),(b))
    pygame.draw.circle(screen,colour,(x,y),(3))
    if y>500:
        y=0
        x+=1
        z+=1
    elif y<0:
        y=500
        x-=3
        z+=1
    if x>1000:
        x=0
        y+=1
        z+=1
    elif x<0:
        x=1000
        y-=1
        z+=1
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
                if togle:
                    if event.key == pygame.K_UP:
                        if flip:
                            r=0
                            g=0
                            b=0
                        else:
                            r=240
                            b=240
                            g=240
                    if event.key == pygame.K_DOWN:
                        if cooler_colour==False:
                            g+=5
                            if g>=250:
                                g=0
                        else:
                            gc=True
                    if event.key == pygame.K_LEFT:
                        if cooler_colour==False:
                            r+=5
                            if r>=250:
                                r=0
                        else:
                            rc=True

                    if event.key == pygame.K_RIGHT:
                        if cooler_colour==False:
                            b+=5
                            if b>=250:
                                b=0
                        else:
                            bc=True
                if togle==False:
                    if event.key == pygame.K_UP:
                        if r<5:
                            r=240
                        if g<5:
                            g=240
                        if b<5:
                            b=240
                        r-=5
                        g-=5
                        b-=5
                    if event.key == pygame.K_LEFT:
                        if r<5:
                            r=240
                        r-=5
                    if event.key == pygame.K_DOWN:

                        if g<5:
                            g=240
                        g-=5
                    if event.key == pygame.K_RIGHT:
                        if b<5:
                            b=240
                        b-=5
                                
                if event.key == pygame.K_e:
                    if flip:
                        screen.fill((0,0,0))
                        r=240
                        b=240
                        g=240
                        flip=False
                    else:
                        screen.fill((255,255,255))
                        r=0
                        g=0
                        b=0
                        flip=True
                if event.key == pygame.K_q:
                    if cooler_colour:
                        cooler_colour=False
                        rc=False
                        gc=False
                        bc=False
                    else:
                        cooler_colour=True
                        rc=False
                        gc=False
                        bc=False
                        
                    
                if event.key == pygame.K_SPACE:
                    xDir=0
                    yDir=0
                
                if event.key == pygame.K_f:
                    if Filler:
                        Filler=False
                    else:
                        Filler=True
                if event.key == pygame.K_r:
                    if togle:
                        togle=False
                    else:
                        togle=True


    if Filler:
        screen.fill((r,g,b))        
    if cooler_colour:
        if rc:
            r+=1
            if r==250:
                r=0
        if gc:
            g+=1
            if g==250:
                g=0
        if bc:
            b+=1
            if b==250:
                b=0
    print(r,g,b,"colour",cooler_colour,"roolerer",togle,"subtration",z)
    x = x + (0.33*xDir)
    y = y + (0.33*yDir)                 
    pygame.display.flip()
pygame.quit()