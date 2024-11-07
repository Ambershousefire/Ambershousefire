
test=["0","1","2","3","4","5","6","7","8","9"]
deck =[x+y+z for x in test for y in test for z in test]

#[print (x) for x in deck]
print(len(deck))
test2 = [i for i in range(10) if i%2 == 0]
print(test2)
test3=["3","7.4","8.2"]
test3=[float(x) for x in test3]
print(test3)