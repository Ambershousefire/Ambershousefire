import pygame, random
l=700
screen=pygame.display.set_mode((l,l))
x=0
y=500
x2=l
y2=100
x3=0
i=0
black=(0,0,0)
white=(0,0,255)
colour=True
color=black
e=0
w=0
b=True
e2=l
key=True
h=100
running=True
screen.fill((255,255,255))
while running:
    if key:
        pygame.draw.lines(screen,color,False,((x,l),(x+100,y),(x+100,l)))
        pygame.draw.lines(screen,color,False,((x2,l),(x2-100,y2),(x2-100,l)))
        pygame.draw.lines(screen,color,False,((l,x2),(y2,x2-100),(l,x2-100)))
        pygame.draw.lines(screen,color,False,((l,x),(y,x+100,),(l,x+100)))
        pygame.draw.lines(screen,color,False,((x2,l-l),(x2-100,y2),(x2-100,l-l)))
        pygame.draw.lines(screen,color,False,((x,l-l),(x+100,y2),(x+100,l-l)))
        pygame.draw.lines(screen,color,False,((l-l,x2),(y2 ,x2-100),(l-l,x2-100)))
        pygame.draw.lines(screen,color,False,((l-l,x),(y,x+100,),(l-l,x+100)))
        x+=100
        x2-=100
        y+=h/2
        y2-=h/2
        if x>l:
            x=w
        if y>l:
            y=w
        if x2<w:
            x2=l
        if y2<w:
            y2=l
        if colour:
            color=(black)
            colour=False
        else:
            color=(white)
            colour=True
    if not key:
        pygame.draw.lines(screen,color,False,((x,l),(x+100,y),(x+100,l)))
        pygame.draw.lines(screen,color,False,((x2,l),(x2-100,y2),(x2-100,l)))
        pygame.draw.lines(screen,color,False,((l,x2),(y2,x2-100),(l,x2-100)))
        pygame.draw.lines(screen,color,False,((l,x),(y,x+100,),(l,x+100)))
        pygame.draw.lines(screen,color,False,((x2,l-l),(x2-100,y2),(x2-100,l-l)))
        pygame.draw.lines(screen,color,False,((x,l-l),(x+100,y2),(x+100,l-l)))
        pygame.draw.lines(screen,color,False,((l-l,x2),(y2 ,x2-100),(l-l,x2-100)))
        pygame.draw.lines(screen,color,False,((l-l,x),(y,x+100,),(l-l,x+100)))
        pygame.draw.lines(screen,color,True,((0,e),(e,l),(l,e2),(e2,0)),(1))
        x+=100
        x2-=100
        y+=h/2
        y2-=h/2
        if x>l:
            x=w
            
        if y>l:
            y=w
        if x2<w:
            x2=l
        if y2<w:
            y2=l
        if b:
            i=e
            e+=1
            e2-=1
        if e==l:
            b=False
        if i%2 == 1:
            color = white
        if not i%2 == 1:
            color = black
        if b==False:
            i=e
            e-=1
            e2+=1
        if e<w:
            b=True
            e=w
            e2=l
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if key:
                    key=False
                    x=0
                    y=0
                    x2=l
                    y2=l
                    e=0
                    e2=l
                    screen.fill((0,0,0))
                else:
                    key=True
                    screen.fill((255,255,255))