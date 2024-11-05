
import pygame
file = open("projects\\games\\win_rate.txt","a")
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
row=[]
pos=[]
while len(pos)<50:
    pos.append(bool)
    row.append(1)
togle=False

def token(i,truth):
    if row[i]==2:
        pos[i*6]=truth
    elif row[i]==3:
        pos[i*6+1]=truth
    elif row[i]==4:
        pos[i*6+2]=truth
    elif row[i]==5:
        pos[i*6+3]=truth
    elif row[i]==6:
        pos[i*6+4]=truth
    elif row[i]==7:
        pos[i*6+5]=truth
    y=0

def line_up(sort,row,list,running):
    if list[row]==sort and list[row+1]==sort and list[row+2]==sort and list[row+3]==sort:
        running=False
    elif list[row+1]==sort and list[row+2]==sort and list[row+3]==sort and list[row+4]==sort:
        running=False
    elif list[row+2]==sort and list[row+3]==sort and list[row+4]==sort and list[row+5]==sort:
        running=False
    return running

def up_di(sort,row,list,running):
    if list[row]==sort and list[row+7]==sort and list[row+14]==sort and list[row+21]==sort:
        running=False
    elif list[row+1]==sort and list[row+8]==sort and list[row+15]==sort and list[row+22]==sort:
        running=False
    elif list[row+2]==sort and list[row+9]==sort and list[row+16]==sort and list[row+23]==sort:
        running=False
    return running

def down_di(sort,row,list,running):
    if list[row+5]==sort and list[row+10]==sort and list[row+15]==sort and list[row+20]==sort:
        running=False
    elif list[row+4]==sort and list[row+9]==sort and list[row+14]==sort and list[row+19]==sort:
        running=False
    elif list[row+3]==sort and list[row+8]==sort and list[row+13]==sort and list[row+18]==sort:
        running=False
    return running

def line_flat(sort,row,list,running):
    if list[row]==sort and list[row+6]==sort and list[row+12]==sort and list[row+18]==sort:
        running=False
    elif list[row+1]==sort and list[row+7]==sort and list[row+13]==sort and list[row+19]==sort:
        running=False
    elif list[row+2]==sort and list[row+8]==sort and list[row+14]==sort and list[row+20]==sort:
        running=False
    elif list[row+3]==sort and list[row+9]==sort and list[row+15]==sort and list[row+21]==sort:
        running=False
    elif list[row+4]==sort and list[row+10]==sort and list[row+16]==sort and list[row+22]==sort:
        running=False
    elif list[row+5]==sort and list[row+11]==sort and list[row+17]==sort and list[row+23]==sort:
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
                if x==40:
                        i=0
                elif x==120:
                        i=1
                elif x==200:
                        i=2
                elif x==280:
                        i=3
                elif x==360:
                        i=4
                elif x==440:
                        i=5
                elif x==520:
                        i=6
                if togle:
                    togle=False
                    y=420-65*row[i]
                    pygame.draw.circle(screen,red,(x,y),(30))
                    row[i]=row[i]+1
                    token(i,True)
                    
                else:
                    togle=True
                    y=420-65*row[i]
                    pygame.draw.circle(screen,yellow,(x,y),(30))
                    row[i]=row[i]+1
                    token(i,False)
                        
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

    if row[0]>6 and row[1]>6 and row[2]>6 and row[3]>6 and row[4]>6 and row[5]>6 and row[6]>6:
        running=False
    if togle:
        player=red
    else:
        player=yellow

    pygame.draw.circle(screen,player,(x,30),(20))
    pygame.display.flip()
    if running==False:
            file.write("\nconnect four: ")
            if row[0]>6 and row[1]>6 and row[2]>6 and row[3]>6 and row[4]>6 and row[5]>6 and row[6]>6:
                print("Draw")
                file.write("Draw")
            elif togle:
                print("Yellow won")
                file.write("Yellow won")
            else:
                print("Red won")
                file.write("Red won")