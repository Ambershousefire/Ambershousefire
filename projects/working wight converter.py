run=input("this is a metric imperul converter, whtich do you wahnat to contert, distance or whight: ")
if run.capitalize().startswith("D"):
    y=float(input("disance in numers:"))
    kg =input("meaters or feet: ")
    if kg.upper().startswith("F"):
        print( y * 0.3048,"m")
    elif kg.upper().startswith("M"):
        print( y * 3.2808,"ft")
elif not run.capitalize().startswith("D"):
    x =float(input("wight in numers:"))
    kg =input("Kg or Lb: ")
    if kg.upper().startswith("L"):
        print( x * 0.453592,"kg")
    elif kg.upper().startswith("K"):
        print( x * 2.20462,"lb")