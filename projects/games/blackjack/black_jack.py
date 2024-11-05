
import random as r, values
file = open("data\\money.txt","r")
playing = True
token = int(file.readline(-1))
file.close
file = open("data\\money.txt","w")
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

while playing:
    start=True
    dealer = []
    player = []
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

    print("How much do you want to bet, you current balance is:",token,"tokens")
    try:
        y=int(input(": "))
    except:
        start=False
        print("not a full number try again","\n")
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
        i = 4
        r.shuffle(deck)
        player.append(deck[0])
        player.append(deck[1])
        dealer.append(deck[2])
        dealer.append(deck[3])

        d_value = values.value[dealer[0]]
        p_value = counter(player, p_value)
        print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",dealer[0],"(",d_value,"+?",")")

        d_value = counter(dealer,d_value)
        p_value = counter(player, p_value)
        if d_value==21:
            running=False
            print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",", ".join(dealer),"(",d_value,")")
            print("you lose")
            token-=y

        if p_value==21:
            running=False
            print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",", ".join(dealer),"(",d_value,")")
            print("you win")
            token+=int((1.5*y))

        while running:
            x = input("hit or stand: ")
            print("\n")

            if x.capitalize().startswith("H"): 
                player.append(deck[i])
                p_value = counter(player,p_value)
                d_value = values.value[dealer[0]]
                print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",dealer[0],"(",d_value,"+?",")")

                i+=1
                if p_value>21:
                    running=False
                    d_value = counter(dealer,d_value)
                    p_value = counter(player,p_value)
                    print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",", ".join(dealer),"(",d_value,")")       
                    print("bust")
                    token-=y

                elif p_value==21:
                    running=False
                    p_value = counter(player,p_value)
                    d_value = counter(dealer,d_value)
                    print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",", ".join(dealer),"(",d_value,")")
                    print("you win")
                    token+=y

            elif x.capitalize().startswith("S"):
                d_value = counter(dealer,d_value)
                p_value = counter(player,p_value)
                print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",", ".join(dealer),"(",d_value,")","\n")

                if d_value==16:
                    running=False

                while d_value<16:
                    dealer.append(deck[i])
                    d_value = counter(dealer,d_value)
                    i+=1
                    print("dealer: ",", ".join(dealer),"(",d_value,")")
                    print("\n")

                if d_value<=21:
                    running=False
                    if p_value>d_value:
                        print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",", ".join(dealer),"(",d_value,")")
                        print("you win")
                        token+=y

                    elif d_value>p_value:
                        print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",", ".join(dealer),"(",d_value,")")
                        print("you lose")
                        token-=y

                    elif d_value == p_value:
                        print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",", ".join(dealer),"(",d_value,")")
                        print("draw")
                        token=token

                if d_value>21:
                    running=False
                    print("your cards: ",", ".join(player),"(",p_value,")","\n","dealer: ",", ".join(dealer),"(",d_value,")")
                    print("you win")
                    token+=y
        if input("do you whant to continu (y/n): ").capitalize().startswith("N"):
            playing=False
            file.write(str(token))