
import colour as c, pygame
start = True
try:
    l=int(input("what size window do you wahnt: "))
except:
    print("not a full number try again","\n")
    start = False
if start:
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
        if w<0:
            w=1
        if mouseDown:
            i,z=c.mouse_pos_relative(w)
            c.square(screen,c.colour_list[x],i,z,w)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    w=1
                if event.key == pygame.K_e:
                    if not x==14:
                        x+=1
                if event.key == pygame.K_q:
                    if not x == 0:
                        x-=1
                if event.key == pygame.K_ESCAPE:
                    running=False
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown=False
            if event.type == pygame.MOUSEWHEEL:
                if event.y==1:
                    w+=1
                elif event.y==-1:
                    if not w==1:
                        w-=1
                    else:
                        w=w