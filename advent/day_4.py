file=open("advent/day_4.txt","r")
file=[file.readlines(-1)]
full_list=[]
x=0
file=[x for x in file[0]]
while not len(full_list)==len(file):
    full_list.append(list(str(file[x]).split("   ")))
    x+=1
x=0
i=0
xmas=0
ewxmas=0
nsxmas=0
neswxmas=0
nwsexmas=0
while not x == 1440:
    try:
        if (full_list[x][0][i]+full_list[x][0][i+1]+full_list[x][0][i+2]+full_list[x][0][i+3])==("XMAS"or"SAMX"):
            ewxmas+=1
            print("test")
    except:
        pass
    try:
        if (full_list[x][0][i]+full_list[x+1][0][i+1]+full_list[x+2][0][i+2]+full_list[x+3][0][i+3])==("XMAS"or"SAMX"):
            neswxmas+=1
            #print("test")
    except:
        pass
    try: 
        if (full_list[x][0][i]+full_list[x+1][0][i]+full_list[x+2][0][i]+full_list[x+3][0][i])==("XMAS"or"SAMX"):
            nsxmas+=1
            #print("test")
    except:
        pass
    try:
        if (full_list[x][0][i]+full_list[x-1][0][i+1]+full_list[x-2][0][i+2]+full_list[x-3][0][i+3])==("XMAS"or"SAMX"):
            nwsexmas+=1
            #print("test")
    except:
        pass
    if i==140:
        i=0
        x+=1
    i+=1
i=0
x=0


print(ewxmas,nsxmas,neswxmas,nwsexmas)
xmas=ewxmas+nsxmas+neswxmas+nwsexmas
print(xmas)