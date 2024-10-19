import colour as c, pygame
l=500
screen = pygame.display.set_mode((l,l))
i=0
z=0
x=1
w=10
num=0
mouseDown=False
running=True
screen.fill(c.white)
while running:
    if x==0:
        x=1
    if mouseDown:
        i,z=c.mouse_pos_relative(w)
        c.square(screen,c.colour_list[x],i,z,w)
    pygame.display.flip()

    for event in pygame.event.get():
        print(x,"colour",w,"size")
        if event.type == pygame.QUIT: 
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown=False
        if event.type == pygame.MOUSEWHEEL:
            num+=1
            if num==5:
                if event.y==1:
                    w+=5
                elif event.y==-1:
                    if not w==1:
                        w-=5
                    else:
                        w=w
                if event.x==1:
                    if not x==14:
                        x+=1
                    else:
                        x=x
                if event.x==-1:
                    if not x==0:
                        x-=1
                    else:
                        x=x
                num=0

