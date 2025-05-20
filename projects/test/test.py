
import pygame 
mode = 500
screen= pygame.display.set_mode((mode,mode))
running = True
playerx=250
playery=250
bx=[150]
by=[250]
map_x=[]
map_y=[]
size=10
i=0
dbx=[0,10,20,30,40]
dby=[0,0,0,0,0]
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
                if (playery-size == by[i]) and (playerx == bx[i]):
                    by[i]-=size
                playery-=size
                map_y.append(playery)
                map_x.append(playerx)
                
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if (playerx-size == bx[i]) and (playery == by[i]):
                    bx[i]-=size
                playerx-=size
                map_y.append(playery)
                map_x.append(playerx)
                
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if (playery+size == by[i]) and (playerx == bx[i]):
                    by[i]+=size
                playery+=size
                map_y.append(playery)
                map_x.append(playerx)

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if (playerx+size == bx[i]) and (playery == by[i]):
                    bx[i]+=size
                playerx+=size
                map_y.append(playery)
                map_x.append(playerx)

        if playerx<=0:
            playerx+=mode

        if playerx>=mode:
            playerx-=mode

        if playery<=0:
            playery+=mode

        if playery>=mode:
            playery-=mode

    if bx[i]<0:
        bx[i]=mode-2*size

    if bx[i]>mode:
        bx[i]=size

    if by[i]<0:
        by[i]=mode-2*size

    if by[i]>mode:
        by[i]=size
    if not dbx == 0:
        while i<len(dbx):
            pygame.draw.polygon(screen,(255,0,0),((dbx[i],dby[i]),(dbx[i]+size,dby[i]),(dbx[i]+size,dby[i]+size),(dbx[i],dby[i]+size)))
            i+=1
        i=0
        z=0
    while i<len(bx):
        while z<len(dbx):
            if (dbx[z]==bx[i] and dby[i]==by[i]):
                running = False
            z+=1
        z=0
        i+=1
    i=0
    pygame.draw.polygon(screen,(0,0,0),((bx[i],by[i]),(bx[i]+size,by[i]),(bx[i]+size,by[i]+size),(bx[i],by[i]+size)))
    pygame.draw.polygon(screen,(255,255,255),((playerx,playery),(playerx+size,playery),(playerx+size,playery+size),(playerx,playery+size)))
    print(playerx,playery,bx[i],by[i])
    pygame.display.flip()
print(map_x)
print("\n\n\n")
print(map_y)