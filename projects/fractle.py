
import pygame
l=600
colour=True
space=True
color=(0,0,0)
y=0
b=0
z=1
x2=0
count=1
yDir=0
x2Dir=0
speed=.001
black=(0,0,0)
white=(255,255,255)
screen=pygame.display.set_mode((l,l))
running =True
screen.fill((white))
while running:
    b+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                yDir=-1
                x2Dir=1
            if event.key == pygame.K_SPACE:
                xDir=0
                x2Dir=0
                yDir=0
                y2Dir=0
                if space:
                    space=False
                else:
                    space=True
            if event.key == pygame.K_z:
                count+=1
            if event.key == pygame.K_e:
                if speed==.1:
                    speed=.001
                else:
                    speed=.1
    if count==4:
        count=1
    if x2<0:
        x2=l
    if x2>l:
        x2=0

    if y<0:
        y=l
    if y>l:
        y=0

    x2 = x2 + (speed*x2Dir)
    x2-=x2Dir
    y = y +(speed*yDir)
    y-=yDir
    if colour:
        color=(0,0,0)
        colour=False
    else:
        color=white
        colour=True
    if space:
        pygame.draw.line(screen,color,(0,y),(l/z,l/z))
        pygame.draw.line(screen,color,(x2,0),(l/z,l/z))
        
        if count>2:
            z=2
            pygame.draw.line(screen,color,(l,l-y),(l/z,l/z))
            pygame.draw.line(screen,color,(l-x2,l),(l/z,l/z))
            
        if count<2:
            z=1
    if b>10000:
        b=0
        count+=1
    print(speed)
    pygame.display.flip()