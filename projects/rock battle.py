import random
win="   You Won :3"
loss="  You lost >:3"
draw="  Thats a Draw"
w=0
l=0
d=0
run=input("do you whant to play rock paper sisors(yes or no): ")
if run.capitalize().startswith("Y"):
    run=True
elif not run.capitalize().startswith("Y"):
        print("aww i whanted to play")
if run==True:
    npc=[1,2,3] #rock is 1 paper is 2 sisors are 3
    b=0
    while b<3:
         b=b+1
         random.shuffle(npc)
         x=int(input("ok to paly rock(1) paper(2) sisors(3) you will say what you whant to play and we will see who wins: "))    
         z=npc[0]
         if z==x:
            print(draw)
            d=+1
         if z==(1):#R
            if x==2:#P
                print (win)
                w=+1
            elif x==3:#S
                    print (loss)
                    l=+1  
         elif z==(2):#P
            if x==3:#S
                print (win)
                w=+1
            elif x==1:#R
                    print(loss)
                    l=+1
         elif z==(3):#S
            if x==1:#R
                print(win)
                w=+1
            elif x==2:#P
                    print(loss)
                    l=+1
print("wins",w,"losses",l,"draws",d)