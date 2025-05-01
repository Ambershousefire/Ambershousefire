txt=input("input your morse code here: ")
sep=[]
combind=[]
final=[]
sep=[x for x in txt]
running=True
x=0
z=""
while running:
    while not x == len(sep):
        if not sep[x] == " ":
            combind.append(sep[x])
            x+=1
        else:
            combind.append("//")
            x+=1
    x=0
    combind.append("//")
    while not x == len(combind):
        if not combind[x] == "//":
            z=z+(combind[x])
            x+=1
        else:
            x+=1
            final.append(z)
            z=""
    running=False
    output=[]
morse = [
    ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",  
    ".----","..---","...--","....-",".....","-....","--...","---..","----.","-----",
    "/","..--..","-.-.--","..-..",".-.-.-","-.-.-","---...","-..-.","-....-",".----.","..--.-",".-..-.",".-...",".--.-.","-.--.","-.--.","?"
]
lexacon = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "1","2","3","4","5","6","7","8","9","0",
    " ","?","!",",",".",";",":","/","-","'","@",'"',"&","@","(",")","*erro"
]
x=0
y=0
while len(output)< len(final):
    try:
        while not final[y]==morse[x]:
            x+=1
            if x>=len(morse):
                x = 0
                y+=1
        output.append(lexacon[x])
        y+=1
        x = 0
    except:
        output.append("?")
print("".join(output))