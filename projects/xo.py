
import pygame  
# using RGB color coding. 
delay=5

# Define the dimensions of 
# screen object(width,height) 
global AppClick; AppClick = False
global MouseDown; MouseDown = False
global screen
k=False

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
                O(x,y)
                    
            else:
                isO=True
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
    
    if MouseDown == False and AppClick == True:
        AppClick = False
    if mousex<100 and mousey <100:
        AppClick,k = Button(0,0,AppClick,k)
    AppClick,k = Button(100,0,AppClick,k)
    AppClick,k = Button(200,0,AppClick,k)
    AppClick,k = Button(0,100,AppClick,k)
    AppClick,k = Button(100,100,AppClick,k)
    AppClick,k = Button(200,100,AppClick,k)
    AppClick,k = Button(0,200,AppClick,k)
    AppClick,k = Button(100,200,AppClick,k)
    AppClick,k = Button(200,200,AppClick,k)

    pygame.display.flip()