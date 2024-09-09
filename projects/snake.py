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
xpos=r.randint(1,89)
xpos=xpos*10
ypos=r.randint(1,89)
ypos=ypos*10
def snake(screen, x, y, alpha, bata, black, white):
    pygame.draw.circle(screen,black,(x,y),(10))
    pygame.draw.circle(screen,white,(x+alpha,y+bata),(10))

while running:
    pygame.display.set_caption("snail""score:",str(score))
    if score==scorecount:
        xpos=r.randint(1,89)
        xpos=xpos*10
        ypos=r.randint(1,44)
        ypos=ypos*10
        scorecount= scorecount+1
        
    if x==xpos and y==ypos:
        score= score+1 
    
        
    screen.fill(green)
    pygame.draw.circle(screen,red,((xpos),(ypos)),(5))
    pygame.time.delay(delay)
    snake(screen, x, y, alpha, bata, black, white)
    
    
    for event in pygame.event.get():
        if y>440:
            y=10
        elif y<10:
            y=440
        if x>890:
            x=10
        elif x<10:
            x=890

        if event.type == pygame.QUIT: 
             running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bata=+10
                alpha=0
                y=y-10
            elif event.key == pygame.K_DOWN:
                bata=-10
                alpha=0
                y=y+10
            elif event.key == pygame.K_LEFT:
                alpha=+10
                bata=0
                x=x-10
            elif event.key == pygame.K_RIGHT:
                alpha=-10
                bata=0
                x=x+10
            elif event.key == pygame.K_SPACE:
                score= score+1
        if score==10:
            pygame.quit()


                
    #debug

    print("player:",x,y,alpha,bata,"apple:",xpos,ypos,"score:",score)
            
             







    pygame.display.flip()

pygame.quit()
print("how did you win")