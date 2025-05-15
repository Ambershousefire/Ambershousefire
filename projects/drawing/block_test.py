import pygame
alpha=2
mode=255*alpha
screen=pygame.display.set_mode((mode,mode))
running=True
mbd=False
mbu=True
bx=[0]
by=[0]
i=0
G=55
z=0
l=0
size=1
while not l >= mode/size:
    bx.append(z*size)
    by.append(l*size)
    if not z+1 >= mode/size:
        z+=1
    else:
        l+=1
        z=0
bx.append(mode)
by.append(mode)
print(len(bx))
while running:
    screen.fill((0,0,0))
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mbd=True
            mbu=False
        if event. type == pygame.MOUSEBUTTONUP:
            mbd=False
            mbu=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                bx.clear
                by.clear
            if event.key == pygame.K_UP:
                if not G == 255:
                    G+=1
                else:
                    print(G)
            if event.key == pygame.K_DOWN:
                if not G==0:
                    G-=1
                else:
                    print(G)
    while not i==len(bx)-1:
        pygame.draw.polygon(screen,((255-round(bx[i]/alpha)),G,(255-round(by[i]/alpha))),[(bx[i],by[i]),(bx[i]+size,by[i]),(bx[i]+size,by[i]+size),(bx[i],by[i]+size)])
        if x >=bx[i] and x<=bx[i]+size:
            if y>=by[i] and y<=by[i]+size:
                if mbd:
                    print(255-round(bx[i]/alpha),G,255-round(by[i]/alpha))
        if bx[i]<0:
            bx[i]=0
        if bx[i]>mode-size:
            bx[i]=mode-size
        if by[i]<0 :
            by[i]=0
        if by[i]>mode-size:
            by[i]=mode-size
        i+=1
    i=0
    pygame.display.flip()