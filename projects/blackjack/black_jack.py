
import random as r, values
token=1000
def hands():
    print("your cards: ",", ".join(player),"(",p_value,")","\n","deler: ",", ".join(deler),"(",d_value,")")
def safe_hands():
    ("your cards: ",", ".join(player),"(",p_value,")","\n","deler: ",deler[0],"(",d_value,"+?",")")
def counter(obj,Value):
    count=0
    Value=0
    while not count==len(obj):
        Value+=values.value[obj[count]]
        if obj[count]==("Ace of Hearts" or "Ace of Diamonds" or "Ace of Spades" or "Ace of Clubs"):
            if Value>21:
                Value-=10
        count+=1
    count = 0
    return Value

while token>0:
    start=True
    deler = []
    player = []
    count=0
    running = True
    p_value = 0
    d_value = 0
    i = 0
    x = 0
    cards = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    deck = []

    while not i==2:
        for x in cards: 
            deck.append(x+" of Hearts")
            deck.append(x+" of Diamonds")
            deck.append(x+" of Spades")
            deck.append(x+" of Clubs")
        i+=1
        
    print("how much do you whant to bet, you cutnet blance is:",token,"tokens")
    y=(input(": "))
    try:
        y=int(y)
    except:
        start=False
        print("not a number try again","\n")
    else:
        if y<=0:
            print("try again")
            start=False
        elif y>token:
            print("try again")
            start=False
        else:
            start=True
    if start==True:

        i = 5
        r.shuffle(deck)
        player.append(deck[0])
        player.append(deck[1])
        deler.append(deck[3])
        deler.append(deck[4])

        d_value = values.value[deler[0]]
        p_value = counter(player, p_value)
        safe_hands

        d_value = counter(deler,d_value)
        p_value = counter(player, p_value)

        if p_value>21:
            running=False
            hands
            print("you lose")
            token-=y

        if d_value==21:
            running=False
            hands
            print("you lose")
            token-=y

        if p_value==21:
            running=False
            hands
            print("you win")
            token+=y

        while running:
            x = input("hit or stand: ")
            print("\n")

            if x.capitalize().startswith("H"): 
                player.append(deck[i])
                d_value=0
                p_value = counter(player,p_value)
                d_value+=values.value[deler[0]]
                safe_hands

                i+=1
                if p_value>21:
                    d_value = counter(deler,d_value)
                    p_value = counter(player,p_value)
                    hands       
                    running=False
                    print("bust")
                    token-=y

                elif p_value==21:
                    running=False
                    p_value = counter(player,p_value)
                    d_value = counter(deler,d_value)
                    hands
                    print("you win")
                    token+=y

            elif x.capitalize().startswith("S"):
                d_value = counter(deler,d_value)
                p_value = counter(player,p_value)
                
                if d_value==16:
                    hands
                    running=False

                while d_value<16:
                    deler.append(deck[i])
                    d_value = counter(deler,d_value)
                    i+=1
                    hands
                    print("\n")
                
                if d_value<=21:
                    running=False
                    if p_value>d_value:
                        hands
                        print("you win")
                        token+=y
                        running=False

                    elif d_value>p_value:
                        hands
                        print("you lose")
                        token-=y
                        running=False

                    elif d_value == p_value:
                        hands
                        print("draw")
                        token=token
                        running=False

                if d_value>21:
                    hands
                    print("you win")
                    token+=y
                    running=False
print("you ran out of funds")