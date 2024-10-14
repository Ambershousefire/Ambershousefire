
import random as r
deler = []
player = []
running = True
p_value = 0
d_value = 0
i = 0
x = 0
count = 0
value={
    "2H" : 2,
    "2D" : 2,
    "2S" : 2,
    "2C" : 2,
    "3H" : 3,
    "3D" : 3,
    "3S" : 3,
    "3C" : 3,
    "4H" : 4,
    "4D" : 4,
    "4S" : 4,
    "4C" : 4,
    "5H" : 5,
    "5D" : 5,
    "5S" : 5,
    "5C" : 5,
    "6H" : 6,
    "6D" : 6,
    "6S" : 6,
    "6C" : 6,
    "7H" : 7,
    "7D" : 7,
    "7S" : 7,
    "7C" : 7,
    "8H" : 8,
    "8D" : 8,
    "8S" : 8,
    "8C" : 8,
    "9H" : 9,
    "9D" : 9,
    "9S" : 9,
    "9C" : 9,
    "10H" : 10,
    "10D" : 10,
    "10S" : 10,
    "10C" : 10,
    "JH" : 10,
    "JD" : 10,
    "JS" : 10,
    "JC" : 10,
    "QH" : 10,
    "QD" : 10,
    "QS" : 10,
    "QC" : 10,
    "KH" : 10,
    "KD" : 10,
    "KS" : 10,
    "KC" : 10,
    "AceH" : 1,
    "AceD" : 1,
    "AceS" : 1,
    "AceC" : 1,
}
sets = ["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"]
used = []
deck = []
while not i==2:
    for x in sets: 
        deck.append(x+"H")
        deck.append(x+"D")
        deck.append(x+"S")
        deck.append(x+"C")
    i+=1
i = 5
r.shuffle(deck)
player.append(deck[0])
player.append(deck[1])
deler.append(deck[3])
deler.append(deck[4])
d_value+=value[deler[0]]
p_value+=value[player[0]]
p_value+=value[player[1]]
print("your cards: "," ".join(player),"(",p_value,")")
print("deler: ",deler[0],"(",d_value,"+?",")")
while running:
    x = input("hit or stand: ")
    print("\n")
    if x.capitalize().startswith("H"): 
        player.append(deck[i])
        p_value=0
        d_value=0
        while not count==len(player):
            p_value+=value[player[count]]
            count+=1
        count=0
        print("player: "," ".join(player),"(",p_value,")")

        i+=1
        if p_value>21:
            running=False
            print("bust")
        elif p_value==21:
            running=False
            print("you win")
    else:
        while d_value<16:
            deler.append(deck[i])
            d_value = 0
            p_value = 0
            while not count==len(deler):
                d_value+=value[deler[count]]
                count+=1
            count = 0
            i+=1
            print("deler: "," ".join(deler),"(",d_value,")")

        if d_value>21:
            running=False
            if p_value<=21:
                print("you win")