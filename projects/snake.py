
import random as r
import pygame
l=1000
w=500
green=(25,255,25)
red=(255,25,25)
black=(0,0,0)
white=(255,255,255)
X=[]
Y=[]
x=l/2
y=w/2
xpos=0
ypos=0
xDir=0
yDir=0
delay=5
score=0
scorecount=0
running=True
pickupDist=15
speed=1
screen=pygame.display.set_mode((l,w))
while running:
    pygame.display.set_caption("snake for real this time")
    mousex, mousey = pygame.mouse.get_pos()
    pygame.time.delay(delay)
    if (x-xpos)<pickupDist and (x-xpos)>-pickupDist and (y-ypos)<pickupDist and (y-ypos)>-pickupDist:
        score= score+1 
    if score==scorecount:
        xpos=r.randint(10,(l-10))
        ypos=r.randint(10,(w-10))
        scorecount+=1
    if x>l:
        x=0
    if x<0:
        x=l
    if y>w:
        y=0
    if y<0:
        y=w
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                yDir = -1
                xDir = 0
            elif event.key == pygame.K_DOWN:
                yDir = 1
                xDir = 0
                
            elif event.key == pygame.K_LEFT:
                xDir = -1
                yDir = 0
                
            elif event.key == pygame.K_RIGHT:
                xDir = 1
                yDir = 0
                
            if event.key == pygame.K_SPACE:
                print(score)
    screen.fill(green)
    x = x +(speed*xDir)
    y = y + (speed*yDir)
    pygame.draw.circle(screen,red,(xpos,ypos),(5))
    
    pygame.draw.circle(screen,black,(x,y),10)

    X.append(x)
    Y.append(y)
    if score>=1:
        x1=X[-15]
        y1=Y[-15]
        pygame.draw.circle(screen,white,(x1,y1),10)
    if score>=2:
        x2=X[-5*2*3]
        y2=Y[-5*2*3]
        pygame.draw.circle(screen,black,(x2,y2),10)
    if score>=3:
        x3=X[-5*3*3]
        y3=Y[-5*3*3]
        pygame.draw.circle(screen,white,(x3,y3),10)
    if score>=4:
        x4=X[-5*4*3]
        y4=Y[-5*4*3]
        pygame.draw.circle(screen,black,(x4,y4),10)
    if score>=5:
        x5=X[-5*5*3]
        y5=Y[-5*5*3]
        pygame.draw.circle(screen,white,(x5,y5),10)
    if score>=6:
        x6=X[-5*6*3]
        y6=Y[-5*6*3]
        pygame.draw.circle(screen,black,(x6,y6),10)
    if score>=7:
        x7=X[-5*7*3]
        y7=Y[-5*7*3]
        pygame.draw.circle(screen,white,(x7,y7),10)
    if score>=8:
        x8=X[-5*8*3]
        y8=Y[-5*8*3]
        pygame.draw.circle(screen,black,(x8,y8),10)
    if score>=9:
        x9=X[-5*9*3]
        y9=Y[-5*9*3]
        pygame.draw.circle(screen,white,(x9,y9),10)
    if score>=10:
        x10=X[-15*10]
        y10=Y[-15*10]
        pygame.draw.circle(screen,black,(x10,y10),10)
    if score>=11:
        x11=X[-15*11]
        y11=Y[-15*11]
        pygame.draw.circle(screen,white,(x11,y11),10)
    if score>=12:
        x12=X[-15*12]
        y12=Y[-15*12]
        pygame.draw.circle(screen,black,(x12,y12),10)
    if score>=13:
        x13=X[-15*13]
        y13=Y[-15*13]
        pygame.draw.circle(screen,white,(x13,y13),10)
    if score>=14:
        x14=X[-15*14]
        y14=Y[-15*14]
        pygame.draw.circle(screen,black,(x14,y14),10)
    if score>=15:
        x15=X[-15*15]
        y15=Y[-15*15]
        pygame.draw.circle(screen,white,(x15,y15),10)
    if score>=16:
        x16=X[-15*16]
        y16=Y[-15*16]
        pygame.draw.circle(screen,black,(x16,y16),10)
    if score>=17:
        x17=X[-15*17]
        y17=Y[-15*17]
        pygame.draw.circle(screen,white,(x17,y17),10)
    if score>=18:
        x18=X[-15*18]
        y18=Y[-15*18]
        pygame.draw.circle(screen,black,(x18,y18),10)
    if score>=19:
        x19=X[-15*19]
        y19=Y[-15*19]
        pygame.draw.circle(screen,white,(x19,y19),10)
    if score>=20:
        x20=X[-15*20]
        y20=Y[-15*20]
        pygame.draw.circle(screen,black,(x20,y20),10)
    if score>=21:
        x21=X[-15*21]
        y21=Y[-15*21]
        pygame.draw.circle(screen,white,(x21,y21),10)
    if score>=22:
        x22=X[-15*22]
        y22=Y[-15*22]
        pygame.draw.circle(screen,black,(x22,y22),10)
    if score>=23:
        x23=X[-15*23]
        y23=Y[-15*23]
        pygame.draw.circle(screen,white,(x23,y23),10)
    if score>=24:
        x24=X[-15*24]
        y24=Y[-15*24]
        pygame.draw.circle(screen,black,(x24,y24),10)
    if score>=25:
        x25=X[-15*25]
        y25=Y[-15*25]
        pygame.draw.circle(screen,white,(x25,y25),10)
    if score>=26:
        x26=X[-15*26]
        y26=Y[-15*26]
        pygame.draw.circle(screen,black,(x26,y26),10)
    if score>=27:
        x27=X[-15*27]
        y27=Y[-15*27]
        pygame.draw.circle(screen,white,(x27,y27),10)
    if score>=28:
        x28=X[-15*28]
        y28=Y[-15*28]
        pygame.draw.circle(screen,black,(x28,y28),10)
    if score>=29:
        x29=X[-15*29]
        y29=Y[-15*29]
        pygame.draw.circle(screen,white,(x29,y29),10)
    if score>=30:
        x30=X[-15*30]
        y30=Y[-15*30]
        pygame.draw.circle(screen,black,(x30,y30),10)
    if score>=31:
        x31=X[-15*31]
        y31=Y[-15*31]
        pygame.draw.circle(screen,white,(x31,y31),10)
    if score>=32:
        x32=X[-15*32]
        y32=Y[-15*32]
        pygame.draw.circle(screen,black,(x32,y32),10)
    if score>=33:
        x33=X[-15*33]
        y33=Y[-15*33]
        pygame.draw.circle(screen,white,(x33,y33),10)
    if score>=34:
        x34=X[-15*34]
        y34=Y[-15*34]
        pygame.draw.circle(screen,black,(x34,y34),10)
    if score>=35:
        x35=X[-15*35]
        y35=Y[-15*35]
        pygame.draw.circle(screen,white,(x35,y35),10)
    if score>=36:
        x36=X[-15*36]
        y36=Y[-15*36]
        pygame.draw.circle(screen,black,(x36,y36),10)
    if score>=37:
        x37=X[-15*37]
        y37=Y[-15*37]
        pygame.draw.circle(screen,white,(x37,y37),10)
    if score>=38:
        x38=X[-15*38]
        y38=Y[-15*38]
        pygame.draw.circle(screen,black,(x38,y38),10)
    if score>=39:
        x39=X[-15*39]
        y39=Y[-15*39]
        pygame.draw.circle(screen,white,(x39,y39),10)
    if score>=40:
        x40=X[-15*40]
        y40=Y[-15*40]
        pygame.draw.circle(screen,black,(x40,y40),10)
    if score>=41:
        x41=X[-15*41]
        y41=Y[-15*41]
        pygame.draw.circle(screen,white,(x41,y41),10)
    if score>=42:
        x42=X[-15*42]
        y42=Y[-15*42]
        pygame.draw.circle(screen,black,(x42,y42),10)
    if score>=43:
        x43=X[-15*43]
        y43=Y[-15*43]
        pygame.draw.circle(screen,white,(x43,y43),10)
    if score>=44:
        x44=X[-15*44]
        y44=Y[-15*44]
        pygame.draw.circle(screen,black,(x44,y44),10)
    if score>=45:
        x45=X[-15*45]
        y45=Y[-15*45]
        pygame.draw.circle(screen,white,(x45,y45),10)
    if score>=46:
        x46=X[-15*46]
        y46=Y[-15*46]
        pygame.draw.circle(screen,black,(x46,y46),10)
    if score>=47:
        x47=X[-15*47]
        y47=Y[-15*47]
        pygame.draw.circle(screen,white,(x47,y47),10)
    if score>=48:
        x48=X[-15*48]
        y48=Y[-15*48]
        pygame.draw.circle(screen,black,(x48,y48),10)
    if score>=49:
        x49=X[-15*49]
        y49=Y[-15*49]
        pygame.draw.circle(screen,white,(x49,y49),10)
    if score>=50:
        x50=X[-15*50]
        y50=Y[-15*50]
        pygame.draw.circle(screen,black,(x50,y50),10)
    if score>=51:
        x51=X[-15*51]
        y51=Y[-15*51]
        pygame.draw.circle(screen,white,(x51,y51),10)
    if score>=52:
        x52=X[-15*52]
        y52=Y[-15*52]
        pygame.draw.circle(screen,black,(x52,y52),10)
    if score>=53:
        x53=X[-15*53]
        y53=Y[-15*53]
        pygame.draw.circle(screen,white,(x53,y53),10)
    if score>=54:
        x54=X[-15*54]
        y54=Y[-15*54]
        pygame.draw.circle(screen,black,(x54,y54),10)
    if score>=55:
        x55=X[-15*55]
        y55=Y[-15*55]
        pygame.draw.circle(screen,white,(x55,y55),10)
    if score>=56:
        x56=X[-15*56]
        y56=Y[-15*56]
        pygame.draw.circle(screen,black,(x56,y56),10)
    if score>=57:
        x57=X[-15*57]
        y57=Y[-15*57]
        pygame.draw.circle(screen,white,(x57,y57),10)
    if score>=58:
        x58=X[-15*58]
        y58=Y[-15*58]
        pygame.draw.circle(screen,black,(x58,y58),10)
    if score>=59:
        x59=X[-15*59]
        y59=Y[-15*59]
        pygame.draw.circle(screen,white,(x59,y59),10)
    if score>=60:
        x60=X[-15*60]
        y60=Y[-15*60]
        pygame.draw.circle(screen,black,(x60,y60),10)
    if score>=61:
        x61=X[-15*61]
        y61=Y[-15*61]
        pygame.draw.circle(screen,white,(x61,y61),10)
    if score>=62:
        x62=X[-15*62]
        y62=Y[-15*62]
        pygame.draw.circle(screen,black,(x62,y62),10)
    if score>=62:
        x63=X[-15*63]
        y63=Y[-15*63]
        pygame.draw.circle(screen,white,(x63,y63),10)
    if score>=64:
        x64=X[-15*64]
        y64=Y[-15*64]
        pygame.draw.circle(screen,black,(x64,y64),10)
    if score>=65:
        x65=X[-15*65]
        y65=Y[-15*65]
        pygame.draw.circle(screen,white,(x65,y65),10)
    if score>=66:
        x66=X[-15*66]
        y66=Y[-15*66]
        pygame.draw.circle(screen,black,(x66,y66),10)
    if score>=67:
        x67=X[-15*67]
        y67=Y[-15*67]
        pygame.draw.circle(screen,white,(x67,y67),10)
    if score>=68:
        x68=X[-15*68]
        y68=Y[-15*68]
        pygame.draw.circle(screen,black,(x68,y68),10)
    if score>=69:
        x69=X[-15*69]
        y69=Y[-15*69]
        pygame.draw.circle(screen,white,(x69,y69),10)
    if score>=70:
        x70=X[-15*70]
        y70=Y[-15*70]
        pygame.draw.circle(screen,black,(x70,y70),10)
    if score>=71:
        x71=X[-15*71]
        y71=Y[-15*71]
        pygame.draw.circle(screen,white,(x71,y71),10)
    if score>=72:
        x72=X[-15*72]
        y72=Y[-15*72]
        pygame.draw.circle(screen,black,(x72,y72),10)
    if score>=73:
        x73=X[-15*73]
        y73=Y[-15*73]
        pygame.draw.circle(screen,white,(x73,y73),10)
    if score>=74:
        x74=X[-15*74]
        y74=Y[-15*74]
        pygame.draw.circle(screen,black,(x74,y74),10)
    if score>=75:
        x75=X[-15*75]
        y75=Y[-15*75]
        pygame.draw.circle(screen,white,(x75,y75),10)
    if score>=76:
        x76=X[-15*76]
        y76=Y[-15*76]
        pygame.draw.circle(screen,black,(x76,y76),10)
    if score>=77:
        x77=X[-15*77]
        y77=Y[-15*77]
        pygame.draw.circle(screen,white,(x77,y77),10)
    if score>=78:
        x78=X[-15*78]
        y78=Y[-15*78]
        pygame.draw.circle(screen,black,(x78,y78),10)
    if score>=79:
        x79=X[-15*79]
        y79=Y[-15*79]
        pygame.draw.circle(screen,white,(x79,y79),10)
    if score>=80:
        x80=X[-15*80]
        y80=Y[-15*80]
        pygame.draw.circle(screen,black,(x80,y80),10)
    if score>=81:
        x81=X[-15*81]
        y81=Y[-15*81]
        pygame.draw.circle(screen,white,(x81,y81),10)
    if score>=82:
        x82=X[-15*82]
        y82=Y[-15*82]
        pygame.draw.circle(screen,black,(x82,y82),10)
    if score>=83:
        x83=X[-15*83]
        y83=Y[-15*83]
        pygame.draw.circle(screen,white,(x83,y83),10)
    if score>=84:
        x84=X[-15*84]
        y84=Y[-15*84]
        pygame.draw.circle(screen,black,(x84,y84),10)
    if score>=85:
        x85=X[-15*85]
        y85=Y[-15*85]
        pygame.draw.circle(screen,white,(x85,y85),10)
    if score>=86:
        x86=X[-15*86]
        y86=Y[-15*86]
        pygame.draw.circle(screen,black,(x86,y86),10)
    if score>=87:
        x87=X[-15*87]
        y87=Y[-15*87]
        pygame.draw.circle(screen,white,(x87,y87),10)
    if score>=88:
        x88=X[-15*88]
        y88=Y[-15*88]
        pygame.draw.circle(screen,black,(x88,y88),10)
    if score>=89:
        x89=X[-15*89]
        y89=Y[-15*89]
        pygame.draw.circle(screen,white,(x89,y89),10)
    if score>=90:
        x90=X[-15*90]
        y90=Y[-15*90]
        pygame.draw.circle(screen,black,(x90,y90),10)
    if score>=91:
        x91=X[-15*91]
        y91=Y[-15*91]
        pygame.draw.circle(screen,white,(x91,y91),10)
    if score>=92:
        x92=X[-15*92]
        y92=Y[-15*92]
        pygame.draw.circle(screen,black,(x92,y92),10)
    if score>=93:
        x93=X[-15*93]
        y93=Y[-15*93]
        pygame.draw.circle(screen,white,(x93,y93),10)
    if score>=94:
        x94=X[-15*94]
        y94=Y[-15*94]
        pygame.draw.circle(screen,black,(x94,y94),10)
    if score>=95:
        x95=X[-15*95]
        y95=Y[-15*95]
        pygame.draw.circle(screen,white,(x95,y95),10)
    if score>=96:
        x96=X[-15*96]
        y96=Y[-15*96]
        pygame.draw.circle(screen,black,(x96,y96),10)
    if score>=97:
        x97=X[-15*97]
        y97=Y[-15*97]
        pygame.draw.circle(screen,white,(x97,y97),10)
    if score>=98:
        x98=X[-15*98]
        y98=Y[-15*98]
        pygame.draw.circle(screen,black,(x98,y98),10)
    if score>=99:
        x99=X[-15*99]
        y99=Y[-15*99]
        pygame.draw.circle(screen,white,(x99,y99),10)
    
    if score==100:
        running=False
    pygame.display.flip()