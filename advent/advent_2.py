file = open("advent/advent_2.txt","r")
file=file.readlines(-1)
x=0
z=0
list_1=[]
while not x ==-1: 
    try:
        list_1.append((file[x][0:-1]))
    except:
        break
    x+=1
x=0
while not x == -1:
    try:
        list_1[x]=str(list_1[x]).split(" ")
    except:
        break
    x+=1
x=0

i=0

print(i)