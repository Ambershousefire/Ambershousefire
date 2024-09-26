
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
r1,r2,r3,r4,r5,r6,r7=1,1,1,1,1,1,1
a1,a2,a3,a4,a5,a6,b1,b2,b3,b4,b5,b6,c1,c2,c3,c4,c5,c6,d1,d2,d3,d4,d5,d6,e1,e2,e3,e4,e5,e6,f1,f2,f3,f4,f5,f6,g1,g2,g3,g4,g5,g6=bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool
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
                        y=420-65*r1
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r1+=1
                        if r1==2:
                            a1=True
                        elif r1==3:
                            a2=True
                        elif r1==4:
                            a3=True
                        elif r1==5:
                            a4=True
                        elif r1==6:
                            a5=True
                        elif r1==7:
                            a6=True
                        

                        y=0
                    elif x==120:
                        y=420-65*r2
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r2+=1
                        if r2==2:
                            b1=True
                        elif r2==3:
                            b2=True
                        elif r2==4:
                            b3=True
                        elif r2==5:
                            b4=True
                        elif r2==6:
                            b5=True
                        elif r2==7:
                            b6=True
                        
                        y=0
                    elif x==200:
                        y=420-65*r3
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r3+=1
                        if r3==2:
                            c1=True
                        elif r3==3:
                            c2=True
                        elif r3==4:
                            c3=True
                        elif r3==5:
                            c4=True
                        elif r3==6:
                            c5=True
                        elif r3==7:
                            c6=True
                        
                        y=0
                    elif x==280:
                        y=420-65*r4
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r4+=1
                        if r4==2:
                            d1=True
                        elif r4==3:
                            d2=True
                        elif r4==4:
                            d3=True
                        elif r4==5:
                            d4=True
                        elif r4==6:
                            d5=True
                        elif r4==7:
                            d6=True
                        
                        y=0
                    elif x==360:
                        y=420-65*r5
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r5+=1
                        if r5==2:
                            e1=True
                        elif r5==3:
                            e2=True
                        elif r5==4:
                            e3=True
                        elif r5==5:
                            e4=True
                        elif r5==6:
                            e5=True
                        elif r5==7:
                            e6=True
                        
                        y=0
                    elif x==440:
                        y=420-65*r6
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r6+=1
                        if r6==2:
                            f1=True
                        elif r6==3:
                            f2=True
                        elif r6==4:
                            f3=True
                        elif r6==5:
                            f4=True
                        elif r6==6:
                            f5=True
                        elif r6==7:
                            f6=True
                        
                        y=0
                    elif x==520:
                        y=420-65*r7
                        pygame.draw.circle(screen,red,(x,y),(30))
                        r7+=1
                        if r7==2:
                            g1=True
                        elif r7==3:
                            g2=True
                        elif r7==4:
                            g3=True
                        elif r7==5:
                            g4=True
                        elif r7==6:
                            g5=True
                        elif r7==7:
                            g6=True
                        
                        y=0
                else:
                    togle=True
                    if x==40:
                        y=420-65*r1
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r1+=1
                        if r1==2:
                            a1=False
                        elif r1==3:
                            a2=False
                        elif r1==4:
                            a3=False
                        elif r1==5:
                            a4=False
                        elif r1==6:
                            a5=False
                        elif r1==7:
                            a6=False
                        
                        y=0
                    elif x==120:
                        y=420-65*r2
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r2+=1
                        if r2==2:
                            b1=False
                        elif r2==3:
                            b2=False
                        elif r2==4:
                            b3=False
                        elif r2==5:
                            b4=False
                        elif r2==6:
                            b5=False
                        elif r2==7:
                            b6=False
                       
                        y=0
                    elif x==200:
                        y=420-65*r3
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r3+=1
                        if r3==2:
                            c1=False
                        elif r3==3:
                            c2=False
                        elif r3==4:
                            c3=False
                        elif r3==5:
                            c4=False
                        elif r3==6:
                            c5=False
                        elif r3==7:
                            c6=False
                        
                        y=0
                    elif x==280:
                        y=420-65*r4
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r4+=1
                        if r4==2:
                            d1=False
                        elif r4==3:
                            d2=False
                        elif r4==4:
                            d3=False
                        elif r4==5:
                            d4=False
                        elif r4==6:
                            d5=False
                        elif r4==7:
                            d6=False
                        
                        y=0
                    elif x==360:
                        y=420-65*r5
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r5+=1
                        if r5==2:
                            e1=False
                        elif r5==3:
                            e2=False
                        elif r5==4:
                            e3=False
                        elif r5==5:
                            e4=False
                        elif r5==6:
                            e5=False
                        elif r5==7:
                            e6=False
                        
                        y=0
                    elif x==440:
                        y=420-65*r6
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r6+=1
                        if r6==2:
                            f1=False
                        elif r6==3:
                            f2=False
                        elif r6==4:
                            f3=False
                        elif r6==5:
                            f4=False
                        elif r6==6:
                            f5=False
                        elif r6==7:
                            f6=False
                        
                        y=0
                    elif x==520:
                        y=420-65*r7
                        pygame.draw.circle(screen,yellow,(x,y),(30))
                        r7+=1
                        if r7==2:
                            g1=False
                        elif r7==3:
                            g2=False
                        elif r7==4:
                            g3=False
                        elif r7==5:
                            g4=False
                        elif r7==6:
                            g5=False
                        elif r7==7:
                            g6=False
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
    if a1==True and b1==True and c1==True and d1==True:
        running=False
    elif b1==True and c1==True and d1==True and e1==True:
        running=False
    elif c1==True and d1==True and e1==True and f1==True:
        running=False
    elif d1==True and e1==True and f1==True and g1==True:
        running=False
        
    elif a2==True and b2==True and c2==True and d2==True:
        running=False
    elif b2==True and c2==True and d2==True and e2==True:
        running=False
    elif c2==True and d2==True and e2==True and f2==True:
        running=False
    elif d2==True and e2==True and f2==True and g2==True:
        running=False
        
    elif a3==True and b3==True and c3==True and d3==True:
        running=False
    elif b3==True and c3==True and d3==True and e3==True:
        running=False
    elif c3==True and d3==True and e3==True and f3==True:
        running=False
    elif d3==True and e3==True and f3==True and g3==True:
        running=False
        
    elif a4==True and b4==True and c4==True and d4==True:
        running=False
    elif b4==True and c4==True and d4==True and e4==True:
        running=False
    elif c4==True and d4==True and e4==True and f4==True:
        running=False
    elif d4==True and e4==True and f4==True and g4==True:
        running=False
        
    elif a5==True and b5==True and c5==True and d5==True:
        running=False
    elif b5==True and c5==True and d5==True and e5==True:
        running=False
    elif c5==True and d5==True and e5==True and f5==True:
        running=False
    elif d5==True and e5==True and f5==True and g5==True:
        running=False
        
    elif a6==True and b6==True and c6==True and d6==True:
        running=False
    elif b6==True and c6==True and d6==True and e6==True:
        running=False
    elif c6==True and d6==True and e6==True and f6==True:
        running=False
    elif d6==True and e6==True and f6==True and g6==True:
        running=False
    
    
    #up's        
    elif a1==True and  a2 ==True and a3==True and a4==True:
        running=False
    elif a2==True and  a3 ==True and a4==True and a4==True:
        running=False
    elif a3==True and  a4 ==True and a5==True and a6==True:
        running=False
        
    elif b1==True and  b2 ==True and b3==True and b4==True:
        running=False
    elif b2==True and  b3 ==True and b4==True and b5==True:
        running=False
    elif b3==True and  b4 ==True and b5==True and b6==True:
        running=False
    
    elif c1==True and  c2 ==True and c3==True and c4==True:
        running=False
    elif c2==True and  c3 ==True and c4==True and c5==True:
        running=False
    elif c3==True and  c4 ==True and c5==True and c6==True:
        running=False
    
    elif d1==True and  d2 ==True and d3==True and d4==True:
        running=False
    elif d2==True and  d3 ==True and d4==True and d5==True:
        running=False
    elif d3==True and  d4 ==True and d5==True and d6==True:
        running=False
    
    elif e1==True and  e2 ==True and e3==True and e4==True:
        running=False
    elif e2==True and  e3 ==True and e4==True and e5==True:
        running=False
    elif e3==True and  e4 ==True and e5==True and e6==True:
        running=False
    
    elif f1==True and  f2 ==True and f3==True and f4==True:
        running=False
    elif f2==True and  f3 ==True and f4==True and f5==True:
        running=False
    elif f3==True and  f4 ==True and f5==True and f6==True:
        running=False
        
    elif g1==True and  g2 ==True and g3==True and g4==True:
        running=False
    elif g2==True and  g3 ==True and g4==True and g5==True:
        running=False
    elif g3==True and  g4 ==True and g5==True and g6==True:
        running=False
        
    #posative diagnels 
    elif a1==True and b2 == True and c3 == True and d3 == True: 
        running=False
    elif a2 == True and b3 == True and c3 == True and d5 == True:
        running = False
    elif a3 == True and b3== True and c5 == True and d6 == True:
        running = False
        
    elif b1==True and c2 == True and d3 == True and e3 == True: 
        running=False
    elif b2 == True and c3 == True and d3 == True and e5 == True:
        running = False
    elif b3 == True and c3== True and d5 == True and e6 == True:
        running = False
        
    elif c1 == True and d2 == True and e3 == True and f3 == True: 
        running=False
    elif c2 == True and d3 == True and e3 == True and f5 == True:
        running = False
    elif c3 == True and d3== True and e5 == True and f6 == True:
        running = False
    
    elif d1==True and e2 == True and f3 == True and g3 == True: 
        running=False
    elif d2 == True and e3 == True and f3 == True and g5 == True:
        running = False
    elif d3 == True and e3== True and f5 == True and g6 == True:
        running = False
    
    #negative  diagnels 
    elif a6==True and b5 == True and c4 == True and d3 == True: 
        running=False
    elif a5 == True and b4 == True and c3 == True and d2 == True:
        running = False
    elif a4 == True and b3== True and c2 == True and d1 == True:
        running = False
        
    elif b6==True and c5 == True and d4 == True and e3 == True: 
        running=False
    elif b5 == True and c4 == True and d3 == True and e2 == True:
        running = False
    elif b4 == True and c3== True and d2 == True and e1 == True:
        running = False
        
    elif c6==True and d5 == True and e4 == True and f3 == True: 
        running=False
    elif c5 == True and d4 == True and e3 == True and f2 == True:
        running = False
    elif c4 == True and d3== True and e2 == True and f1 == True:
        running = False
    
    elif d6==True and e5 == True and f4 == True and g3 == True: 
        running=False
    elif d5 == True and e4 == True and f3 == True and g2 == True:
        running = False
    elif d4 == True and e3== True and f2 == True and g1 == True:
        running = False
    
    elif a1==False and b1==False and c1==False and d1==False:
        running=False
    elif b1==False and c1==False and d1==False and e1==False:
        running=False
    elif c1==False and d1==False and e1==False and f1==False:
        running=False
    elif d1==False and e1==False and f1==False and g1==False:
        running=False
        
    elif a2==False and b2==False and c2==False and d2==False:
        running=False
    elif b2==False and c2==False and d2==False and e2==False:
        running=False
    elif c2==False and d2==False and e2==False and f2==False:
        running=False
    elif d2==False and e2==False and f2==False and g2==False:
        running=False
        
    elif a3==False and b3==False and c3==False and d3==False:
        running=False
    elif b3==False and c3==False and d3==False and e3==False:
        running=False
    elif c3==False and d3==False and e3==False and f3==False:
        running=False
    elif d3==False and e3==False and f3==False and g3==False:
        running=False
        
    elif a4==False and b4==False and c4==False and d4==False:
        running=False
    elif b4==False and c4==False and d4==False and e4==False:
        running=False
    elif c4==False and d4==False and e4==False and f4==False:
        running=False
    elif d4==False and e4==False and f4==False and g4==False:
        running=False
        
    elif a5==False and b5==False and c5==False and d5==False:
        running=False
    elif b5==False and c5==False and d5==False and e5==False:
        running=False
    elif c5==False and d5==False and e5==False and f5==False:
        running=False
    elif d5==False and e5==False and f5==False and g5==False:
        running=False
        
    elif a6==False and b6==False and c6==False and d6==False:
        running=False
    elif b6==False and c6==False and d6==False and e6==False:
        running=False
    elif c6==False and d6==False and e6==False and f6==False:
        running=False
    elif d6==False and e6==False and f6==False and g6==False:
        running=False
    
    
    #up's        
    elif a1==False and  a2 ==False and a3==False and a4==False:
        running=False
    elif a2==False and  a3 ==False and a4==False and a4==False:
        running=False
    elif a3==False and  a4 ==False and a5==False and a6==False:
        running=False
        
    elif b1==False and  b2 ==False and b3==False and b4==False:
        running=False
    elif b2==False and  b3 ==False and b4==False and b5==False:
        running=False
    elif b3==False and  b4 ==False and b5==False and b6==False:
        running=False
    
    elif c1==False and  c2 ==False and c3==False and c4==False:
        running=False
    elif c2==False and  c3 ==False and c4==False and c5==False:
        running=False
    elif c3==False and  c4 ==False and c5==False and c6==False:
        running=False
    
    elif d1==False and  d2 ==False and d3==False and d4==False:
        running=False
    elif d2==False and  d3 ==False and d4==False and d5==False:
        running=False
    elif d3==False and  d4 ==False and d5==False and d6==False:
        running=False
    
    elif e1==False and  e2 ==False and e3==False and e4==False:
        running=False
    elif e2==False and  e3 ==False and e4==False and e5==False:
        running=False
    elif e3==False and  e4 ==False and e5==False and e6==False:
        running=False
    
    elif f1==False and  f2 ==False and f3==False and f4==False:
        running=False
    elif f2==False and  f3 ==False and f4==False and f5==False:
        running=False
    elif f3==False and  f4 ==False and f5==False and f6==False:
        running=False
        
    elif g1==False and  g2 ==False and g3==False and g4==False:
        running=False
    elif g2==False and  g3 ==False and g4==False and g5==False:
        running=False
    elif g3==False and  g4 ==False and g5==False and g6==False:
        running=False
        
    #posative diagnels 
    elif a1==False and b2 == False and c3 == False and d4 == False: 
        running=False
    elif a2 == False and b3 == False and c4 == False and d5 == False:
        running = False
    elif a3 == False and b3== False and c5 == False and d6 == False:
        running = False
        
    elif b1==False and c2 == False and d3 == False and e4 == False: 
        running=False
    elif b2 == False and c3 == False and d4 == False and e5 == False:
        running = False
    elif b3 == False and c3== False and d5 == False and e6 == False:
        running = False
        
    elif c1==False and d2 == False and e3 == False and f4 == False: 
        running=False
    elif c2 == False and d3 == False and e4 == False and f5 == False:
        running = False
    elif c3 == False and d3== False and e5 == False and f6 == False:
        running = False
    
    elif d1==False and e2 == False and f3 == False and g3 == False: 
        running=False
    elif d2 == False and e3 == False and f4 == False and g4 == False:
        running = False
    elif d3 == False and e3== False and f5 == False and g6 == False:
        running = False
    
    #negative  diagnels 
    elif a6==False and b5 == False and c4 == False and d3 == False: 
        running=False
    elif a5 == False and b4 == False and c3 == False and d2 == False:
        running = False
    elif a4 == False and b3== False and c2 == False and d1 == False:
        running = False
        
    elif b6==False and c5 == False and d4 == False and e3 == False: 
        running=False
    elif b5 == False and c4 == False and d3 == False and e2 == False:
        running = False
    elif b4 == False and c3== False and d2 == False and e1 == False:
        running = False
        
    elif c6==False and d5 == False and e4 == False and f3 == False: 
        running=False
    elif c5 == False and d4 == False and e3 == False and f2 == False:
        running = False
    elif c4 == False and d3== False and e2 == False and f1 == False:
        running = False
    
    elif d6==False and e5 == False and f4 == False and g3 == False: 
        running=False
    elif d5 == False and e4 == False and f3 == False and g2 == False:
        running = False
    elif d4 == False and e3== False and f2 == False and g1 == False:
        running = False

    elif r1>6 and r2>6 and r3>6 and r4>6 and r5>6 and r6>6 and r7>6:
        running=False    
    if togle:
        player=red
    else:
        player=yellow

    pygame.draw.circle(screen,player,(x,30),(20ddddddddddd))
    pygame.display.flip()
    if running==False:
            if r1>6 and r2>6 and r3>6 and r4>6 and r5>6 and r6>6 and r7>6:
                print("thats a draw!!")
            elif togle:
                print("  yellow won!!")
            else:
                print("     red won!!")
#if your reading this, dont cry my code is over yes i know its so bad that its might possably be the worst possable code on earth that works but it works 