file = open("advent/avdent_2.txt","r").readlines(-1)
file=[x for x in file]
x=0
i=1
count=1
zet=0
cet=0
while not x==1000:
    cut=file[x].split(" ")
    while not (i-2)==len(cut):
        try:
            if (int(cut[i])-int(cut[i+1]))==( -1 or -2):
                zet+=1
            elif (int(cut[i])-int(cut[i+1]))==(1 or 2 or 3):
                zet-=1
        except:
            zet+=0
        i+=1
        if abs(zet)==len(cut):
            cet+=1
    x+=1
    i=0
    zet=0
print(cet)