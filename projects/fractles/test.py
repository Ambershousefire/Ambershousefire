import pygame, colour as c
l=500
screen = pygame.display.set_mode((l,l))
i=0
z=0
w=1
running=True
while running:
    i,z=c.mouse_pos_local(w)
    c.square(screen,5,i,z,10)
    pygame.display.flip()
    c.end