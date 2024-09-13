
import pygame

print("this is a graphing tool for alloy Graphs")
print("the max temp on this graph is 500 so your max temp must be less than 500, so insure your numbers are all hole numbers under 500")
v=(input("is the highest temp over 500 (y/n)"))

if v.capitalize().startswith("Y"):
    o=2
else:
    o=1
count=10

sort=(input("are you using this grap for eutetic alloys (y/n)"))

sorttype=False

if sort.capitalize().startswith("Y"):
    start1=int(input("what is the end point for solifcation: "))
    sorttype=True
if sorttype==False:
    start1=int(input("what is the sart point for solidfcation: "))
    start2=int(input("what is the end point for solifcation: "))

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
ef=0
ez=0
num=0
temp=0
xpos=100
x2pos=0
run1=True


screen.fill(white)
while running==True:
    if sorttype:
        while z<count:
            if run1:
                mintemp=int(input("end of solifcation: "))
                mintemp=(w-mintemp)
                start1=(w-start1)
                run1=False
            maxtemp=int(input("sart of solifcation: "))

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
    else:
        while z<count:
            mintemp=int(input("end of soilifaction: "))
            maxtemp=int(input("sart of solifcation: "))
            mintemp=mintemp/o
            maxtemp=maxtemp/o
            mintemp=(w-mintemp)
            maxtemp=(w-maxtemp)
            start1=(start1/o)
            start2=(start2/o)
            start1=(w-start1)
            start2=(w-start2)
            

            if z==0:
                ef=maxtemp
                eg=mintemp
        
        
            if z==0:
                pygame.draw.line(screen,black,(x2pos,start2),(xpos,mintemp),(3))
                pygame.draw.line(screen,black,(x2pos,start1),(xpos,maxtemp),(3))
                xpos+=100
                x2pos+=100
            else:
                pygame.draw.line(screen,black,(xpos,mintemp),(xpos,mintemp),(3))
                pygame.draw.line(screen,black,(x2pos,eg),(xpos,mintemp),(3))
                pygame.draw.line(screen,black,(xpos,maxtemp),(xpos,maxtemp),(3))
                pygame.draw.line(screen,black,(x2pos,ef),(xpos,maxtemp),(3))
                
                ef=maxtemp
                eg=mintemp
                xpos+=100
                x2pos+=100
            z=z+1
            
        
    
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