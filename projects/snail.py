
import random as r
import pygame

global screen
x=450
y=220
alpha=0
bata=0
pos=((x,y))
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(12,183,30)
score=0
scorecount=0
delay=5
screen=pygame.display.set_mode((900,450))
running=True
xpos=r.randint(1,890)
ypos=r.randint(1,440)
xDir=0
yDir=0
speed = 1
pickupDist = 15

def snake(screen, x, y, alpha, bata, black, white):
    pygame.draw.circle(screen,black,(x,y),(10))
    pygame.draw.circle(screen,white,(x+alpha,y+bata),(10))

while running:
    
    pygame.display.set_caption("supper snail")
    
    if score==scorecount:
        print("score:",score)
        xpos=r.randint(1,890)
        ypos=r.randint(1,440)
        speed= speed+0.5
        scorecount= scorecount+1
        
    if (x-xpos)<pickupDist and (x-xpos)>-pickupDist and (y-ypos)<pickupDist and (y-ypos)>-pickupDist:
        score= score+1 
    
    screen.fill(green)
    pygame.draw.circle(screen,red,((xpos),(ypos)),(5))
    pygame.time.delay(delay)
    snake(screen, x, y, alpha, bata, black, white)
    
    if y>450:
        y=0
    elif y<0:
        y=450
    if x>900:
        x=0
    elif x<0:
        x=900
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             running = False
             
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bata=+10
                alpha=0
                yDir = -1
                xDir = 0#
            elif event.key == pygame.K_DOWN:
                bata=-10
                alpha=0
                yDir = 1
                xDir = 0
                
            elif event.key == pygame.K_LEFT:
                alpha=+10
                bata=0
                xDir = -1
                yDir = 0
                
            elif event.key == pygame.K_RIGHT:
                alpha=-10
                bata=0
                xDir = 1
                yDir = 0
                
            if event.key == pygame.K_SPACE:
                running=False

    if score>=10:
        running=False
        print("how did you win that, you were moving like 100 pixles a second")

    x = x +(speed*xDir)
    y = y + (speed*yDir)
    
    pygame.display.flip()

pygame.quit()