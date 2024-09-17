
x=int(input("Select of these: Addition(1) Subtraction(2) Multiplication(3) Division(4) Number Game(5) Square Numbers(6): "))
def sqr(x):
    x*=x 
    return x
if x>6:
    print("thats not something i can do")
else: 
    modes = ["Addition", "Subtraction", "Multiplication", "Division", "Number Game", "Square Numbers"]
    print(modes[x-1], "Selected!")

list=[1,2,3,4]
if list.count(x)==True:
    y=float(input("first number: "))
    z=float(input("second nuber: "))
    if x==(1):
        print(y+z)
    elif x==(2):
        print(y-z)
    elif x==(3):
        print(y * z)
    elif x==(4):
        print(y/z)
    b=input("is that corect? ")
    if b.capitalize().startswith("Y"):
        print("yay")
    elif not b.capitalize().startswith("Y"):
        print("aww")

    
if x==(5):
    q=1
    c=input("two nubers multipyed together is the gole, this will spit out a lsit of suqar numbers, do you whant to play: ")
    if c.capitalize().startswith("Y"):
        y=float(input("first number: "))
        z=float(input("second nuber: "))
        while ((y)*(z)) > sqr(q):
            print(q*q)
            q=q+1
        print ("your number:",z*y)
if x==(6):
    g=int(input("number: "))
    print(sqr(g))