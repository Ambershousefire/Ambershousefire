import random as r
import pygame


global screen
x=450
y=220
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
    pygame.draw.circle(screen,red,((xpos),(ypos)),(10))
    pygame.time.delay(delay)
    pygame.draw.circle(screen,black,(x,y),(10))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y=y-10
            elif event.key == pygame.K_DOWN:
                y=y+10
            elif event.key == pygame.K_LEFT:
                x=x-10
            elif event.key == pygame.K_RIGHT:
                x=x+10
            elif event.key == pygame.K_SPACE:
                score= score+1
        if score==10:
            pygame.quit()


                
    #debug

    print("player:",x,y,"apple:",xpos,ypos,"score:",score)
            
             







    pygame.display.flip()

pygame.quit()
print("how did you win")