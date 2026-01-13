
import random,time
bord=[]
i=1
while not i==65:
    
    bord.append('-')
    i+=1
i=0
def game_state(bord,i):
    print(" ","~"*16)
    while not i==len(bord):
        print("|"," ".join(bord[i:i+8]),"|")
        i+=8
    print(" ","~"*16)

posx=[4]
posy=[4]

def pos_update(x,y):
    num=0
    while not num == len(x):
        bord[(8*y[num])+x[num]]="#"
        num+=1
    return bord




def apple(posx,posy): 
    test=True
    x=random.randrange(1,8)
    y=random.randrange(1,8)
    i=0
    running=True
    while running:
        while not i == len(posx):
            if x == posx and y == posy:
                test=False
                i+=1
            else:
                i+=1
        if test:
            running=False
        else: x,y=roll_pos(x,y)
    bord[(8*y)+x]="@"
    return x,y
running=True
apple(posx,posy)
z=""



while running:
    pos_update(posx,posy)
    game_state(bord,0)
    z=(input(":"))
    i=0
    if z.capitalize().startswith("U"):
        bord[((8*posy[i])+posx[i])]="-"
        posy[i]-=1
        

    elif z.capitalize().startswith("D"):
        bord[((8*posy[i])+posx[i])]="-"
        posy[0]=posy[0]+1

    elif z.capitalize().startswith("R"):
        bord[((8*posy[i])+posx[i])]="-"
        posx[0]+=1

    elif z.capitalize().startswith("L"):
        bord[((8*posy[i])+posx[i])]="-"
        posx[0]-=1


    
    if posy[0] < 0 or posy[0] > 8:
        running=False
        print("game over") 
    elif posx[0] < 0 or posx[0] == 8:
        running=False
        print("game over") 

        
    #if 

apple(posx,posy)