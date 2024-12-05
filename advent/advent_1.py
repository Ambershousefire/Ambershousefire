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
left_unsort=Left_list
Right_unsort=Right_list
Left_list=sorted(Left_list)
Right_list=sorted(Right_list)
d=0
x=0
while not x==len(file):
    d+=(abs((int(Left_list[x])-int(Right_list[x]))))
    x+=1
#print(d)
'''
#above this code works as intendid i dont know why the bottome isnt 
#it might be a problume with the way the numebrs are changed
'''
x=0
a=[]
#''' 
while not x ==10000:
    try:
        a.append(Right_unsort[x])
        Right_unsort[x]=Right_unsort[x]
        print(f"{a[x]}{Right_unsort[x]}")
        x+=1
    except:
        #print(x)
        x+=1
#'''
x=0
i=0
num=[]
while not x == 10000:
    try:
        if Right_unsort[x] in left_unsort:
            num.append(int(left_unsort.count(left_unsort[x]))*int(Right_unsort[x]))
        x+=1
    except:
        #print(x,"too many")
        x+=1
total=0
i=0
while not i == 410:
    try:
        total+=num[i]
        i+=1
    except:
        #print(i,"stop")
        i+=1
#print(total)