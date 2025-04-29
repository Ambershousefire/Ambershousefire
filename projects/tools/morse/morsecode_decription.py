file = open("Ambershousefire\\projects\\tools\\morse\\temp_data.txt","w")
txt=input(":")
file.write(txt)
file = open("Ambershousefire\\projects\\tools\\morse\\temp_data.txt","r")
running=True
x=0
test_1=[]
print(len(file.read(-1)))
while running==True:
    x+=1
    if len(test_1)>len(file.read(-1)):
        running=False
    try:
        test_1.append(file.read(x))
    except:
        running=False
print(test_1)