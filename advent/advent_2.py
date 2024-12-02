file = open("advent/avdent_2.txt","r").readlines(-1)
file=[x for x in file]
x=0
i=0
z=0
but=[]
zet=[]
while not x==len(file):
    cut=file[x].split(" ")

    if (sorted(cut)==cut) or (sorted(cut,reverse=True)==cut):
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
        if but[f-1]-but[f]==(1 or 2):
            i+=1
        if but[f-1]-but[f]==(-1 or -2 or -3):
            i+=-1
        f+=1
        if i==(len(but)-1):
            y+=1
        if i==-(len(but)-1):
            y+=1
        i=0
    z+=1
    f=0
    but=[]
print(y)