
import random
import pygame
l=int(input("how large do you wahnt the sreen to be size 1 or 2 :"))
if l==1:
    l=600
elif l==2:
    l=9000
else:
    l=900
h=l
colour=True
space=True
color=(0,0,0)
y=0
b=0
p=False
z=1
x2=0
count=1
yDir=0
x2Dir=0
black=(0,0,0)
white=(255,255,255)
screen=pygame.display.set_mode((l,l))
running =True
screen.fill((white))
while running:
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
            if event.key == pygame.K_w:
                y+=10
                x2-=10
            if event.key == pygame.K_s:
                y-=10
                x2+=10
            if event.key == pygame.K_BACKSPACE:
                running=False
    if count==3:
        count=1
    if x2<0:
        x2=l
    if y>l:
        y=0
    x2 = x2 - x2Dir
    y = y - yDir
    if colour:
        color=(black)
        colour=False
    else:
        color=(white)
        colour=True
    if space:
        pygame.draw.line(screen,color,(0,y),(l/z,l/z))
        pygame.draw.line(screen,color,(x2,0),(l/z,l/z))
        
        if count==2:
            z=2
            pygame.draw.line(screen,color,(l,l-y),(l/z,l/z))
            pygame.draw.line(screen,color,(l-x2,l),(l/z,l/z))
        if count==1:
            z=1
    pygame.display.flip()