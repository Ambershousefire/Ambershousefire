
loc = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
}
type = { 
    "R":0,
    "KN":1,
    "B":2,
    "KI":3,
    "Q":4,
    "P":5
}

rookx = [1,8,1,8]
rooky = [1,1,8,8]
bishiopx = [2,7,2,7]
bishiopy = [1,1,8,8]
knightx = [3,6,3,6]
knighty = [1,1,8,8]
pawnx = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
pawny = [2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,7]
kingx = [5,5]
kingy = [1,8]
queenx = [4,4]
queeny = [1,8]

rook = [rookx,rooky]
knight = [knightx,knighty]
bishiop = [bishiopx,bishiopy]
pawn = [pawnx,pawny]
king = [kingx,kingy]
queen = [queenx,queeny]

role = [rook,knight,bishiop,king,queen,pawn]
text = input(": ")
text2 = int(input(": "))
text3 = int(input(": "))

text = str(text).capitalize()



x = type[text]
y = text2-1
z = text3-1

print(x,y,z)

