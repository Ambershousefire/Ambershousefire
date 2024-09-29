
import pygame 
l=500
x=0
y=249
x2=500
y2=0
x3=0
y3=500
x4=500
y4=500
yDir=0
y2Dir=0
y3Dir=0
y4Dir=0
xDir=0
x2Dir=0
x3Dir=0
x4Dir=0
speed=0.1
white=(255,255,255)
screen=pygame.display.set_mode((l,l))
running =True 
screen.fill((white))
while running: 
    pygame.draw.circle(screen,(0,0,0),(x,y),(5))
    pygame.draw.circle(screen,(0,0,0),(x2,y2),(5))
    pygame.draw.circle(screen,(0,0,0),(x3,y3),(5))
    pygame.draw.circle(screen,(0,0,0),(x4,y4),(5))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             running = False
        if event. type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                yDir=.1
                xDir=0
                y4Dir=-.1
                x4Dir=0
                x2Dir=-.1
                y2Dir=0
                x3Dir=.1
                y3Dir=0
            if event.key == pygame.K_DOWN:
                yDir=-.1
                xDir=0
                y4Dir=.1
                x4Dir=0
                x2Dir=.1
                y2Dir=0
                x3Dir=-.1
                y3Dir=0
            if event.key == pygame.K_LEFT:
                xDir=-.1
                yDir=0
                x4Dir=.1
                y4Dir=0
                y2Dir=-.1
                x2Dir=0
                y3Dir=.1
                x3Dir=0
            if event.key == pygame.K_RIGHT:
                xDir=.1
                yDir=0
                x4Dir=-.1
                y4Dir=0
                y2Dir=.1
                x2Dir=0
                y3Dir=-.1
                x3Dir=0
            if event.key == pygame.K_SPACE:
                xDir=0
                x2Dir=0
                x3Dir=0
                x4Dir=0
                yDir=0
                y2Dir=0
                y3Dir=0
                y4Dir=0
    if x<0:
        x=500
    if x>500:
        x=0
    if x2<0:
        x2=500
    if x2>500:
        x2=0
    if x3<0:
        x3=500
    if x3>500:
        x3=0
    if x4<0:
        x4=500
    if x4>500:
        x4=0
    if y<0:
        y=500
    if y>500:
        y=0
    if y2<0:
        y2=500
    if y2>500:
        y2=0
    if y3<0:
        y3=500
    if y3>500:
        y3=0
    if y4<0:
        y4=500
    if y4>500:
        y4=0
    
    if x<250 and y<250:
        x+=.01
        y-=.01
    elif x>250 and y>250:
        x+=.01
        y+=.01
    elif x>250 and y<250:
        x-=.01
        y+=.01
    elif x<250 and y<250:
        x-=.01
        y-=.01
          
    x = x +(speed*xDir)
    x-=xDir
    x2 = x2 + (speed*x2Dir)
    x2-=x2Dir
    x3 = x3 + (speed*x3Dir)
    x3-=x3Dir
    x4 = x4 +(speed*x4Dir)
    x4-=x4Dir
    
    y = y +(speed*yDir)
    y-=yDir
    y2 = y2 + (speed*y2Dir)
    y2-=y2Dir
    y3 = y3 + (speed*y3Dir)
    y3-=y3Dir
    y4 = y4 +(speed*y4Dir)
    y4-=y4Dir
    pygame.display.flip()
            