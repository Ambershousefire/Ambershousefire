
x=1
z=1
y=40
running = True
list=[]
while not z==21:
    x+=z
    z+=1
    while running:
        list.append(x)
        x+=1
        if x>=41:
            running=False
            x=1
    if z<20:
        running=True


[print (x) for x in list]