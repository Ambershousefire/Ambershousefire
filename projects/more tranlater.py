string = input("what to translate: ")
letter = [x for x in string]
i,x,y = 0,0,0
trans=[]
morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----"," ","..--..","-.-.--"]
lexacon=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," ","?","!"]
while i< len(letter):
    while not letter[y]==lexacon[x]:
        x+=1
        if x>=len(lexacon):
            x=0
    letter[y]==lexacon[x]
    trans.append(morse[x])
    i+=1
    y+=1
print(trans)