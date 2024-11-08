#test=["0","1","2","3","4","5","6","7","8","9"]
#deck =[x+y+z for x in test for y in test for z in test]

#[print (x) for x in deck]
#print(len(deck))
#test2 = [i for i in range(10) if i%2 == 0]
#print(test2)
#test3=["3","7.4","8.2"]
#test3=[float(x) for x in test3]
#print(test3)


dice=20
num=2
x=True
y=0
z=0

list=[i for i in range(dice+1) if i>0]
list2=[]
while x:
    list2.append(list[y]+list[z])
    y+=1
    if y==len(list):
        z+=1
        y=0
    if z==len(list):
        z=0
        y=0
        x=False
list4=[i for i in range(41) if i>1]
list2.sort()
list3=[]
i=num-1
while i<dice*num:
    i+=1
    list3.append(list2.count(i))

print(list)
print("\n\n")
print(list2)
print("\n\n")
print(list3)
print("\n\n")
print(list4)
print("\n\n")
[print (list3[i],list4[i]) for i in range(39)]