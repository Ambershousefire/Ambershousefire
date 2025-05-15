
import pygame 
mode = 500
screen= pygame.display.set_mode((mode,mode))
running = True
playerx=[250]
playery=[250]
bx=[0]
by=[0]
size=10
i=0

while running:

    screen.fill((255-mode/5,255-mode/6,255-mode/3))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                bx.append(100)
                by.append(100)

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                while i<len(playery):
                   playery[i]-=size
                   i+=1
                i=0
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                while i<len(playerx):
                   playerx[i]-=size
                   i+=1
                i=0
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                while i<len(playery):
                   playery[i]+=size
                   i+=1
                i=0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                while i<len(playerx):
                   playerx[i]+=size
                   i+=1
                i=0
    while i<len(playerx):
        if playerx[i]<=0:
            playerx[i]+=mode

        if playerx[i]>=mode:
            playerx[i]-=mode

        if playery[i]<=0:
            playery[i]+=mode

        if playery[i]>=mode:
            playery[i]-=mode
        pygame.draw.polygon(screen,(255,255,255),((playerx[i],playery[i]),(playerx[i]+size,playery[i]),(playerx[i]+size,playery[i]+size),(playerx[i],playery[i]+size)))
        i+=1

    i=0
    while i<len(bx):
        if bx[i]<=0:
            bx[i]+=mode

        if bx[i]>=mode:
            bx[i]-=mode

        if by[i]<=0:
            by[i]+=mode

        if by[i]>=mode:
            by[i]-=mode
        pygame.draw.polygon(screen,(0,0,0),((bx[i],by[i]),(bx[i]+size,by[i]),(bx[i]+size,by[i]+size),(bx[i],by[i]+size)))

        i+=1  
    i=0


    pygame.display.flip()