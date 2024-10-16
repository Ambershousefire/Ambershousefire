import pygame, random
l=600
screen=pygame.display.set_mode((l,l))
x=0
y=500
x2=l
y2=100
x3=0

h=100
running=True
screen.fill((255,255,255))
while running:
    pygame.draw.lines(screen,(0,0,0),False,((x,l),(x+100,y),(x+100,l)))
    pygame.draw.lines(screen,(0,0,0),False,((x2,l),(x2-100,y2),(x2-100,l)))
    pygame.draw.lines(screen,(0,0,0),False,((l,x2),(y2,x2-100),(l,x2-100)))
    pygame.draw.lines(screen,(0,0,0),False,((l,x),(y,x+100,),(l,x+100)))
    pygame.draw.lines(screen,(0,0,0),False,((x2,l-l),(x2-100,y2),(x2-100,l-l)))
    pygame.draw.lines(screen,(0,0,0),False,((x,l-l),(x+100,y2),(x+100,l-l)))
    pygame.draw.lines(screen,(0,0,0),False,((l-l,x2),(y2 ,x2-100),(l-l,x2-100)))
    pygame.draw.lines(screen,(0,0,0),False,((l-l,x),(y,x+100,),(l-l,x+100)))
    x+=100
    x2-=100
    y+=h/2
    y2-=h/2
    if x>l:
        x=0
    if y>l:
        y=0
    if x2<0:
        x2=l
    if y2<0:
        y2=l
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False