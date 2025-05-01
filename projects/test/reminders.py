x=[1,2,3]
dict = {
    "a":"b",
    "b": 4,
    4 : x,

}
print(dict["a"],dict["b"],dict[4])

for b in x:
    if not b == 2:
        x.append(2)
print(x)
print("\n".join(str(x))) 
x=[ x for x in x]
print(x)
