file = open("advent/advent_2.txt","r").readlines(-1)
file=[x for x in file]
x=0
i=0
z=0
but=[]
zet=[]
while not x==len(file):
    cut=file[x].split(" ")

    if (sorted(cut,reverse=False)==cut) or (sorted(cut,reverse=True)==cut):
        zet.append(cut)
    x+=1
x=0
z=0
y=0
i=0
f=1
get=0
while not z==len(zet):
    for x in zet[z]:
        but.append(int(x))
    while not f == len(but):
        
        
        if (int(but[f-1])-int(but[f])==1) or (int(but[f-1])-int(but[f])==2) or (int(but[f-1])-int(but[f])==3) :
            i+=1
            print("done")
        else:
            ("not")
        f+=1
        if i==(len(but)-1):
            y+=1
        print(i)
        print(but)
    print(len(but),"count")

    i=0
    z+=1
    f=0
    but=[]
    print("\n")
print(y)
print(len(zet))