txt=input(": ")
sep=[]
combind=[]
final=[]
sep=[x for x in txt]
running=True
x=0
i=0
y=0
z=""
while running:
    while not x == len(sep):
        if not sep[x] == " ":
            combind.append(sep[x])
            x+=1
        else:
            combind.append("//")
            x+=1
    combind.append("//")
    while not y == len(combind):
        if not combind[y] == "//":
            z=z+(combind[y])
            y+=1
        else:
            y+=1
            final.append(z)
            z=""
    print(sep,combind,final)
    running=False
    output=[]
morse = [
    ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",  #lower case letters
    ".----","..---","...--","....-",".....","-....","--...","---..","----.","-----",                                                                                  #numbers
    "/","..--..","-.-.--","..-..",".-.-.-","-.-.-","---...","-..-.","-....-",".----.","..--.-",".-..-.",".-...",".--.-.","-.--.","-.--.",                             #puntuation
    ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."   #upper case letters
]
lexacon = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",                                                          #lowercas etters
    "1","2","3","4","5","6","7","8","9","0",                                                                                                                          #numbers
    " ","?","!",",",".",";",":","/","-","'","@",'"',"&","@","(",")",                                                                                                  #puntuation
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"                                                           #upper case letters
]
x=0
y=0
while len(final)< len(output):
    try:
        while not final[y]==morse[x]:
            x+=1
            if x>=len(morse):
                y+=1
                x = 0
        output.append(lexacon[x])
        y+=1
        x = 0
    except:
        output.append("?")
print(" ".join(output))