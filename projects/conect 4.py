
import pygame
l=560
w=420
screen=pygame.display.set_mode((l,w))
pygame.display.set_caption("connect 4 in pos row")
blue=(0,125,255)
red=(255,0,0,)
yellow=(255,255,0)
global running
running=True
screen.fill(blue)
hole=0
x=40
y=30
i=-1
r=[1,1,1,1,1,1,1,1]
pos=[]
while len(pos)<41:
    pos.append(bool)
togle=False
def line_up(sort,row,list,running):
    i=0
    i=row
    if list[i]==sort and list[i+1]==sort and list[i+2]==sort and list[i+3]==sort:
        running=False
    if list[i+1]==sort and list[i+2]==sort and list[i+3]==sort and list[i+4]==sort:
        running=False
    if list[i+2]==sort and list[i+3]==sort and list[i+4]==sort and list[i+5]==sort:
        running=False
    return running

def up_di(sort,row,list,running):
    i=0
    i=row
    if list[i]==sort and list[i+7]==sort and list[i+14]==sort and list[i+21]==sort:
        running=False
    if list[i+1]==sort and list[i+8]==sort and list[i+15]==sort and list[i+22]==sort:
        running=False
    if list[i+2]==sort and list[i+9]==sort and list[i+16]==sort and list[i+23]==sort:
        running=False
    return running

def down_di(sort,row,list,running):
    i=0
    i=row
    if list[i+5]==sort and list[i+10]==sort and list[i+15]==sort and list[i+20]==sort:
        running=False
    if list[i+4]==sort and list[i+9]==sort and list[i+14]==sort and list[i+19]==sort:
        running=False
    if list[i+3]==sort and list[i+8]==sort and list[i+13]==sort and list[i+18]==sort:
        running=False
    return running

