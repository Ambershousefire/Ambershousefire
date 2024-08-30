import random
win="you won :3"
loss="haha i won"
draw="ha thats a draw"
i=0
j=0
run=input("do you whant to play rock paper sisors(yes or no): ")
if run.capitalize().startswith("Y"):
    run=True
elif not run.capitalize().startswith("Y"):
        print("aww i whanted to play")
if run==True:
    npc=[1,2,3] #rock is 1 paper is 2 sisors are 3
    while j<=2 or j<=2:
         random.shuffle(npc)
         x=int(input("ok to paly rock(1) paper(2) sisors(3) you will say what you whant to play and we will see who wins: "))    
         z=npc[0]
         if z==x:
            print(draw)

         if z==(1):#R
            if x==2:#P
                i = i +(1)
                print (win)
            elif x==3:#S
                    j = j +(1)
                    print (loss)

         elif z==(2):#P
            if x==3:#S
                i = i +(1)
                print (win)
            elif x==1:#R
                    j = +(1)
                    print(loss)

         elif z==(3):#S
            if x==1:#R
                i = i +(1)
                print(win)
            elif x==2:#P
                    j = j +(1)
                    print(loss)

if j<=2:
     print("ha i wont and you lost")
if i<=2:
     print("aww you one i whanted to win")
    