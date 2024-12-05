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

while not x == -1:
    try:
        list_1[x]=str(list_1[x]).split(" ")
    except:
        break
    x+=1
x=0
i=0
while not x == 1000:
    try:
        if (0<(int(list_1[x][0])-int(list_1[x][1])<4) and 0<(int(list_1[x][1])-int(list_1[x][2])<4) and 0<(int(list_1[x][2])-int(list_1[x][3])<4) and 0<(int(list_1[x][3])-int(list_1[x][4])<4)) and 0<(int(list_1[x][4])-int(list_1[x][5])<4 and  0<(int(list_1[x][5])-int(list_1[x][6])<4) and 0<(int(list_1[x][6])-int(list_1[x][7])<4) and 0<(int(list_1[x][7])-int(list_1[x][8])<4)):
            i+=1
    except:
        try:
            if (0<(int(list_1[x][0])-int(list_1[x][1])<4) and 0<(int(list_1[x][1])-int(list_1[x][2])<4) and 0<(int(list_1[x][2])-int(list_1[x][3])<4) and 0<(int(list_1[x][3])-int(list_1[x][4])<4)) and 0<int(list_1[x][4])-int(list_1[x][5])<4 and  0<(int(list_1[x][5])-int(list_1[x][6])<4) and 0<(int(list_1[x][6])-int(list_1[x][7])<4):
                i+=1
        except:
            try:
                if (0<(int(list_1[x][0])-int(list_1[x][1])<4) and 0<(int(list_1[x][1])-int(list_1[x][2])<4) and 0<(int(list_1[x][2])-int(list_1[x][3])<4) and 0<(int(list_1[x][3])-int(list_1[x][4])<4)) and 0<int(list_1[x][4])-int(list_1[x][5])<4 and  0<int(list_1[x][5])-int(list_1[x][6])<4:
                    i+=1
            except:
                try:
                    if (0<(int(list_1[x][0])-int(list_1[x][1])<4) and 0<(int(list_1[x][1])-int(list_1[x][2])<4) and 0<(int(list_1[x][2])-int(list_1[x][3])<4) and 0<(int(list_1[x][3])-int(list_1[x][4])<4)) and 0<int(list_1[x][4])-int(list_1[x][5])<4:
                        i+=1
                except:
                    try:
                        if (0<(int(list_1[x][0])-int(list_1[x][1])<4) and 0<(int(list_1[x][1])-int(list_1[x][2])<4) and 0<(int(list_1[x][2])-int(list_1[x][3])<4) and 0<(int(list_1[x][3])-int(list_1[x][4])<4)):
                            i+=1
                    except:
                        pass
    finally:
        x+=1
x=0
while not x == 1000:
    try:
        if (-4<(int(list_1[x][0])-int(list_1[x][1])<0) and -4<(int(list_1[x][1])-int(list_1[x][2])<0) and -4<(int(list_1[x][2])-int(list_1[x][3])<0) and -4<(int(list_1[x][3])-int(list_1[x][4])<0)) and -4<(int(list_1[x][4])-int(list_1[x][5])<0 and  -4<(int(list_1[x][5])-int(list_1[x][6])<0) and -4<(int(list_1[x][6])-int(list_1[x][7])<0) and -4<(int(list_1[x][7])-int(list_1[x][8])<0)):
            i+=1
    except:
        try:
            if (-4<(int(list_1[x][0])-int(list_1[x][1])<0) and -4<(int(list_1[x][1])-int(list_1[x][2])<0) and -4<(int(list_1[x][2])-int(list_1[x][3])<0) and -4<(int(list_1[x][3])-int(list_1[x][4])<0)) and -4<int(list_1[x][4])-int(list_1[x][5])<0 and  -4<(int(list_1[x][5])-int(list_1[x][6])<0) and -4<(int(list_1[x][6])-int(list_1[x][7])<0):
                i+=1
        except:
            try:
                if (-4<(int(list_1[x][0])-int(list_1[x][1])<0) and -4<(int(list_1[x][1])-int(list_1[x][2])<0) and -4<(int(list_1[x][2])-int(list_1[x][3])<0) and -4<(int(list_1[x][3])-int(list_1[x][4])<0)) and -4<int(list_1[x][4])-int(list_1[x][5])<0 and  -4<int(list_1[x][5])-int(list_1[x][6])<0:
                    i+=1
            except:
                try:
                    if (-4<(int(list_1[x][0])-int(list_1[x][1])<0) and -4<(int(list_1[x][1])-int(list_1[x][2])<0) and -4<(int(list_1[x][2])-int(list_1[x][3])<0) and -4<(int(list_1[x][3])-int(list_1[x][4])<0)) and -4<int(list_1[x][4])-int(list_1[x][5])<0:
                        i+=1
                except:
                    try:
                        if (-4<(int(list_1[x][0])-int(list_1[x][1])<0) and -4<(int(list_1[x][1])-int(list_1[x][2])<0) and -4<(int(list_1[x][2])-int(list_1[x][3])<0) and -4<(int(list_1[x][3])-int(list_1[x][4])<0)):
                            i+=1
                    except:
                        pass
    finally:
        x+=1
print(i)