def line_flat(sort,row,list,running):
    i=0
    i=row
    if list[i]==sort and list[i+6]==sort and list[i+12]==sort and list[i+18]==sort:
        running=False
    if list[i+1]==sort and list[i+7]==sort and list[i+13]==sort and list[i+19]==sort:
        running=False
    if list[i+2]==sort and list[i+8]==sort and list[i+14]==sort and list[i+20]==sort:
        running=False
    if list[i+3]==sort and list[i+9]==sort and list[i+15]==sort and list[i+21]==sort:
        running=False
    if list[i+4]==sort and list[i+10]==sort and list[i+16]==sort and list[i+22]==sort:
        running=False
    if list[i+5]==sort and list[i+11]==sort and list[i+17]==sort and list[i+23]==sort:
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
                        if r[0]==2:
                            pos[0]=True
                        elif r[0]==3:
                            pos[1]=True
                        elif r[0]==4:
                            pos[2]=True
                        elif r[0]==5:
                            pos[3]=True
                        elif r[0]==6:
                            pos[4]=True
                        elif r[0]==7:
                            pos[5]=True
                        

                        y=0
                    elif x==120:
                        y=420-65*r[1]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[1]=r[1]+1
                        if r[1]==2:
                            pos[6]=True
                        elif r[1]==3:
                            pos[7]=True
                        elif r[1]==4:
                            pos[8]=True
                        elif r[1]==5:
                            pos[9]=True
                        elif r[1]==6:
                            pos[10]=True
                        elif r[1]==7:
                            pos[11]=True
                        
                        y=0
                    elif x==200:
                        y=420-65*r[2]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[2]=r[2]+1
                        if r[2]==2:
                            pos[12]=True
                        elif r[2]==3:
                            pos[13]=True
                        elif r[2]==4:
                            pos[14]=True
                        elif r[2]==5:
                            pos[15]=True
                        elif r[2]==6:
                            pos[16]=True
                        elif r[2]==7:
                            pos[17]=True
                        
                        y=0
                    elif x==280:
                        y=420-65*r[3]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[3]=r[3]+1
                        if r[3]==2:
                            pos[18]=True
                        elif r[3]==3:
                            pos[19]=True
                        elif r[3]==4:
                            pos[20]=True
                        elif r[3]==5:
                            pos[21]=True
                        elif r[3]==6:
                            pos[22]=True
                        elif r[3]==7:
                            pos[23]=True
                        
                        y=0
                    elif x==360:
                        y=420-65*r[4]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[4]=r[4]+1
                        if r[4]==2:
                            pos[24]=True
                        elif r[4]==3:
                            pos[25]=True
                        elif r[4]==4:
                            pos[26]=True
                        elif r[4]==5:
                            pos[27]=True
                        elif r[4]==6:
                            pos[28]=True
                        elif r[4]==7:
                            pos[29]=True
                        
                        y=0
                    elif x==440:
                        y=420-65*r[5]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[5]=r[5]+1
                        if r[5]==2:
                            pos[30]=True
                        elif r[5]==3:
                            pos[31]=True
                        elif r[5]==4:
                            pos[32]=True
                        elif r[5]==5:
                            pos[33]=True
                        elif r[5]==6:
                            pos[34]=True
                        elif r[5]==7:
                            pos[35]=True
                        
                        y=0
                    elif x==520:
                        y=420-65*r[6]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[6]=r[6]+1
                        if r[6]==2:
                            pos[36]=True
                        elif r[6]==3:
                            pos[37]=True
                        elif r[6]==4:
                            pos[38]=True
                        elif r[6]==5:
                            pos[39]=True
                        elif r[6]==6:
                            pos[40]=True
                        elif r[6]==7:
                            pos[41]=True
                        
                        y=0
                else:
                    togle=True
                    if x==40:
                        y=420-65*r[0]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[0]=r[0]+1
                        if r[0]==2:
                            pos[0]=False
                        elif r[0]==3:
                            pos[1]=False
                        elif r[0]==4:
                            pos[2]=False
                        elif r[0]==5:
                            pos[3]=False
                        elif r[0]==6:
                            pos[4]=False
                        elif r[0]==7:
                            pos[5]=False
                        
                        y=0
                    elif x==120:
                        y=420-65*r[1]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[1]=r[1]+1
                        if r[1]==2:
                            pos[6]=False
                        elif r[1]==3:
                            pos[7]=False
                        elif r[1]==4:
                            pos[8]=False
                        elif r[1]==5:
                            pos[9]=False
                        elif r[1]==6:
                            pos[10]=False
                        elif r[1]==7:
                            pos[11]=False
                       
                        y=0
                    elif x==200:
                        y=420-65*r[2]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[2]=r[2]+1
                        if r[2]==2:
                            pos[12]=False
                        elif r[2]==3:
                            pos[13]=False
                        elif r[2]==4:
                            pos[14]=False
                        elif r[2]==5:
                            pos[15]=False
                        elif r[2]==6:
                            pos[16]=False
                        elif r[2]==7:
                            pos[17]=False
                        
                        y=0
                    elif x==280:
                        y=420-65*r[3]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[3]=r[3]+1
                        if r[3]==2:
                            pos[18]=False
                        elif r[3]==3:
                            pos[19]=False
                        elif r[3]==4:
                            pos[20]=False
                        elif r[3]==5:
                            pos[21]=False
                        elif r[3]==6:
                            pos[22]=False
                        elif r[3]==7:
                            pos[23]=False
                        
                        y=0
                    elif x==360:
                        y=420-65*r[4]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[4]=r[4]+1
                        if r[4]==2:
                            pos[24]=False
                        elif r[4]==3:
                            pos[25]=False
                        elif r[4]==4:
                            pos[26]=False
                        elif r[4]==5:
                            pos[27]=False
                        elif r[4]==6:
                            pos[28]=False
                        elif r[4]==7:
                            pos[29]=False
                        
                        y=0
                    elif x==440:
                        y=420-65*r[5]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[5]=r[5]+1
                        if r[5]==2:
                            pos[30]=False
                        elif r[5]==3:
                            pos[31]=False
                        elif r[5]==4:
                            pos[32]=False
                        elif r[5]==5:
                            pos[33]=False
                        elif r[5]==6:
                            pos[34]=False
                        elif r[5]==7:
                            pos[35]=False
                        
                        y=0
                    elif x==520:
                        y=420-65*r[6]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[6]=r[6]+1
                        if r[6]==2:
                            pos[36]=False
                        elif r[6]==3:
                            pos[37]=False
                        elif r[6]==4:
                            pos[38]=False
                        elif r[6]==5:
                            pos[39]=False
                        elif r[6]==6:
                            pos[40]=False
                        elif r[6]==7:
                            pos[41]=False
                        y=0
                        
            elif event.key == pygame.K_a:
                pygame.draw.circle(screen,(255,255,255),(x,30),(20))
                x-=80
            elif event.key == pygame.K_d:
                pygame.draw.circle(screen,(255,255,255),(x,30),(20))
                x+=80
            elif event.key == pygame.K_LEFT:
                pygame.draw.circle(screen,(255,255,255),(x,30),(20))
                x-=80
            elif event.key == pygame.K_RIGHT:
                pygame.draw.circle(screen,(255,255,255),(x,30),(20))
                x+=80

    running=up_di(True,0,pos,running)
    running=up_di(False,0,pos,running)
    running=up_di(True,6,pos,running)
    running=up_di(False,6,pos,running)
    running=up_di(True,12,pos,running)
    running=up_di(False,12,pos,running)
    running=up_di(True,18,pos,running)
    running=up_di(False,18,pos,running)

    running=down_di(True,0,pos,running)
    running=down_di(False,0,pos,running)
    running=down_di(True,6,pos,running)
    running=down_di(False,6,pos,running)
    running=down_di(True,12,pos,running)
    running=down_di(False,12,pos,running)
    running=down_di(True,18,pos,running)
    running=down_di(False,18,pos,running)

    running=line_up(True,0,pos,running)
    running=line_up(False,0,pos,running)
    running=line_up(True,6,pos,running)
    running=line_up(False,6,pos,running)
    running=line_up(True,12,pos,running)
    running=line_up(False,12,pos,running)
    running=line_up(True,18,pos,running)
    running=line_up(False,18,pos,running)
    running=line_up(True,24,pos,running)
    running=line_up(False,24,pos,running)
    running=line_up(True,30,pos,running)
    running=line_up(False,30,pos,running)
    running=line_up(True,36,pos,running)
    running=line_up(False,36,pos,running)    

    running=line_flat(True,0,pos,running)
    running=line_flat(False,0,pos,running)
    running=line_flat(True,6,pos,running)
    running=line_flat(False,6,pos,running)
    running=line_flat(True,12,pos,running)
    running=line_flat(False,12,pos,running)
    running=line_flat(True,18,pos,running)
    running=line_flat(False,18,pos,running)


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
                print("thats pos draw!!")
            elif togle:
                print("  yellow won!!")
            else:
                print("     red won!!")