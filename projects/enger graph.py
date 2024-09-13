
import pygame
print("this is a graphing tool for alloy Graphs")
print("the max temp on this graph is 500 so your max temp must be less than 500, so insure your numbers are all hole numbers under 500")
start1=int(input("what is the satring point for liqufaction: "))
count=int(input("how many points: "))

l=1000
w=500
screen=pygame.display.set_mode((l,w))



running=True
white=(255,255,255)
gray=(128,128,128)
black=(0,0,0)
per=0
xgrid=0
ygrid=0
f=0
z=0
num=0
temp=0
xpos=100
x2pos=0
run1=True


screen.fill(white)
while running==True:
    while z<count:
        if run1:
            mintemp=int(input("Min temperture: "))
            mintemp=(w-mintemp)
            start1=(w-start1)
            run1=False
        maxtemp=int(input("Max temperture: "))

        maxtemp=(w-maxtemp)

        if z==0:
            f=maxtemp
    
        pygame.draw.line(screen,black,(x2pos,mintemp),(xpos,mintemp),(3))
        if z==0:
            pygame.draw.line(screen,black,(x2pos,start1),(xpos,maxtemp),(3))
            xpos+=100
            x2pos+=100
        else:
            pygame.draw.line(screen,black,(xpos,maxtemp),(xpos,maxtemp),(3))
            pygame.draw.line(screen,black,(x2pos,f),(xpos,maxtemp),(3))
            
            f=maxtemp
            xpos+=100
            x2pos+=100
        z=z+1
        pygame.display.flip()
    
    while xgrid<w:
        pygame.draw.line(screen,gray,(0,xgrid),(l,xgrid),(1))
        xgrid+=10
        
    while ygrid<1000:
        pygame.draw.line(screen,gray,(ygrid,0),(ygrid,w),(1))
        ygrid+=10
    pygame.draw.line(screen,black,(0,w-10),(l,w-10),(5))
    pygame.draw.line(screen,black,(10,w),(10,0),(5))
    while per<1000:
        pygame.draw.line(screen,black,(per,w-20),(per,w))
        per+=100
        
        while temp<430:
            pygame.draw.line(screen,black,(5,num),(0,num))
            num+=10
            temp+=10
    
        
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
        if event.type == pygame.QUIT: 
            running = False

pygame.quit()