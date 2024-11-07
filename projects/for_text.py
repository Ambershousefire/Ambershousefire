
test=["1","2","3"]
test2=["a","b","c"]
suit = ["h", "s"]
deck =[x+y+z for x in test for y in suit for z in test2]

[print (x) for x in deck]