
import random as r
import pygame
l=1000
w=500
green=(25,255,25)
red=(255,76,48)
black=(0,0,0)
white=(255,255,255)
X=[]
Y=[]
i=0
count=0
def tail(a,b):
    a[score]=X[-5*int(score)]
    b[score]=Y[-5*int(score)]
    pygame.draw.circle(screen,white,(x1,y1),10)
x=l/2
y=w/2
xpos=0
ypos=0
xDir=0
yDir=0
delay=5
score=0
scorecount=0
running=True
pickupDist=15
speed=1
screen=pygame.display.set_mode((l,w))
while running:
    mousex, mousey = pygame.mouse.get_pos()
    pygame.time.delay(delay)
    if (x-xpos)<pickupDist and (x-xpos)>-pickupDist and (y-ypos)<pickupDist and (y-ypos)>-pickupDist:
        score= score+1 
    if score==scorecount:
        xpos=r.randint(10,(l-10))
        ypos=r.randint(10,(w-10))
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
                
            if event.key == pygame.K_SPACE:
                score+=1
    screen.fill(green)
    x = x +(speed*xDir)
    y = y + (speed*yDir)
    pygame.draw.circle(screen,red,(xpos,ypos),(5))
    
    pygame.draw.circle(screen,black,(x,y),10)

    X.append(x)
    Y.append(y)
    if score>=1:
        x1=X[-5*3]
        y1=Y[-5*3]
        pygame.draw.circle(screen,white,(x1,y1),10)
        if x==x1 and y==y1:
            running=False
    if score>=2:
        x2=X[-5*2*3]
        y2=Y[-5*2*3]
        pygame.draw.circle(screen,black,(x2,y2),10)
        if x==x2 and y==y2:
            running=False
    if score>=3:
        x3=X[-5*3*3]
        y3=Y[-5*3*3]
        pygame.draw.circle(screen,white,(x3,y3),10)
        if x==x3 and y==y3:
            running=False
    if score>=4:
        x4=X[-5*4*3]
        y4=Y[-5*4*3]
        pygame.draw.circle(screen,black,(x4,y4),10)
        if x==x4 and y==y4:
            running=False
    if score>=5:
        x5=X[-5*5*3]
        y5=Y[-5*5*3]
        pygame.draw.circle(screen,white,(x5,y5),10)
        if x==x5 and y==y5:
            running=False
    if score>=6:
        x6=X[-5*6*3]
        y6=Y[-5*6*3]
        pygame.draw.circle(screen,black,(x6,y6),10)
        if x==x6 and y==y6:
            running=False
    if score>=7:
        x7=X[-5*7*3]
        y7=Y[-5*7*3]
        pygame.draw.circle(screen,white,(x7,y7),10)
        if x==x7 and y==y7:
            running=False
    if score>=8:
        x8=X[-5*8*3]
        y8=Y[-5*8*3]
        pygame.draw.circle(screen,black,(x8,y8),10)
        if x==x8 and y==y8:
            running=False
    if score>=9:
        x9=X[-5*9*3]
        y9=Y[-5*9*3]
        pygame.draw.circle(screen,white,(x9,y9),10)
        if x==x9 and y==y9:
            running=False
    if score==10:
        running=False
    pygame.display.flip()