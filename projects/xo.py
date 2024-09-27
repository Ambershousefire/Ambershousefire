
import pygame  
global AppClick; AppClick = False
global MouseDown; MouseDown = False
global screen
o="O wins"
Y="X wins"
k=False
b1,b2,b3,b4,b5,b6,b7,b8,b9=False,False,False,False,False,False,False,False,False
c1,c2,c3,c4,c5,c6,c7,c8,c9=6,6,6,6,6,6,6,6,6
screen = pygame.display.set_mode((300, 300))

pygame.display.set_caption('Tick, Tack, Toe') 
 
screen.fill((255,255,255))

pygame.draw.line(screen,(0,0,0),(100,0),(100,300),(3))
pygame.draw.line(screen,(0,0,0),(200,0),(200,300),(3))
pygame.draw.line(screen,(0,0,0),(0,100),(300,100),(3))
pygame.draw.line(screen,(0,0,0),(0,200),(300,200),(3))
def O (mousex,mousey):

        pygame.draw.circle(screen,(255,8,48),(mousex+50,mousey+50),(40))
        pygame.draw.circle(screen,(255,255,255),(mousex+50,mousey+50),(35))
    
def X (mousex, mousey):
      
        pygame.draw.line(screen,(48,8,255),(mousex+10,mousey+10),(mousex+90,mousey+90),(5)) 
        pygame.draw.line(screen,(48,8,255),(mousex+10,mousey+90),(mousex+90,mousey+10),(5))
    
def Button(x, y, AppClick, isO):
    inboundingbox = False
    
    if mousex >= x and mousey >= y and mousex <= (x + 100) and mousey <= (y + 100):
        inboundingbox = True
        
    if MouseDown and inboundingbox and AppClick == False:
            if isO:
                isO=False
                g=False
                O(x,y)
                    
            else:
                isO=True
                g=True
                X(x,y)
                
            AppClick = True
    return AppClick, isO

pygame.display.flip() 

running = True

while running:
    mousex, mousey = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             running = False
             pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseDown = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            MouseDown = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running=False
    
    if MouseDown == False and AppClick == True:
        AppClick = False
        
    if b1==False:
        if MouseDown:
            if mousex<100 and mousey<100:
                AppClick,k = Button(0,0,AppClick,k)
                b1=True
                MouseDown=False
    if b2==False:
        if MouseDown:
            if mousex<200 and mousex>100 and mousey<100:            
                AppClick,k = Button(100,0,AppClick,k)
                b2=True
                MouseDown=False
    if b3==False:
        if MouseDown:
            if mousex<300 and mousex>200 and mousey<100:
                AppClick,k = Button(200,0,AppClick,k)
                b3=True
                MouseDown=False
    if b4==False:
        if MouseDown:
            if mousex<100 and mousey<200 and mousey>100:
                AppClick,k = Button(0,100,AppClick,k)
                b4=True
                MouseDown=False
    if b5==False:
        if MouseDown:
            if mousex<200 and mousex>100 and mousey<200 and mousey>100:
                AppClick,k = Button(100,100,AppClick,k)
                b5=True
                MouseDown=False
    if b6==False:
        if MouseDown:
            if mousex<300 and mousex>200 and mousey<200 and mousey>100:
                AppClick,k = Button(200,100,AppClick,k)
                b6=True
                MouseDown=False
    if b7==False:
        if MouseDown:
            if mousex<100 and mousey<300 and mousey>200:
                AppClick,k = Button(0,200,AppClick,k)
                b7=True
                MouseDown=False
    if b8==False:
        if MouseDown:
            if mousex<200 and mousex>100 and mousey<300 and mousey>200:
                AppClick,k = Button(100,200,AppClick,k)
                b8=True
                MouseDown=False
    if b9==False:
        if MouseDown:
            if mousex<300 and mousex>200 and mousey<300 and mousey>200:
                AppClick,k = Button(200,200,AppClick,k)
                b9=True
                MouseDown=False
    if b1:
        if not b1==6:
            if k:
                c1=False
            else:
                c1=True
            b1=6
    if b2:
        if not b2==6:
            if k:
                c2=False
            else:
                c2=True
            b2=6
    if b3:
        if not b3==6:
            if k:
                c3=False
            else:
                c3=True
            b3=6
    if b4:
        if not b4==6:
            if k:
                c4=False
            else:
                c4=True
            b4=6
    if b5:
        if not b5==6:
            if k:
                c5=False
            else:
                c5=True
            b5=6
    if b6:
        if not b6==6:
            if k:
                c6=False
            else:
                c6=True
            b6=6
    if b7:
        if not b7==6:
            if k:
                c7=False
            else:
                c7=True
            b7=6
    if b8:
        if not b8==6:
            if k:
                c8=False
            else:
                c8=True
            b8=6
    if b9:
        if not b9==6:
            if k:
                c9=False
            else:
                c9=True
            b9=6
            
    if c1==True and c2==True and c3==True:
        running=False
        print(o)
   
    elif c4==True and c5==True and c6==True:
        running=False
        print(o)
   
    elif c7==True and c8==True and c9==True:
        running=False
        print(o)
   
    elif c1==True and c4==True and c7==True:
        running=False
        print(o)
  
    elif c2==True and c5==True and c8==True:
        running=False
        print(o)
        
    elif c3==True and c6==True and c9==True:
        running=False
        print(o)
        
    elif c1==True and c5==True and c9==True:
        running=False
        print(o)
            
    elif c7==True and c5==True and c3==True:
        running=False
        print(o)
        
    elif c1==False and c2==False and c3==False:
        running=False
        print(Y) 
        
    elif c4==False and c5==False and c6==False:
        running=False
        print(Y)
        
    elif c7==False and c8==False and c9==False:
        running=False
        print(Y) 
        
    elif c1==False and c4==False and c7==False:
        running=False
        print(Y)
        
    elif c2==False and c5==False and c8==False:
        running=False
        print(Y) 
          
    elif c3==False and c6==False and c9==False:
        running=False
        print(Y) 
        
    elif c7==False and c5==False and c3==False:
        running=False
        print(Y)
    
    elif c1==False and c5==False and c9==False:
        running=False
        print(Y)
    pygame.display.flip()