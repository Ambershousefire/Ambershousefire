file=open("advent/advent_1.txt","r")
file=[file.readlines(-1)]
a=[]
x=0
file=[x for x in file[0]]
while not len(a)==len(file):
    a.append(list(str(file[x]).split("   ")))
    x+=1
b=[]
c=[]
x=0
while not len(c)==len(file):
    c.append(a[x][1])
    b.append(a[x][0])
    x+=1
b=sorted(b)
c=sorted(c)
d=0
x=0
while not x==len(file):
    d+=(abs((int(b[x])-int(c[x]))))
    x+=1
print(d)