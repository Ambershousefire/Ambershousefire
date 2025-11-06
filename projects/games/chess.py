
running = True
turn = 1
bordY = ["A","B","C","D","E","F","G","H"]

bordX = ["8","7","6","5","4","3","2","1"]
y=0
x=0
zetta = []
while not y == len(bordX): 
    while not x==8:
        zetta.append(bordY[x]+bordX[y])
        x+=1
    x=0
    y+=1
game = [
        " r","kn"," b"," k"," q"," b","kn"," r"
        ," p"," p"," p"," p"," p"," p"," p"," p"
        ," -"," -"," -"," -"," -"," -"," -"," -"
        ," -"," -"," -"," -"," -"," -"," -"," -"
        ," -"," -"," -"," -"," -"," -"," -"," -"
        ," -"," -"," -"," -"," -"," -"," -"," -"
        ,"Wp","Wp","Wp","Wp","Wp","Wp","Wp","Wp",
        "Wr","Wk","Wb","WQ","WK","Wb","Wk","Wr"
        ]
x=0
def gamestate(x):
        while not x >= 64:
                print("{"," | ".join(zetta[x:x+8]),"}")
        
                print("{"," | ".join(game[x:x+8]),"}")

                print("-"*41)

                x+=8
        return x
z = gamestate(0)
while running:
        text2 = input("place: ")
        text3 = input("To: ")
        y=0
        x=0
        while not zetta[y] == text2:
                y+=1
        while not zetta[x] == text3:
                x+=1
        game[x] = game[y]
        game[y] = " -"
        z = gamestate(0)

# pawns can only move one tile 
# on there first move they can move 2
# pawns can only attack on diagnels 
# pwans can promot to any class apon reaching the other side of the bord

# rooks can only move is stright lines

# bishops can only move on diagnles 

# knights attack in a L shape (2 fowerd 1 to the side)
# knights can hop over other pices 

# queen can use all move sets other then knight 

# king can only move one tile at a time
# king if in the line of attack must move or use another pice to --
# block the attack before they can move another pice 