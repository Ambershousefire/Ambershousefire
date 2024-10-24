
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
r=[1,1,1,1,1,1,1,1]
a=[bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool]
togle=False
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
                            a[0]=True
                        elif r[0]==3:
                            a[1]=True
                        elif r[0]==4:
                            a[2]=True
                        elif r[0]==5:
                            a[3]=True
                        elif r[0]==6:
                            a[4]=True
                        elif r[0]==7:
                            a[5]=True
                        

                        y=0
                    elif x==120:
                        y=420-65*r[1]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[1]=r[1]+1
                        if r[1]==2:
                            a[6]=True
                        elif r[1]==3:
                            a[7]=True
                        elif r[1]==4:
                            a[8]=True
                        elif r[1]==5:
                            a[9]=True
                        elif r[1]==6:
                            a[10]=True
                        elif r[1]==7:
                            a[11]=True
                        
                        y=0
                    elif x==200:
                        y=420-65*r[2]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[2]=r[2]+1
                        if r[2]==2:
                            a[12]=True
                        elif r[2]==3:
                            a[13]=True
                        elif r[2]==4:
                            a[14]=True
                        elif r[2]==5:
                            a[15]=True
                        elif r[2]==6:
                            a[16]=True
                        elif r[2]==7:
                            a[17]=True
                        
                        y=0
                    elif x==280:
                        y=420-65*r[3]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[3]=r[3]+1
                        if r[3]==2:
                            a[18]=True
                        elif r[3]==3:
                            a[19]=True
                        elif r[3]==4:
                            a[20]=True
                        elif r[3]==5:
                            a[21]=True
                        elif r[3]==6:
                            a[22]=True
                        elif r[3]==7:
                            a[23]=True
                        
                        y=0
                    elif x==360:
                        y=420-65*r[4]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[4]=r[4]+1
                        if r[4]==2:
                            a[24]=True
                        elif r[4]==3:
                            a[25]=True
                        elif r[4]==4:
                            a[26]=True
                        elif r[4]==5:
                            a[27]=True
                        elif r[4]==6:
                            a[28]=True
                        elif r[4]==7:
                            a[29]=True
                        
                        y=0
                    elif x==440:
                        y=420-65*r[5]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[5]=r[5]+1
                        if r[5]==2:
                            a[29]=True
                        elif r[5]==3:
                            a[30]=True
                        elif r[5]==4:
                            a[31]=True
                        elif r[5]==5:
                            a[33]=True
                        elif r[5]==6:
                            a[34]=True
                        elif r[5]==7:
                            a[35]=True
                        
                        y=0
                    elif x==520:
                        y=420-65*r[6]
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r[6]=r[6]+1
                        if r[6]==2:
                            a[36]=True
                        elif r[6]==3:
                            a[37]=True
                        elif r[6]==4:
                            a[38]=True
                        elif r[6]==5:
                            a[39]=True
                        elif r[6]==6:
                            a[40]=True
                        elif r[6]==7:
                            a[41]=True
                        
                        y=0
                else:
                    togle=True
                    if x==40:
                        y=420-65*r[0]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[0]=r[0]+1
                        if r[0]==2:
                            a[0]=False
                        elif r[0]==3:
                            a[1]=False
                        elif r[0]==4:
                            a[2]=False
                        elif r[0]==5:
                            a[3]=False
                        elif r[0]==6:
                            a[4]=False
                        elif r[0]==7:
                            a[5]=False
                        
                        y=0
                    elif x==120:
                        y=420-65*r[1]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[1]=r[1]+1
                        if r[1]==2:
                            a[6]=False
                        elif r[1]==3:
                            a[7]=False
                        elif r[1]==4:
                            a[8]=False
                        elif r[1]==5:
                            a[9]=False
                        elif r[1]==6:
                            a[10]=False
                        elif r[1]==7:
                            a[11]=False
                       
                        y=0
                    elif x==200:
                        y=420-65*r[2]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[2]=r[2]+1
                        if r[2]==2:
                            a[12]=False
                        elif r[2]==3:
                            a[13]=False
                        elif r[2]==4:
                            a[14]=False
                        elif r[2]==5:
                            a[15]=False
                        elif r[2]==6:
                            a[16]=False
                        elif r[2]==7:
                            a[17]=False
                        
                        y=0
                    elif x==280:
                        y=420-65*r[3]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[3]=r[3]+1
                        if r[3]==2:
                            a[18]=False
                        elif r[3]==3:
                            a[19]=False
                        elif r[3]==4:
                            a[20]=False
                        elif r[3]==5:
                            a[21]=False
                        elif r[3]==6:
                            a[22]=False
                        elif r[3]==7:
                            a[23]=False
                        
                        y=0
                    elif x==360:
                        y=420-65*r[4]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[4]=r[4]+1
                        if r[4]==2:
                            a[24]=False
                        elif r[4]==3:
                            a[25]=False
                        elif r[4]==4:
                            a[26]=False
                        elif r[4]==5:
                            a[27]=False
                        elif r[4]==6:
                            a[28]=False
                        elif r[4]==7:
                            a[29]=False
                        
                        y=0
                    elif x==440:
                        y=420-65*r[5]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[5]=r[5]+1
                        if r[5]==2:
                            a[30]=False
                        elif r[5]==3:
                            a[31]=False
                        elif r[5]==4:
                            a[32]=False
                        elif r[5]==5:
                            a[33]=False
                        elif r[5]==6:
                            a[34]=False
                        elif r[5]==7:
                            a[35]=False
                        
                        y=0
                    elif x==520:
                        y=420-65*r[6]
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r[6]=r[6]+1
                        if r[6]==2:
                            a[36]=False
                        elif r[6]==3:
                            a[37]=False
                        elif r[6]==4:
                            a[38]=False
                        elif r[6]==5:
                            a[39]=False
                        elif r[6]==6:
                            a[40]=False
                        elif r[6]==7:
                            a[41]=False
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
    #downs
    if a[0]==True and a[6]==True and a[11]==True and a[17]==True:
        running=False
    elif a[6]==True and a[11]==True and a[17]==True and a[23]==True:
        running=False
    elif a[11]==True and a[17]==True and a[23]==True and a[29]==True:
        running=False
    elif a[17]==True and a[23]==True and a[29]==True and a[35]==True:
        running=False
        
    elif a[1]==True and a[7]==True and a[12]==True and a[18]==True:
        running=False
    elif a[7]==True and a[12]==True and a[18]==True and a[24]==True:
        running=False
    elif a[12]==True and a[18]==True and a[24]==True and a[2]==True:
        running=False
    elif a[18]==True and a[24]==True and a[2]==True and a[37]==True:
        running=False
        
    elif a[2]==True and a[7]==True and a[13]==True and a[19]==True:
        running=False
    elif a[7]==True and a[13]==True and a[19]==True and a[25]==True:
        running=False
    elif a[13]==True and a[19]==True and a[25]==True and a[31]==True:
        running=False
    elif a[19]==True and a[25]==True and a[31]==True and a[38]==True:
        running=False
        
    elif a[3]==True and a[8]==True and a[14]==True and a[20]==True:
        running=False
    elif a[8]==True and a[14]==True and a[20]==True and a[26]==True:
        running=False
    elif a[14]==True and a[20]==True and a[26]==True and a[32]==True:
        running=False
    elif a[20]==True and a[26]==True and a[32]==True and a[39]==True:
        running=False
        
    elif a[4]==True and a[9]==True and a[15]==True and a[21]==True:
        running=False
    elif a[9]==True and a[15]==True and a[21]==True and a[27]==True:
        running=False
    elif a[15]==True and a[21]==True and a[27]==True and a[33]==True:
        running=False
    elif a[21]==True and a[27]==True and a[33]==True and a[40]==True:
        running=False
        
    elif a[5]==True and a[10]==True and a[16]==True and a[22]==True:
        running=False
    elif a[10]==True and a[16]==True and a[22]==True and a[28]==True:
        running=False
    elif a[16]==True and a[22]==True and a[28]==True and a[34]==True:
        running=False
    elif a[22]==True and a[28]==True and a[34]==True and a[41]==True:
        running=False


    #up's        
    elif a[0]==True and  a[1] ==True and a[2]==True and a[3]==True:
        running=False
    elif a[1]==True and  a[2] ==True and a[3]==True and a[5]==True:
        running=False
    elif a[2]==True and  a[3] ==True and a[5]==True and a[5]==True:
        running=False
        
    elif a[5]==True and  a[6] ==True and a[7]==True and a[8]==True:
        running=False
    elif a[6]==True and  a[7] ==True and a[8]==True and a[9]==True:
        running=False
    elif a[7]==True and  a[8] ==True and a[9]==True and a[10]==True:
        running=False

    elif a[11]==True and  a[12] ==True and a[13]==True and a[14]==True:
        running=False
    elif a[12]==True and  a[13] ==True and a[14]==True and a[15]==True:
        running=False
    elif a[13]==True and  a[14] ==True and a[15]==True and a[16]==True:
        running=False

    elif a[17]==True and  a[18] ==True and a[19]==True and a[20]==True:
        running=False
    elif a[18]==True and  a[19] ==True and a[20]==True and a[21]==True:
        running=False
    elif a[19]==True and  a[20] ==True and a[21]==True and a[22]==True:
        running=False

    elif a[23]==True and  a[24] ==True and a[25]==True and a[26]==True:
        running=False
    elif a[24]==True and  a[25] ==True and a[26]==True and a[27]==True:
        running=False
    elif a[25]==True and  a[26] ==True and a[27]==True and a[28]==True:
        running=False

    elif a[29]==True and  a[2] ==True and a[31]==True and a[32]==True:
        running=False
    elif a[2]==True and  a[31] ==True and a[32]==True and a[33]==True:
        running=False
    elif a[31]==True and  a[32] ==True and a[33]==True and a[34]==True:
        running=False
        
    elif a[35]==True and  a[37] ==True and a[38]==True and a[39]==True:
        running=False
    elif a[37]==True and  a[38] ==True and a[39]==True and a[40]==True:
        running=False
    elif a[38]==True and  a[39] ==True and a[40]==True and a[41]==True:
        running=False
        
    #posative diagnels 
    elif a[0]==True and a[6] == True and a[13] == True and a[20] == True: 
        running=False
    elif a[1] == True and a[7] == True and a[14] == True and a[21] == True:
        running = False
    elif a[2] == True and a[8]== True and a[15] == True and a[22] == True:
        running = False
        
    elif a[5]==True and a[12] == True and a[19] == True and a[26] == True: 
        running=False
    elif a[6] == True and a[13] == True and a[20] == True and a[27] == True:
        running = False
    elif a[7] == True and a[14]== True and a[21] == True and a[28] == True:
        running = False
        
    elif a[11] == True and a[18] == True and a[25] == True and a[32] == True: 
        running=False
    elif a[12] == True and a[19] == True and a[26] == True and a[33] == True:
        running = False
    elif a[13] == True and a[20]== True and a[27] == True and a[34] == True:
        running = False

    elif a[17]==True and a[24] == True and a[31] == True and a[39] == True: 
        running=False
    elif a[18] == True and a[25] == True and a[32] == True and a[40] == True:
        running = False
    elif a[19] == True and a[26]== True and a[33] == True and a[41] == True:
        running = False

    #negative  diagnels 
    elif a[4]==True and a[9] == True and a[14] == True and a[19] == True: 
        running=False
    elif a[5] == True and a[8] == True and a[13] == True and a[18] == True:
        running = False
    elif a[3] == True and a[7]== True and a[12] == True and a[17] == True:
        running = False
        
    elif a[10]==True and a[15] == True and a[20] == True and a[25] == True: 
        running=False
    elif a[9] == True and a[14] == True and a[19] == True and a[24] == True:
        running = False
    elif a[8] == True and a[13]== True and a[18] == True and a[23] == True:
        running = False
        
    elif a[16]==True and a[21] == True and a[26] == True and a[31] == True: 
        running=False
    elif a[15] == True and a[20] == True and a[25] == True and a[2] == True:
        running = False
    elif a[14] == True and a[19]== True and a[24] == True and a[29] == True:
        running = False

    elif a[22]==True and a[27] == True and a[32] == True and a[38] == True: 
        running=False
    elif a[21] == True and a[26] == True and a[31] == True and a[37] == True:
        running = False
    elif a[20] == True and a[25]== True and a[2] == True and a[35] == True:
        running = False

    elif a[0]==False and a[5]==False and a[11]==False and a[17]==False:
        running=False
    elif a[5]==False and a[11]==False and a[17]==False and a[23]==False:
        running=False
    elif a[11]==False and a[17]==False and a[23]==False and a[29]==False:
        running=False
    elif a[17]==False and a[23]==False and a[29]==False and a[35]==False:
        running=False
        
    elif a[1]==False and a[6]==False and a[12]==False and a[18]==False:
        running=False
    elif a[6]==False and a[12]==False and a[18]==False and a[24]==False:
        running=False
    elif a[12]==False and a[18]==False and a[24]==False and a[30]==False:
        running=False
    elif a[18]==False and a[24]==False and a[30]==False and a[37]==False:
        running=False
        
    elif a[2]==False and a[7]==False and a[13]==False and a[19]==False:
        running=False
    elif a[7]==False and a[13]==False and a[19]==False and a[25]==False:
        running=False
    elif a[13]==False and a[19]==False and a[25]==False and a[31]==False:
        running=False
    elif a[19]==False and a[25]==False and a[31]==False and a[38]==False:
        running=False
        
    elif a[3]==False and a[8]==False and a[14]==False and a[20]==False:
        running=False
    elif a[8]==False and a[14]==False and a[20]==False and a[26]==False:
        running=False
    elif a[14]==False and a[20]==False and a[26]==False and a[32]==False:
        running=False
    elif a[20]==False and a[26]==False and a[32]==False and a[39]==False:
        running=False
        
    elif a[4]==False and a[9]==False and a[15]==False and a[21]==False:
        running=False
    elif a[9]==False and a[15]==False and a[21]==False and a[27]==False:
        running=False
    elif a[15]==False and a[21]==False and a[27]==False and a[33]==False:
        running=False
    elif a[21]==False and a[27]==False and a[33]==False and a[40]==False:
        running=False
        
    elif a[5]==False and a[10]==False and a[16]==False and a[22]==False:
        running=False
    elif a[10]==False and a[16]==False and a[22]==False and a[28]==False:
        running=False
    elif a[16]==False and a[22]==False and a[28]==False and a[34]==False:
        running=False
    elif a[22]==False and a[28]==False and a[34]==False and a[41]==False:
        running=False


    #up's        
    elif a[0]==False and  a[1] ==False and a[2]==False and a[3]==False:
        running=False
    elif a[1]==False and  a[2] ==False and a[3]==False and a[5]==False:
        running=False
    elif a[2]==False and  a[3] ==False and a[5]==False and a[5]==False:
        running=False
        
    elif a[5]==False and  a[6] ==False and a[7]==False and a[8]==False:
        running=False
    elif a[6]==False and  a[7] ==False and a[8]==False and a[9]==False:
        running=False
    elif a[7]==False and  a[8] ==False and a[9]==False and a[10]==False:
        running=False

    elif a[11]==False and  a[12] ==False and a[13]==False and a[14]==False:
        running=False
    elif a[12]==False and  a[13] ==False and a[14]==False and a[15]==False:
        running=False
    elif a[13]==False and  a[14] ==False and a[15]==False and a[16]==False:
        running=False

    elif a[17]==False and  a[18] ==False and a[19]==False and a[20]==False:
        running=False
    elif a[18]==False and  a[19] ==False and a[20]==False and a[21]==False:
        running=False
    elif a[19]==False and  a[20] ==False and a[21]==False and a[22]==False:
        running=False

    elif a[23]==False and  a[24] ==False and a[25]==False and a[26]==False:
        running=False
    elif a[24]==False and  a[25] ==False and a[26]==False and a[27]==False:
        running=False
    elif a[25]==False and  a[26] ==False and a[27]==False and a[28]==False:
        running=False

    elif a[29]==False and  a[30] ==False and a[31]==False and a[32]==False:
        running=False
    elif a[30]==False and  a[31] ==False and a[32]==False and a[33]==False:
        running=False
    elif a[31]==False and  a[32] ==False and a[33]==False and a[34]==False:
        running=False
        
    elif a[35]==False and  a[37] ==False and a[38]==False and a[39]==False:
        running=False
    elif a[37]==False and  a[38] ==False and a[39]==False and a[40]==False:
        running=False
    elif a[38]==False and  a[39] ==False and a[40]==False and a[41]==False:
        running=False
        
    #posative diagnels 
    elif a[0]==False and a[6] == False and a[13] == False and a[20] == False: 
        running=False
    elif a[1] == False and a[7] == False and a[14] == False and a[21] == False:
        running = False
    elif a[2] == False and a[8]== False and a[15] == False and a[22] == False:
        running = False
        
    elif a[5]==False and a[12] == False and a[19] == False and a[26] == False: 
        running=False
    elif a[6] == False and a[13] == False and a[20] == False and a[27] == False:
        running = False
    elif a[7] == False and a[14]== False and a[21] == False and a[28] == False:
        running = False
        
    elif a[11]==False and a[18] == False and a[25] == False and a[32] == False: 
        running=False
    elif a[12] == False and a[19] == False and a[26] == False and a[33] == False:
        running = False
    elif a[13] == False and a[20]== False and a[27] == False and a[34] == False:
        running = False

    elif a[17]==False and a[24] == False and a[31] == False and a[39] == False: 
        running=False
    elif a[18] == False and a[25] == False and a[32] == False and a[40] == False:
        running = False
    elif a[19] == False and a[26]== False and a[33] == False and a[41] == False:
        running = False

    #negative  diagnels 
    elif a[4]==False and a[9] == False and a[14] == False and a[19] == False: 
        running=False
    elif a[5] == False and a[8] == False and a[13] == False and a[18] == False:
        running = False
    elif a[3] == False and a[7]== False and a[12] == False and a[17] == False:
        running = False
        
    elif a[10]==False and a[15] == False and a[20] == False and a[25] == False: 
        running=False
    elif a[9] == False and a[14] == False and a[19] == False and a[24] == False:
        running = False
    elif a[8] == False and a[13]== False and a[18] == False and a[23] == False:
        running = False
        
    elif a[16]==False and a[21] == False and a[26] == False and a[31] == False: 
        running=False
    elif a[15] == False and a[20] == False and a[25] == False and a[30] == False:
        running = False
    elif a[14] == False and a[19]== False and a[24] == False and a[29] == False:
        running = False

    elif a[22]==False and a[27] == False and a[32] == False and a[38] == False: 
        running=False
    elif a[21] == False and a[26] == False and a[31] == False and a[37] == False:
        running = False
    elif a[20] == False and a[25]== False and a[30] == False and a[35] == False:
        running = False

    elif r[0]>6 and r[1]>6 and r[2]>6 and r[3]>6 and r[4]>6 and r[5]>6 and r[6]>6:
        running=False    
    if togle:
        player=red
    else:
        player=yellow

    pygame.draw.circle(screen,player,(x,30),(20))
    pygame.display.flip()
    if running==False:
            if r[0]>6 and r[1]>6 and r[2]>6 and r[3]>6 and r[4]>6 and r[5]>6 and r[6]>6:
                print("thats a draw!!")
            elif togle:
                print("  yellow won!!")
            else:
                print("     red won!!")
#if your reading this, dont cry my code is over yes i know its so bad that its might possably be the worst possable code on earth that works but it works  