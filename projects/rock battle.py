import random
win="you won :3"
loss="haha i won"
draw="ha thats a draw"
i=0
j=0
def winner(i):
    if i<=2:
         print("aww you one i whanted to win")
def losser(j):
    if j<=2:
         print("ha i wont and you lost")
run=input("do you whant to play rock paper sisors(yes or no): ")
if run.capitalize().startswith("Y"):
    run=True
elif not run.capitalize().startswith("Y"):
        print("aww i whanted to play")
if run==True:
    npc=[1,2,3] #rock is 1 paper is 2 sisors are 3
    while (i < (2)) or (j < (2)):
         random.shuffle(npc)
         x=int(input("ok to paly rock(1) paper(2) sisors(3) you will say what you whant to play and we will see who wins: "))    
         z=npc[0]
         if z==x:
            print(draw)
         if z==(1):#R
            if x==2:#P
                print (win)
                i= i+1
            elif x==3:#S
                    print (loss)
                    j= j+1
         elif z==(2):#P
            if x==3:#S
                print (win)
                i= i+1
            elif x==1:#R
                    j= j+1
                    print(loss)
         elif z==(3):#S
            if x==1:#R
                print(win)
                i= i+1
            elif x==2:#P
                    print(loss)
                    j= j+1
         print("win to lose",i,j)


losser(j)
winner(i)