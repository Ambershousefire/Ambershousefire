
import random as r
import pygame
l=1000
w=500
green=(25,200 ,25)
red=(255,25,25)
X=[]
Y=[]
x=l/2
y=w/2
applex=0
appley=0
xDir=0
yDir=0
delay=5
score=0
scorecount=0#to check if socre has incressed
running=True
lines=False
i=0
screen=pygame.display.set_mode((l,w))
pygame.display.set_caption("snake for real this time")
def sectDrawing(X, Y, score, screen, iter):
    black = (0,0,0)
    white = (255,255,255)
    if i%2 == 1:
        colour = white
    else:
        colour = black
    if score>=iter:
        pygame.draw.circle(screen,colour,(X[15*-iter],Y[15*-iter]),10)
while running:
    screen.fill(green)
    pygame.time.delay(delay)
    if (x-applex)<15 and (x-applex)>-15 and (y-appley)<15 and (y-appley)>-15:
        score+=1
    if score==scorecount:
        applex=r.randint(10,(l-10))
        appley=r.randint(10,(w-10))
        scorecount+=1
    if x>l:
        x=0
    if x<0:
        x=l
    if y>w:
        y=0
    if y<0:
        y=w
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                yDir = -1
                xDir = 0
            elif event.key == pygame.K_DOWN:
                yDir = 1
                xDir = 0
            elif event.key == pygame.K_LEFT:
                xDir = -1
                yDir = 0
            elif event.key == pygame.K_RIGHT:
                xDir = 1
                yDir = 0 
            elif event.key == pygame.K_w:
                yDir = -1
                xDir = 0
            elif event.key == pygame.K_s:
                yDir = 1
                xDir = 0
            elif event.key == pygame.K_a:
                xDir = -1
                yDir = 0
            elif event.key == pygame.K_d:
                xDir = 1
                yDir = 0
            if event.key == pygame.K_ESCAPE:
                xDir=0
                yDir=0 
            if event.key == pygame.K_e:
                if lines:
                    lines=False
                else:
                    lines=True     
    x = x +(1*xDir)
    y = y + (1*yDir)
    if lines:
        pygame.draw.polygon(screen,red,((applex,appley),(applex,y),(x,y)),1)
    pygame.draw.circle(screen,red,(applex,appley),(5))
    pygame.draw.circle(screen,(0,0,80),(x,y),10)
    X.append(x)
    Y.append(y)
    while i<score:
        i+=1
        sectDrawing(X, Y, score, screen, i)
    i=0
    if score==100:
        running=False
        print(score,"wow that took forever")
    pygame.display.flip()