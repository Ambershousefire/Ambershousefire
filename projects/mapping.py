
import pygame
screen = pygame.display.set_mode((1000,500))
running = True
delay = (17) #to be around 60fps
screen.fill((255,255,255))# creats a whith screen
floor = True #if true floor is first

while running:
    print(floor,)
    pygame.time.delay(delay)
    if floor: 
        pygame.draw
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:#togle floor
                if floor:
                    floor = False
                else:
                    floor = True
            
    pygame.display.flip()