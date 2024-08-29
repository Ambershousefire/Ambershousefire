import random
win="you won :3"
loss="haha i won"
draw="ha thats a draw"
run=input("do you whant to play rock paper sisors(yes or no): ")
if run.capitalize().startswith("Y"):
    run=True
elif not run.capitalize().startswith("Y"):
        print("aww i whanted to play")
if run==True:
    npc=[1,2,3] #rock is 1 paper is 2 sisors are 3
    xy=0
    while xy<3:
         xy+=1
         random.shuffle(npc)
         x=int(input("ok to paly rock(1) paper(2) sisors(3) you will say what you whant to play and we will see who wins: "))    
         z=npc[0]
         if z==x:
            print(draw)
         if z==(1):#R
            if x==2:#P
                print (win)
            elif x==3:#S
                    print (loss)
         elif z==(2):#P
            if x==3:#S
                print (win)
            elif x==1:#R
                    print(loss)
         elif z==(3):#S
            if x==1:#R
                print(win)
            elif x==2:#P
                    print(loss)