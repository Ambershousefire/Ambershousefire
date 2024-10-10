
import random as r
import pygame
l=1000
w=500
green=(25,200 ,25)
red=(255,25,25)
black=(0,0,0)
white=(255,255,255)
X=[]
Y=[]
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
pygame.display.set_caption("snake for real this time")
def sectDrawing(colour, X, Y, score, screen, iter):
    if score>=iter:
        pygame.draw.circle(screen,colour,(X[15*-iter],Y[15*-iter]),10)

while running:

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
                print(score)
                
    screen.fill(green)
    x = x +(speed*xDir)
    y = y + (speed*yDir)
    pygame.draw.circle(screen,red,(xpos,ypos),(5))
    
    pygame.draw.circle(screen,(0,0,26),(x,y),10)

    X.append(x)
    Y.append(y)
    sectDrawing(white, X, Y, score, screen, 1)
    sectDrawing(black, X, Y, score, screen, 2)
    sectDrawing(white, X, Y, score, screen, 3)
    sectDrawing(black, X, Y, score, screen, 4)
    sectDrawing(white, X, Y, score, screen, 5)
    sectDrawing(black, X, Y, score, screen, 6)
    sectDrawing(white, X, Y, score, screen, 7)
    sectDrawing(black, X, Y, score, screen, 8)
    sectDrawing(white, X, Y, score, screen, 9)
    sectDrawing(black, X, Y, score, screen, 10)
    sectDrawing(white, X, Y, score, screen, 11)
    sectDrawing(black, X, Y, score, screen, 12)
    sectDrawing(white, X, Y, score, screen, 13)
    sectDrawing(black, X, Y, score, screen, 14)
    sectDrawing(white, X, Y, score, screen, 15)
    sectDrawing(black, X, Y, score, screen, 16)
    sectDrawing(white, X, Y, score, screen, 17)
    sectDrawing(black, X, Y, score, screen, 18)
    sectDrawing(white, X, Y, score, screen, 19)
    sectDrawing(black, X, Y, score, screen, 20)    
    sectDrawing(white, X, Y, score, screen, 21)
    sectDrawing(black, X, Y, score, screen, 22)
    sectDrawing(white, X, Y, score, screen, 23)
    sectDrawing(black, X, Y, score, screen, 24)
    sectDrawing(white, X, Y, score, screen, 25)
    sectDrawing(black, X, Y, score, screen, 26)
    sectDrawing(white, X, Y, score, screen, 27)
    sectDrawing(black, X, Y, score, screen, 28)
    sectDrawing(white, X, Y, score, screen, 29)
    sectDrawing(black, X, Y, score, screen, 30)
    sectDrawing(white, X, Y, score, screen, 31)
    sectDrawing(black, X, Y, score, screen, 32)
    sectDrawing(white, X, Y, score, screen, 33)
    sectDrawing(black, X, Y, score, screen, 34)
    sectDrawing(white, X, Y, score, screen, 35)
    sectDrawing(black, X, Y, score, screen, 36)
    sectDrawing(white, X, Y, score, screen, 37)
    sectDrawing(black, X, Y, score, screen, 38)
    sectDrawing(white, X, Y, score, screen, 39)
    sectDrawing(black, X, Y, score, screen, 40)
    sectDrawing(white, X, Y, score, screen, 41)
    sectDrawing(black, X, Y, score, screen, 42)
    sectDrawing(white, X, Y, score, screen, 43)
    sectDrawing(black, X, Y, score, screen, 44)
    sectDrawing(white, X, Y, score, screen, 45)
    sectDrawing(black, X, Y, score, screen, 46)
    sectDrawing(white, X, Y, score, screen, 47)
    sectDrawing(black, X, Y, score, screen, 48)
    sectDrawing(white, X, Y, score, screen, 49)
    sectDrawing(black, X, Y, score, screen, 50)
    sectDrawing(white, X, Y, score, screen, 51)
    sectDrawing(black, X, Y, score, screen, 52)
    sectDrawing(white, X, Y, score, screen, 53)
    sectDrawing(black, X, Y, score, screen, 54)
    sectDrawing(white, X, Y, score, screen, 55)
    sectDrawing(black, X, Y, score, screen, 56)
    sectDrawing(white, X, Y, score, screen, 57)
    sectDrawing(black, X, Y, score, screen, 58)
    sectDrawing(white, X, Y, score, screen, 59)
    sectDrawing(black, X, Y, score, screen, 50)
    sectDrawing(white, X, Y, score, screen, 51)
    sectDrawing(black, X, Y, score, screen, 52)
    sectDrawing(white, X, Y, score, screen, 53)
    sectDrawing(black, X, Y, score, screen, 54)
    sectDrawing(white, X, Y, score, screen, 55)
    sectDrawing(black, X, Y, score, screen, 56)
    sectDrawing(white, X, Y, score, screen, 57)
    sectDrawing(black, X, Y, score, screen, 58)
    sectDrawing(white, X, Y, score, screen, 59)
    sectDrawing(black, X, Y, score, screen, 60)
    sectDrawing(white, X, Y, score, screen, 61)
    sectDrawing(black, X, Y, score, screen, 62)
    sectDrawing(white, X, Y, score, screen, 63)
    sectDrawing(black, X, Y, score, screen, 64)
    sectDrawing(white, X, Y, score, screen, 65)
    sectDrawing(black, X, Y, score, screen, 66)
    sectDrawing(white, X, Y, score, screen, 67)
    sectDrawing(black, X, Y, score, screen, 68)
    sectDrawing(white, X, Y, score, screen, 69)
    sectDrawing(black, X, Y, score, screen, 70)
    sectDrawing(white, X, Y, score, screen, 71)
    sectDrawing(black, X, Y, score, screen, 72)
    sectDrawing(white, X, Y, score, screen, 73)
    sectDrawing(black, X, Y, score, screen, 74)
    sectDrawing(white, X, Y, score, screen, 75)
    sectDrawing(black, X, Y, score, screen, 76)
    sectDrawing(white, X, Y, score, screen, 77)
    sectDrawing(black, X, Y, score, screen, 78)
    sectDrawing(white, X, Y, score, screen, 79)
    sectDrawing(black, X, Y, score, screen, 80)
    sectDrawing(white, X, Y, score, screen, 81)
    sectDrawing(black, X, Y, score, screen, 82)
    sectDrawing(white, X, Y, score, screen, 83)
    sectDrawing(black, X, Y, score, screen, 84)
    sectDrawing(white, X, Y, score, screen, 85)
    sectDrawing(black, X, Y, score, screen, 86)
    sectDrawing(white, X, Y, score, screen, 87)
    sectDrawing(black, X, Y, score, screen, 88)
    sectDrawing(white, X, Y, score, screen, 89)
    sectDrawing(black, X, Y, score, screen, 90)
    sectDrawing(white, X, Y, score, screen, 91)
    sectDrawing(black, X, Y, score, screen, 92)
    sectDrawing(white, X, Y, score, screen, 93)
    sectDrawing(black, X, Y, score, screen, 94)
    sectDrawing(white, X, Y, score, screen, 95)
    sectDrawing(black, X, Y, score, screen, 96)
    sectDrawing(white, X, Y, score, screen, 97)
    sectDrawing(black, X, Y, score, screen, 98)
    sectDrawing(white, X, Y, score, screen, 99)

    if score==100:
        running=False
        print(score,"wow that took forever")
    pygame.display.flip()