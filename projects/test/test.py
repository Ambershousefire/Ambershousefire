b=1
a=1
running = True
while running:
    a+=1
    b+=1
    a=a*b
    b=a/2
    if b==a:
        break
print(a,b)
print(a/b)