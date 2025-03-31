
import pygame
file = open("Ambershousefire\\data\\win_rate.txt","a")
global AppClick; AppClick = False
global MouseDown; MouseDown = False
global screen
o="O wins"
Y="X wins"
winner=bool
k=False
b = [False,False,False,False,False,False,False,False,False,False,False]
c = [6,6,6,6,6,6,6,6,6,6,6]
screen = pygame.display.set_mode((300, 300))

pygame.display.set_caption('Tick, Tack, Toe')

screen.fill((255,255,255))

pygame.draw.line(screen,(0,0,0),(100,0),(100,300),(3))
pygame.draw.line(screen,(0,0,0),(200,0),(200,300),(3))
pygame.draw.line(screen,(0,0,0),(0,100),(300,100),(3))
pygame.draw.line(screen,(0,0,0),(0,200),(300,200),(3))

def line (list,startpos,value):
     if (list[startpos]==value) and (list[startpos+1]==value) and (list[startpos+2]==value):
        return True
     
def line_up(list,startpos,value):
     if (list[startpos]==value) and (list[startpos+3]==value) and (list[startpos+6]==value):
         return True
     
def negative(list,value):
     if (list[7]==value) and (list[5]==value) and (list[3]==value):
          return True
     
def postaive(list,value):
     if (list[1]==value) and (list[5]==value) and (list[9]==value):
          return True
     
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
                O(x,y)

            else:
                isO=True
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

    if b[1]==False:
        if MouseDown:
            if mousex<100 and mousey<100:
                AppClick,k = Button(0,0,AppClick,k)
                b[1]=True
                MouseDown=False
    if b[2]==False:
        if MouseDown:
            if mousex<200 and mousex>100 and mousey<100:
                AppClick,k = Button(100,0,AppClick,k)
                b[2]=True
                MouseDown=False
    if b[3]==False:
        if MouseDown:
            if mousex<300 and mousex>200 and mousey<100:
                AppClick,k = Button(200,0,AppClick,k)
                b[3]=True
                MouseDown=False
    if b[4]==False:
        if MouseDown:
            if mousex<100 and mousey<200 and mousey>100:
                AppClick,k = Button(0,100,AppClick,k)
                b[4]=True
                MouseDown=False
    if b[5]==False:
        if MouseDown:
            if mousex<200 and mousex>100 and mousey<200 and mousey>100:
                AppClick,k = Button(100,100,AppClick,k)
                b[5]=True
                MouseDown=False
    if b[6]==False:
        if MouseDown:
            if mousex<300 and mousex>200 and mousey<200 and mousey>100:
                AppClick,k = Button(200,100,AppClick,k)
                b[6]=True
                MouseDown=False
    if b[7]==False:
        if MouseDown:
            if mousex<100 and mousey<300 and mousey>200:
                AppClick,k = Button(0,200,AppClick,k)
                b[7]=True
                MouseDown=False
    if b[8]==False:
        if MouseDown:
            if mousex<200 and mousex>100 and mousey<300 and mousey>200:
                AppClick,k = Button(100,200,AppClick,k)
                b[8]=True
                MouseDown=False
    if b[9]==False:
        if MouseDown:
            if mousex<300 and mousex>200 and mousey<300 and mousey>200:
                AppClick,k = Button(200,200,AppClick,k)
                b[9]=True
                MouseDown=False
    if b[1]:
            if k:
                c[1]=False
            else:
                c[1]=True
            b[1]=6
    if b[2]:
            if k:
                c[2]=False
            else:
                c[2]=True
            b[2]=6
    if b[3]:
            if k:
                c[3]=False
            else:
                c[3]=True
            b[3]=6
    if b[4]:
            if k:
                c[4]=False
            else:
                c[4]=True
            b[4]=6
    if b[5]:
            if k:
                c[5]=False
            else:
                c[5]=True
            b[5]=6
    if b[6]:
            if k:
                c[6]=False
            else:
                c[6]=True
            b[6]=6
    if b[7]:
            if k:
                c[7]=False
            else:
                c[7]=True
            b[7]=6
    if b[8]:
            if k:
                c[8]=False
            else:
                c[8]=True
            b[8]=6
    if b[9]:
            if k:
                c[9]=False
            else:
                c[9]=True
            b[9]=6
    if line(c,1,True):
        running=False

    if line(c,4,True):
        running=False

    if line(c,7,True):
        running=False

    if line_up(c,1,True):
        running=False

    if line_up(c,2,True):
        running=False

    if line_up(c,3,True):
        running=False

    if negative(c,True):
        running=False

    if postaive(c,True):
        running=False
        #cheking if X#
    if line(c,1,False):
        running=False

    if line(c,4,False):
        running=False

    if line(c,7,False):
        running=False

    if line_up(c,1,False):
        running=False

    if line_up(c,2,False):
        running=False

    if line_up(c,3,False):
        running=False

    if negative(c,False):
        running=False

    if postaive(c,False):
        running=False

    pygame.display.flip()
file.write("\nXO: ")
if not winner:
    file.write(str(Y))
else:
    file.write(str(o))