
import pygame
l=560
w=420
screen=pygame.display.set_mode((l,w))
blue=(0,125,255)
red=(255,0,0,)
yellow=(255,255,0)
running=True
screen.fill(blue)
hole=0
x=40
y=30
r1=1
r2=1
r3=1
r4=1
r5=1
r6=1
r7=1
togle=False
while hole<43:
        if x>l:
            x=40
        pygame.draw.circle(screen,(255,255,255),(x,y),(30))
        x+=80
        if hole == 7:
            y+=65
        if hole == 14:
            y+=65
        if hole == 21:
            y+=65
        if hole == 28:
            y+=65
        if hole == 35:
            y+=65
        hole+=1
x=40
y=30
py=30
while running:
    if x<40:
        x=520
    if x>560:
        x=40
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if togle:
                    togle=False
                    if x==40:
                        y=420-65*r1
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r1+=1
                        y=0
                    if x==120:
                        y=420-65*r2
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r2+=1
                        y=0
                    if x==200:
                        y=420-65*r3
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r3+=1
                        y=0
                    if x==280:
                        y=420-65*r4
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r4+=1
                        y=0
                    if x==360:
                        y=420-65*r5
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r5+=1
                        y=0
                    if x==440:
                        y=420-65*r6
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r6+=1
                        y=0
                    if x==520:
                        y=420-65*r7
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r7+=1
                        y=0
                else:
                    togle=True
                    if x==40:
                        y=420-65*r1
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r1+=1
                        y=0
                    if x==120:
                        y=420-65*r2
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r2+=1
                        y=0
                    if x==200:
                        y=420-65*r3
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r3+=1
                        y=0
                    if x==280:
                        y=420-65*r4
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r4+=1
                        y=0
                    if x==360:
                        y=420-65*r5
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r5+=1
                        y=0
                    if x==440:
                        y=420-65*r6
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r6+=1
                        y=0
                    if x==520:
                        y=420-65*r7
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r7+=1
                        y=0
                        
            if event.key == pygame.K_a:
                pygame.draw.circle(screen,(255,255,255),(x,py),(20))
                x-=80
            if event.key == pygame.K_d:
                pygame.draw.circle(screen,(255,255,255),(x,py),(20))
                x+=80
    
    print(togle,x)
    pygame.draw.circle(screen,(125,255,125),(x,py),(20))
    pygame.display.flip()