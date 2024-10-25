
import pygame
l=560
w=420
screen=pygame.display.set_mode((l,w))
pygame.display.set_caption("connect 4 in a row")
blue=(0,125,255)
red=(255,0,0,)
yellow=(255,255,0) 
running=True
screen.fill(blue)
hole=0
x=40
y=30
i=0
r=[]
pos=[]
while len(pos)<50:
    pos.append(bool)
    r.append(1)
togle=False

def token(i,truth):
    if r[i]==2:
        pos[i*6]=truth
    elif r[i]==3:
        pos[i*6+1]=truth
    elif r[i]==4:
        pos[i*6+2]=truth
    elif r[i]==5:
        pos[i*6+3]=truth
    elif r[i]==6:
        pos[i*6+4]=truth
    elif r[i]==7:
        pos[i*6+5]=truth 
    y=0       


def line_up(sort,row,list,running):
    i=0
    i=row
    if list[i]==sort and list[i+1]==sort and list[i+2]==sort and list[i+3]==sort:
        running=False
    elif list[i+1]==sort and list[i+2]==sort and list[i+3]==sort and list[i+4]==sort:
        running=False
    elif list[i+2]==sort and list[i+3]==sort and list[i+4]==sort and list[i+5]==sort:
        running=False
    return running

def up_di(sort,row,list,running):
    i=0
    i=row
    if list[i]==sort and list[i+7]==sort and list[i+14]==sort and list[i+21]==sort:
        running=False
    elif list[i+1]==sort and list[i+8]==sort and list[i+15]==sort and list[i+22]==sort:
        running=False
    elif list[i+2]==sort and list[i+9]==sort and list[i+16]==sort and list[i+23]==sort:
        running=False
    return running

def down_di(sort,row,list,running):
    i=0
    i=row
    if list[i+5]==sort and list[i+10]==sort and list[i+15]==sort and list[i+20]==sort:
        running=False
    elif list[i+4]==sort and list[i+9]==sort and list[i+14]==sort and list[i+19]==sort:
        running=False
    elif list[i+3]==sort and list[i+8]==sort and list[i+13]==sort and list[i+18]==sort:
        running=False
    return running

def line_flat(sort,row,list,running):
    i=0
    i=row
    if list[i]==sort and list[i+6]==sort and list[i+12]==sort and list[i+18]==sort:
        running=False
    elif list[i+1]==sort and list[i+7]==sort and list[i+13]==sort and list[i+19]==sort:
        running=False
    elif list[i+2]==sort and list[i+8]==sort and list[i+14]==sort and list[i+20]==sort:
        running=False
    elif list[i+3]==sort and list[i+9]==sort and list[i+15]==sort and list[i+21]==sort:
        running=False
    elif list[i+4]==sort and list[i+10]==sort and list[i+16]==sort and list[i+22]==sort:
        running=False
    elif list[i+5]==sort and list[i+11]==sort and list[i+17]==sort and list[i+23]==sort:
        running=False
    return running

while hole<43:
        if x>l:
            x=40
        pygame.draw.circle(screen,(255,255,255),(x,y),(30))
        x+=80
        if hole == 7:
            y+=65
        elif hole == 14:
            y+=65
        elif hole == 21:
            y+=65
        elif hole == 28:
            y+=65
        elif hole == 35:
            y+=65
        hole+=1
x=40
y=30
while running:
    if x<40:
        x=520
    elif x>560:
        x=40
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if togle:
                    togle=False
                    if x==40:
                        y=420-65*r[0]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[0]=r[0]+1
                        token(0,True)

                    elif x==120:
                        y=420-65*r[1]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[1]=r[1]+1
                        token(1,True)
                        
                    elif x==200:
                        y=420-65*r[2]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[2]=r[2]+1
                        token(2,True)
                        
                    elif x==280:
                        y=420-65*r[3]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[3]=r[3]+1
                        token(3,True)
                        
                    elif x==360:
                        y=420-65*r[4]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[4]=r[4]+1
                        token(4,True)
                        
                    elif x==440:
                        y=420-65*r[5]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[5]=r[5]+1
                        token(5,True)
                        
                    elif x==520:
                        y=420-65*r[6]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[6]=r[6]+1
                        token(6,True)
                        
                else:
                    togle=True
                    if x==40:
                        y=420-65*r[0]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[0]=r[0]+1
                        token(0,False)
                        
                    elif x==120:
                        y=420-65*r[1]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[1]=r[1]+1
                        token(1,False)
                       
                    elif x==200:
                        y=420-65*r[2]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[2]=r[2]+1
                        token(2,False)
                        
                    elif x==280:
                        y=420-65*r[3]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[3]=r[3]+1
                        token(3,False)
                        
                    elif x==360:
                        y=420-65*r[4]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[4]=r[4]+1
                        token(4,False)
                        
                    elif x==440:
                        y=420-65*r[5]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[5]=r[5]+1
                        token(5,False)
                        
                    elif x==520:
                        y=420-65*r[6]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[6]=r[6]+1
                        token(6,False)
                        
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                pygame.draw.circle(screen,(255,255,255),(x,30),(20))
                x-=80
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                pygame.draw.circle(screen,(255,255,255),(x,30),(20))
                x+=80
    while i<42:            
        if i<24:
            running=up_di(True,i,pos,running)
            running=up_di(False,i,pos,running)

            running=down_di(True,i,pos,running)
            running=down_di(False,i,pos,running)

            running=line_flat(True,i,pos,running)
            running=line_flat(False,i,pos,running)

        running=line_up(True,i,pos,running)
        running=line_up(False,i,pos,running)
        i+=6
    i=0

    if r[0]>6 and r[1]>6 and r[2]>6 and r[3]>6 and r[4]>6 and r[5]>6 and r[6]>6:
        running=False    
    if togle:
        player=red
    else:
        player=yellow

    pygame.draw.circle(screen,player,(x,30),(20))
    pygame.display.flip()
    if running==False:
            if r[0]>6 and r[1]>6 and r[2]>6 and r[3]>6 and r[4]>6 and r[5]>6 and r[6]>6:
                print("Draw")
            elif togle:
                print("Yellow won")
            else:
                print("Red won")