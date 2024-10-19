import pygame, colour as c
l=500
screen = pygame.display.set_mode((l,l))
i=0
z=0
w=1
running=True
while running:
    i,z=c.mouse_pos_local(w)
    pygame.display.flip()