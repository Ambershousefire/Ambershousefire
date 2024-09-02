
# import the pygame module 
import pygame 
x=0
# Define the background colour 
# using RGB color coding. 
background_colour = (255, 255, 255)
lc=(0,0,0) 

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((300, 300))


# Set the caption of the screen 
pygame.display.set_caption('graph') 

# Fill the background colour to the screen 
screen.fill(background_colour)

pygame.draw.line(screen,lc, (150,0), (150,300))
pygame.draw.line(screen,lc, (0,150), (300,150))

# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

# game loop 
while running: 

    
# for loop through the event queue 
    for event in pygame.event.get():

         if event.type == pygame.QUIT: 
             running = False
             pygame.quit()

