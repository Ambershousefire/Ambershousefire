
# import the pygame module 
import pygame 
# Define the background colour 
# using RGB color coding. 

delay=5
lc=(0,0,0) 
lc2=(255,255,255)
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((300, 300))


# Set the caption of the screen 
pygame.display.set_caption('graph') 

# Fill the background colour to the screen 
screen.fill(lc2)

pygame.draw.line(screen,lc,(100,0),(100,300))
pygame.draw.line(screen,lc,(200,0),(200,300))
pygame.draw.line(screen,lc,(0,100),(300,100))
pygame.draw.line(screen,lc,(0,200),(300,200))
def O(lc, screen,z):
    pygame.draw.circle(screen,lc,(z,z),(50))
    pygame.draw.circle(screen,lc2,(z,z),(45))

def X(x1, x2, x4, y1, y2, y3, y4, lc, screen):
    pygame.draw.line(screen,lc,(x1,y1),(x2,y2),(5)) 
    pygame.draw.line(screen,lc,(x2,y3),(x4,y4),(5))

def Button(x,y,appclick):
    inboundingbox = False
    pygame.draw.rect(window, P3, (x, y, 150, 150))
    pygame.draw.rect(window, P4, (x + 5, y + 5, 140, 140))
    
    if mousex >= x and mousey >= y and mousex <= (x + 150) and mousey <= (y + 150):
        inboundingbox = True


# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

# game loop 
while running: 
    pygame.time.delay(delay)
    #mouse = pygame.mouse.get_pos()
    mousex, mousey = pygame.mouse.get_pos()
    
# for loop through the event queue
    for event in pygame.event.get():
         if pygame.MOUSEBUTTONDOWN:
             
         X(x1, x2, x4, y1, y2, y3, y4, lc, screen)
         O(lc, screen,z)
         if event.type == pygame.QUIT: 
             running = False
             pygame.quit()

