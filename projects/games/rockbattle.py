
import random
file = open("data\\win_rate.txt","a")
win= "  You Won :3"
loss="  You lost >:3"
draw="  Thats a Draw"
runtime = True
w,l,d=0,0,0
run=input("do you whant to play rock paper sisors(yes or no): ")
if run.capitalize().startswith("Y"):
    run=True
elif not run.capitalize().startswith("Y"):

        print("aww i whanted to play")

if run==True:
    npc=[1,1,1,2,2,2,3,3,3] #rock is 1 paper is 2 paper 3 is sissiors
    b=0

    while runtime:
        print("wins",w,"losses",l,"draws",d)

        b=b+1

        x=int(input("ok to paly rock(1) paper(2) sisors(3) you will say what you whant to play and we will see who wins: "))    
        z=npc[random.randint(0,8)]

        if z==x:
            d+=1
            print(draw)

        elif z==(1):#R
            if x==2:#P
                w+=1
                print (win)

        elif x==3:#S
            l+=1
            print (loss)

        elif z==(2):#P
            if x==3:#S
                w+= 1
                print (win)

        elif x==1:#R
            l+= 1
            print(loss)

        elif z==(3):#S
            if x==1:#R
                w+=1
                print(win)

        elif x==2:#P
            l+=1
            print(loss)

        if w == 3:
            runtime = False
        elif l == 3:
            runtime = False
    print("wins",w,"losses",l,"draws",d)
    file.write("\nrock battle: ")
    file.write("wins: ")
    file.write(str(w))
    file.write(" losses: ")
    file.write(str(l))
    file.write(" draws: ")
    file.write(str(d))