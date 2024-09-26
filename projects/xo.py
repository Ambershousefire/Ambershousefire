
import pygame  
# using RGB color coding. 
delay=5

# Define the dimensions of 
# screen object(width,height) 
global AppClick; AppClick = False
global MouseDown; MouseDown = False
global screen
g=bool

k=False
b1,b2,b3,b4,b5,b6,b7,b8,b9=False,False,False,False,False,False,False,False,False
c1,c2,c3,c4,c5,c6,c7,c8,c9=bool,bool,bool,bool,bool,bool,bool,bool,bool
screen = pygame.display.set_mode((300, 300))

# Set the caption of the screen 
pygame.display.set_caption('Tick, Tack, Toe') 

# Fill the background colour to the screen 
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
    #pygame.draw.rect(screen, (x, y, 150, 150))
    #pygame.draw.rect(screen, (x + 5, y + 5, 140, 140))
    
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

# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

# game loop 
while running:
    pygame.time.delay(delay)
    #mouse = pygame.mouse.get_pos()
    mousex, mousey = pygame.mouse.get_pos()
    
#   for loop through the event queue
    for event in pygame.event.get():
        #if pygame.MOUSEBUTTONDOWN:
        #     X(mousex, mousey)
        #     O(mousex, mousey)
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
                if g:
                    g=False
                else:
                    g=True
    if b2==False:
        if MouseDown:
            if mousex<200 and mousex>100 and mousey<100:            
                AppClick,k = Button(100,0,AppClick,k)
                b2=True
                if g:
                    g=False
                else:
                    g=True
    if b3==False:
        if MouseDown:
            if mousex<300 and mousex>200 and mousey<100:
                AppClick,k = Button(200,0,AppClick,k)
                b3=True
                if g:
                    g=False
                else:
                    g=True
    if b4==False:
        if MouseDown:
            if mousex<100 and mousey<200 and mousey>100:
                AppClick,k = Button(0,100,AppClick,k)
                b4=True
                if g:
                    g=False
                else:
                    g=True
    if b5==False:
        if MouseDown:
            if mousex<200 and mousex>100 and mousey<200 and mousey>100:
                AppClick,k = Button(100,100,AppClick,k)
                b5=True
                if g:
                    g=False
                else:
                    g=True
    if b6==False:
        if MouseDown:
            if mousex<300 and mousex>200 and mousey<200 and mousey>100:
                AppClick,k = Button(200,100,AppClick,k)
                b6=True
                if g:
                    g=False
                else:
                    g=True
    if b7==False:
        if MouseDown:
            if mousex<100 and mousey<300 and mousey>200:
                AppClick,k = Button(0,200,AppClick,k)
                b7=True
                if g:
                    g=False
                else:
                    g=True
    if b8==False:
        if MouseDown:
            if mousex<200 and mousex>100 and mousey<300 and mousey>200:
                AppClick,k = Button(100,200,AppClick,k)
                b8=True
                if g:
                    g=False
                else:
                    g=True
    if b9==False:
        if MouseDown:
            if mousex<300 and mousex>200 and mousey<300 and mousey>200:
                AppClick,k = Button(200,200,AppClick,k)
                b9=True
                if g:
                    g=False
                else:
                    g=True
    if b1:
        if g:
            c1=False
        else:
            c1=True
        b1=0
    if b2:
        if g:
            c2=False
        else:
            c2=True
        b2=0
    if b3:
        if g:
            c3=False
        else:
            c3=True
        b3=0
    if b4:
        if g:
            c4=False
        else:
            c4=True
        b4=0
    if b5:
        if g:
            c5=False
        else:
            c5=True
        b5=0
    if b6:
        if g:
            c6=False
        else:
            c6=True
        b6=0
    if b7:
        if g:
            c7=False
        else:
            c7=True
        b7=0
    if b8:
        if g:
            c8=False
        else:
            c8=True
        b8=0
    if b9:
        if g:
            c9=False
        else:
            c9=True
        b9=0
            
            
    if c1==True and c2==True and c3==True:
        running=False
    elif c1==False and c2==False and c3==False:
        running=False
    elif c4==True and c5==True and c6==True:
        running=False
    elif c4==False and c5==False and c6==False:
        running=False
    elif c7==True and c8==True and c9==True:
        running=False
    elif c7==False and c8==False and c9==False:
        running=False
    elif c1==True and c4==True and c7==True:
        running=False
    elif c1==False and c4==False and c7==False:
        running=False
    elif c2==True and c5==True and c8==True:
        running=False
    elif c2==False and c5==False and c8==False:
        running=False
    elif c3==True and c6==True and c9==True:
        running=False
    elif c3==False and c6==False and c9==False:
        running=False
    elif c1==True and c5==True and c9==True:
        running=False
    elif c1==False and c5==False and c9==False:
        running=False
    elif c7==True and c5==True and c3==True:
        running=False
    elif c7==False and c5==False and c3==False:
        running=False
        
    print(c1,c4,c7)

    print(g)
    pygame.display.flip()
print(c1,c2,c3,c4,c5,c6,c7,c8,c9)