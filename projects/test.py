
list=[]
i=0
done= True
while done:
    a=input("name: ")
    b=str(input("age: "))
    c=input("job: ")
    list.append(a)
    list.append(b)
    list.append(c)
    if (list[i] or list[i+1] or list[i+2]) == "end":
        done =False
        del list[i+2],list[i+1],list[i]
    i+=3
i=0
class test: 

    def __init__(self,name,type,job):
        self.name = name
        self.type = type
        self.job = job

    def __str__(self):
        return f"hello im {self.name} i'm {self.type} years old and i work as {self.job}."
    
while i<len(list):
    p=test(list[i],list[i+1],list[i+2])
    i+=3
    print(p,"\n")