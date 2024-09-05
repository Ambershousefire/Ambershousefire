
import pygame
import os
import links # type: ignore

pygame.init()


windowwidth = 1150
windowheight = 600
window = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("App Explorer")
font2 = pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Pm-Regular.ttf'), 25,)
reset = False
reset2 = True
delay = 5

global AppClick; AppClick = False
global MouseDown; MouseDown = False

speed = 50
#Colors
red = 249, 35, 35
green = 35, 249 , 86
blue = 45, 86, 153
purple = 8,0,42
white = 255, 255, 255
black = 0, 0, 0

#Border
P1 = 188,76,224
P2 = 141,51,207
P3 = 79,15,161
P4 = 40,7,95

#Painter1
x1 = 50
y1 = 50
stage1 = 0

#Painter2
x2 = windowwidth - 50
y2 = 50
stage2 = 3

#Painter3
x3 = windowwidth - 50
y3 = windowheight -50
stage3 = 2

#Painter4
x4 = 50
y4 = windowheight - 50
stage4 = 1
#Buttons
Button1 = True

#Apps
Link1 = links.Link1
Link2 = links.Link2
Link3 = links.Link3
Link4 = links.Link4
Link5 = links.Link5
Link6 = links.Link6
Link7 = links.Link7
Link8 = links.Link8
Link9 = links.Link9
Link10 =links.Link10

Title1 = links.Title1
Title2 = links.Title2
Title3 = links.Title3
Title4 = links.Title4
Title5 = links.Title5
Title6 = links.Title6
Title7 = links.Title7
Title8 = links.Title8
Title9 = links.Title9
Title10 = links.Title10

window.fill(purple)

def turtle(Colour, x, y, Stage, speed):
    if Stage == 0:
        x += speed
        pygame.draw.line(window, Colour, (x - 5, y), (x, y), 5)
        if x >= windowwidth - 50:
            Stage = 1

    if Stage == 1:
        y += speed
        pygame.draw.line(window, Colour, (x - 5, y), (x, y), 5)
        if y >= windowheight - 50:
            Stage = 2

    if Stage == 2:
        x -= speed
        pygame.draw.line(window, Colour, (x - 5, y), (x, y), 5)
        if x <= 50:
            Stage = 3    

    if Stage == 3:
        y -= speed
        pygame.draw.line(window, Colour, (x - 5, y), (x, y), 5)
        if y <= 50:
            Stage = 0   

    return  x, y, Stage

def Button(x, y, Link, AppClick, Name):
    inboundingbox = False
    pygame.draw.rect(window, P3, (x, y, 150, 150))
    pygame.draw.rect(window, P4, (x + 5, y + 5, 140, 140))
    
    if mousex >= x and mousey >= y and mousex <= (x + 150) and mousey <= (y + 150):
        inboundingbox = True

    if MouseDown and inboundingbox and AppClick == False:
            os.startfile(Link)
            AppClick = True
    render = font2.render(Name , True, white)        
    window.blit(render, (x + 10, y + 68), )
    return AppClick



run = True
while run:
    pygame.time.delay(delay)
    #mouse = pygame.mouse.get_pos()
    mousex, mousey = pygame.mouse.get_pos()


    #Quit Check + App Opening
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            MouseDown = False
    
    if MouseDown == False and AppClick == True:
        AppClick = False
        
#Border Aesthetic
    x1, y1, stage1 = turtle(P1, x1, y1, stage1, speed)
    x2, y2, stage2 = turtle(P3, x2, y2, stage2, speed)
    x3, y3, stage3 = turtle(P1, x3, y3, stage3, speed)
    x4, y4, stage4 = turtle(P3, x4, y4, stage4, speed)

    if stage1 == 2 and reset == False:
        window.fill(purple)
        reset = True
        speed = 5

    if reset2 == False:
        reset = False
        speed = 20
        x1 = 50
        y1 = 50
        stage1 = 0
        x2 = windowwidth - 50
        y2 = 50
        stage2 = 3
        x3 = windowwidth - 50
        y3 = windowheight -50
        stage3 = 2
        x4 = 50
        y4 = windowheight - 50
        stage4 = 1
        window.fill(purple)

#App Buttons    
    AppClick = Button(100, 115, Link1, AppClick, Title1)
    AppClick = Button(300, 115, Link2, AppClick, Title2)
    AppClick = Button(500, 115, Link3, AppClick, Title3)
    AppClick = Button(700, 115, Link4, AppClick, Title4)
    AppClick = Button(900, 115, Link5, AppClick, Title5)
    AppClick = Button(100, 335, Link6, AppClick, Title6)
    AppClick = Button(300, 335, Link7, AppClick, Title7)
    AppClick = Button(500, 335, Link8, AppClick, Title8)
    AppClick = Button(700, 335, Link9, AppClick, Title9)
    AppClick = Button(900, 335, Link10, AppClick,Title10)

    pygame.display.update()

pygame.quit()
