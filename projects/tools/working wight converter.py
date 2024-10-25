
run=input("this is a metric imperul converter, whtich do you wahnat to contert, distance or whight: ")

def wight(x, kg):
    if kg.upper().startswith("L"):
        output = str(x * 0.453592)+"kg"
    elif kg.upper().startswith("K"):
        output = str(x * 2.20462)+"lb"
    print(output)

def distance(x, kg):
    if kg.upper().startswith("F"):
        output = str(x * 0.3048)+"m"
    elif kg.upper().startswith("M"):
        output = str(x * 3.2808)+"ft"
    print(output)

if run.capitalize().startswith("D"):
    x=float(input("disance in numers:"))
    kg =input("meaters or feet: ")
    distance(x, kg)

elif not run.capitalize().startswith("D"):
    x =float(input("wight in numers:"))
    kg =input("Kg or Lb: ")
    wight(x, kg)