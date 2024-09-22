
import pygame
bord=pygame.display.set_mode((62*8,62*8))
black=(125,125,125)
white=(255,255,255)
tblack=(0,0,0)
delay=5
select=False
#chker coluer
cc1=(225,0,0)
cc2=(0,0,225)
pice=0
togle=True
action=0
x=0
y=0
px=31
py=31
grid=0

ec1x=31
ec1y=31

ec2x=31*5
ec2y=31

ec3x=31*9
ec3y=31

ec4x=31*13
ec4y=31

ec5x=31*3
ec5y=31*3

ec6x=31*7
ec6y=31*3

ec7x=31*11
ec7y=31*3

ec8x=31*15
ec8y=31*3

ec9x=31
ec9y=31*5

ec10x=31*5
ec10y=31*5

ec11x=31*9
ec11y=31*5

ec12x=31*13
ec12y=31*5

c1x=31
c1y=31*13

c2x=31*5
c2y=31*13

c3x=31*9
c3y=31*13

c4x=31*13
c4y=31*13

c5x=31*3
c5y=31*11

c6x=31*7
c6y=31*11

c7x=31*11
c7y=31*11

c8x=31*15
c8y=31*11

c9x=31*3
c9y=31*15

c10x=31*7
c10y=31*15

c11x=31*11
c11y=31*15

c12x=31*15
c12y=31*15


running=True

def checker(bord, tblack, x, y):
    pygame.draw.circle(bord,tblack,(x-31,y-31),(31))
    pygame.draw.circle(bord,tblack,(x-31,y-31),(30))

def regrid(bord, black, white, action, x, y, grid):
    while not grid>32+action:
        pygame.display.flip()
        pygame.draw.rect(bord,black,(x,y,62,62))
        x+=124
        pygame.draw.rect(bord,white,(x-62,y,62,62))
        if grid==4:
            y+=62
            x=62
            pygame.draw.rect(bord,white,(x-62,y,62,62))
        if grid==8:
            y+=62
            x=0
        if grid==12:
            y+=62
            x=62
            pygame.draw.rect(bord,white,(x-62,y,62,62))
        if grid ==16:
            y+=62
            x=0
        if grid==20:
            y+=62
            x=62
            pygame.draw.rect(bord,white,(x-62,y,62,62))
        if grid==24:
            y+=62
            x=0
        if grid==28:
            y+=62
            x=62
            pygame.draw.rect(bord,white,(x-62,y,62,62))
        if grid==32:
            pygame.draw.rect(bord,black,(x-62,y,62,62))
        grid+=1
regrid(bord, black, white, action, x, y, grid)
while running:
    
    if px>465:
        px=465
        if togle:
            togle=False
        else:
            togle=True
    if py>465:
        py=465
        if togle:
            togle=False
        else:
            togle=True
    if px<0:
        px=31
        if togle:
            togle=False
        else:
            togle=True
    if py<0:
        py=31
        if togle:
            togle=False
        else:
            togle=True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                select=True
            if event.key == pygame.K_UP:

                if togle:
                    pygame.draw.circle(bord,black,(px,py),(20))
                    togle=False
                else:
                    pygame.draw.circle(bord,white,(px,py),(20))
                    togle=True
                py-=62   
            if event.key == pygame.K_DOWN:
                if togle:
                    pygame.draw.circle(bord,black,(px,py),(20))
                    togle=False
                else:
                    pygame.draw.circle(bord,white,(px,py),(20))
                    togle=True
                py+=62
            if event.key == pygame.K_LEFT:
                
                if togle:
                    pygame.draw.circle(bord,black,(px,py),(20))
                    togle=False
                else:
                    pygame.draw.circle(bord,white,(px,py),(20))
                    togle=True
                px-=62
            if event.key == pygame.K_RIGHT:
                if togle:
                    pygame.draw.circle(bord,black,(px,py),(20))
                    togle=False
                else:
                    pygame.draw.circle(bord,white,(px,py),(20))
                    togle=True  
                px+=62              
        if event.type == pygame.QUIT: 
            running = False
   
    pygame.draw.circle(bord,(125,255,125),(px,py),(20))
    pygame.draw.circle(bord,tblack,(c1x,c1y),(15))
    pygame.draw.circle(bord,tblack,(c2x,c2y),(15))
    pygame.draw.circle(bord,tblack,(c3x,c3y),(15))
    pygame.draw.circle(bord,tblack,(c4x,c4y),(15))
    pygame.draw.circle(bord,tblack,(c5x,c5y),(15))
    pygame.draw.circle(bord,tblack,(c6x,c6y),(15))
    pygame.draw.circle(bord,tblack,(c7x,c7y),(15))
    pygame.draw.circle(bord,tblack,(c8x,c8y),(15))
    pygame.draw.circle(bord,tblack,(c9x,c9y),(15))
    pygame.draw.circle(bord,tblack,(c10x,c10y),(15))
    pygame.draw.circle(bord,tblack,(c11x,c11y),(15))
    pygame.draw.circle(bord,tblack,(c12x,c12y),(15))
    
    pygame.draw.circle(bord,tblack,(ec1x,ec1y),(15))
    pygame.draw.circle(bord,tblack,(ec2x,ec2y),(15))
    pygame.draw.circle(bord,tblack,(ec3x,ec3y),(15))
    pygame.draw.circle(bord,tblack,(ec4x,ec4y),(15))
    pygame.draw.circle(bord,tblack,(ec5x,ec5y),(15))
    pygame.draw.circle(bord,tblack,(ec6x,ec6y),(15))
    pygame.draw.circle(bord,tblack,(ec7x,ec7y),(15))
    pygame.draw.circle(bord,tblack,(ec8x,ec8y),(15))
    pygame.draw.circle(bord,tblack,(ec9x,ec9y),(15))
    pygame.draw.circle(bord,tblack,(ec10x,ec10y),(15))
    pygame.draw.circle(bord,tblack,(ec11x,ec11y),(15))
    pygame.draw.circle(bord,tblack,(ec12x,ec12y),(15))

    pygame.display.flip()