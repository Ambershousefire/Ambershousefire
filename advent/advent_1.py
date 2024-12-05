file=open("advent/advent_1.txt","r")
file=[file.readlines(-1)]
full_list_not_sperated=[]
x=0
file=[x for x in file[0]]
while not len(full_list_not_sperated)==len(file):
    full_list_not_sperated.append(list(str(file[x]).split("   ")))
    x+=1
Left_list=[]
Right_list=[]
x=0
while not len(Right_list)==len(file):
    Right_list.append(full_list_not_sperated[x][1])
    Left_list.append(full_list_not_sperated[x][0])
    x+=1
Left_list=sorted(Left_list)
Right_list=sorted(Right_list)
d=0
x=0
while not x==len(file):
    d+=(abs((int(Left_list[x])-int(Right_list[x]))))
    x+=1
x=0
a=[]
x=0
i=0
list=[]
total=0
x=0
z=0
while not z == 1000:
    try:
        if int(Left_list[x])-int(Right_list[z])==0:
            list.append(Left_list[x])
    except IndexError:
        x=0
        z+=1
    x+=1
i=0
while not i == -1:
    try:
        total+=int(list[i])
        i+=1
    except:
        break
print(f"{d},{total}")