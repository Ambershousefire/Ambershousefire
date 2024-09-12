
import pygame
print("this is a graphing tool for alloy Graphs")
l=900
w=450
screen=pygame.display.set_mode((l,w))
mintemp=int(input("min tempture"))
maxtemp=int(input("max tempture"))
running=True
white=(255,255,255)
gray=(128,128,128)
black=(0,0,0)
per=0
xgrid=0
ygrid=0
H=0
f=0
if maxtemp<mintemp:
    running=False
    print("cheak if you have your numbers the right way around")
maxtemp-mintemp/10==H
H+int(H)
num=0
screen.fill(white)
while running==True:
    

    
    while xgrid<450:
        pygame.draw.line(screen,gray,(0,xgrid),(l,xgrid),(1))
        xgrid+=10
        
    while ygrid<900:
        pygame.draw.line(screen,gray,(ygrid,0),(ygrid,w),(1))
        ygrid+=10
    pygame.draw.line(screen,black,(0,440),(l,440),(5))
    pygame.draw.line(screen,black,(10,w),(10,0),(5))
    while per<900:
        pygame.draw.line(screen,black,(per,430),(per,w))
        per+=90
        
    if ygrid==900:
        ygrid=0
        while ygrid<430:
            pygame.draw.line(screen,black,(5,num+H),(0,num+H))
            num+=10
            ygrid+=10
        
    
        
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             running = False

pygame.quit()