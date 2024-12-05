file = open("advent/advent_2.txt","r")
file=file.readlines(-1)
#print(file)
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
#len of lsit 1k
list_1.sort()
while not x == -1:
    try:
        list_1[x]=str(list_1[x]).split(" ")
    except:
        break
    x+=1
x=0
z=0
i=0
while not x == 1000:
    try:
        if (0<(int(list_1[x][z+0])-int(list_1[x][z+1])<4) and 0<(int(list_1[x][z+1])-int(list_1[x][z+2])<4) and 0<(int(list_1[x][z+2])-int(list_1[x][z+3])<4) and 0<(int(list_1[x][z+3])-int(list_1[x][z+4])<4)) and 0<(int(list_1[x][z+4])-int(list_1[x][z+5])<4 and  0<(int(list_1[x][z+5])-int(list_1[x][z+6])<4) and 0<(int(list_1[x][z+6])-int(list_1[x][z+7])<4) and 0<(int(list_1[x][z+7])-int(list_1[x][z+8])<4)):
            i+=1
    except:
        try:
            if (0<(int(list_1[x][z+0])-int(list_1[x][z+1])<4) and 0<(int(list_1[x][z+1])-int(list_1[x][z+2])<4) and 0<(int(list_1[x][z+2])-int(list_1[x][z+3])<4) and 0<(int(list_1[x][z+3])-int(list_1[x][z+4])<4)) and 0<int(list_1[x][z+4])-int(list_1[x][z+5])<4 and  0<(int(list_1[x][z+5])-int(list_1[x][z+6])<4) and 0<(int(list_1[x][z+6])-int(list_1[x][z+7])<4):
                i+=1
        except:
            try:
                if (0<(int(list_1[x][z+0])-int(list_1[x][z+1])<4) and 0<(int(list_1[x][z+1])-int(list_1[x][z+2])<4) and 0<(int(list_1[x][z+2])-int(list_1[x][z+3])<4) and 0<(int(list_1[x][z+3])-int(list_1[x][z+4])<4)) and 0<int(list_1[x][z+4])-int(list_1[x][z+5])<4 and  0<int(list_1[x][z+5])-int(list_1[x][z+6])<4:
                    i+=1
            except:
                try:
                    if (0<(int(list_1[x][z+0])-int(list_1[x][z+1])<4) and 0<(int(list_1[x][z+1])-int(list_1[x][z+2])<4) and 0<(int(list_1[x][z+2])-int(list_1[x][z+3])<4) and 0<(int(list_1[x][z+3])-int(list_1[x][z+4])<4)) and 0<int(list_1[x][z+4])-int(list_1[x][z+5])<4:
                        i+=1
                except:
                    try:
                        if (0<(int(list_1[x][z+0])-int(list_1[x][z+1])<4) and 0<(int(list_1[x][z+1])-int(list_1[x][z+2])<4) and 0<(int(list_1[x][z+2])-int(list_1[x][z+3])<4) and 0<(int(list_1[x][z+3])-int(list_1[x][z+4])<4)):
                            i+=1
                    except:
                        try:
                            if 0<(int(list_1[x][z+0])-int(list_1[x][z+1])<4) and 0<(int(list_1[x][z+1])-int(list_1[x][z+2])<4) and 0<(int(list_1[x][z+2])-int(list_1[x][z+3])<4):
                                i+=1
                        except:
                            try:
                                if (0<int(list_1[x][z+0])-int(list_1[x][z+1]))<4 and 0<(int(list_1[x][z+1])-int(list_1[x][z+2])<4):
                                    i+=1
                            except:
                                pass
    finally:
        x+=1
print(i)