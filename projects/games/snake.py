
import random as r, pygame
from time import sleep
file = open("Ambershousefire/projects/data/win_rate.txt","a")
xpos=[]
ypos=[]
x=500
y=250
applex=0
appley=0
n=0
xDir=0
yDir=0
score=0
scorecount=0#to check if score has incressed
running=True
lines=False
i=0
speed=1
lenght1=1000
lenght2=500

screen=pygame.display.set_mode((lenght1,lenght2))
pygame.display.set_caption("Snake for real this time")

def sectDrawing(xpos, ypos, score, screen, iter, space):
    black = (0,0,0)
    white = (255,255,255)
    if i%2 == 1:#if score is even colour=black
        colour = white
    else:
        colour = black
    if score>=iter:
        pygame.draw.circle(screen,colour,(xpos[space*-iter],ypos[space*-iter]),10)#uses the (space)th postion in the list multpleyed by iteration to draw tailing pieces
        #xpos[space*-iter] this only works becuse all positions of players are stored in list
while running:
    screen.fill((25,200 ,25))
    pygame.time.delay(5)
    if (x-applex)<15 and (x-applex)>-15 and (y-appley)<15 and (y-appley)>-15:#proximity detection pickup for apple
        score+=1
    if score==scorecount:#generates random positions for apple
        applex=r.randint(10,(lenght1-10))
        appley=r.randint(10,(lenght2-10))
        scorecount= score+1

    #Wrap around for the player
    if x>lenght1:
        running=False
    elif x<0:
        running=False
    elif y>lenght2:
        running=False
    elif y<0:
        running=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:#controls 
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                yDir = -1
                xDir = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                yDir = 1
                xDir = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                xDir = -1
                yDir = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                xDir = 1
                yDir = 0 
            if event.key == pygame.K_1:
                score+=10
            if event.key == pygame.K_e:
                if lines:
                    lines=False
                else:
                    lines=True
    x = x + (speed*xDir)#controls direction on x 
    y = y + (speed*yDir)#controls diretion on y

    if lines:#draws a triangle to apple 
        pygame.draw.polygon(screen,(255,25,25),((applex,appley),(applex,y),(x,y)),2)
    pygame.draw.circle(screen,(255,25,25),(applex,appley),(5))#draws the apple
    pygame.draw.circle(screen,(0,0,100),(x,y),10)#draws the players
    pygame.draw.circle(screen,(255,0,0),(x,y),1)
    xpos.append(x)#adds player position into list 
    ypos.append(y)#so that next segment can have a position
    while i<score:#draws a number of segments baced off of score
        #print(speed)
        i+=1
        sectDrawing(xpos, ypos, score, screen, i,20)
        if lines:
            pygame.draw.polygon(screen,(255,25,25),((applex,appley),(applex,ypos[i*-20]),(xpos[i*-20],ypos[i*-20])),1)
        if (x <= xpos[i*-20]+9 and x >= xpos[i*-20]-9 and y <= ypos[i*-20]+9 and y >= ypos[i*-20]-9):
            running=False

    i=0#sets i to zero for next loop
    if score==100:
        running=False
        print(score,"Wow that took forever")
    pygame.display.flip()
pygame.quit()
file.write("\nsnake: ")
file.write(str(score))