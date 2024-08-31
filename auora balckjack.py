import random

runTime = True
i = 4
Difficulty = 0
difficulties = ["House", "Amateur", "Professional"]
suitNames = ["of Hearts", "of Diamonds", "of Clubs", "of Spades"]
cardNames = ["An Ace", "A Two", "A Three", "A Four", "A Five", "A Six", "A Seven", "An Eight", "A Nine", "A Ten", "A Jack", "A Queen", "A King"]

discardPile = []

PlayerHand = []
DealerHand = []
PlayerScore = 0
DealerScore = 0

#Card & Deck Setup
def cardSet(suit, reversed):
        list = []
        i = 1

        while i < 11:
                list.append(suit + str(i))
                i += 1

        list.append(suit + "J")
        list.append(suit + "Q")
        list.append(suit + "K")

        if reversed:
                list.reverse()

        return list

def AddCardSuit(SuitDeck, NewDeck):
        for card in SuitDeck:
                NewDeck.append(card)

        return NewDeck

def Shuffle(deck):
        shuffledDeck = []
        d = []
        d += deck
        while len(d) > 0:
                i = random.randint(0, len(d)-1)
                shuffledDeck.append(d[i])
                d.remove(d[i])

        return shuffledDeck

def ShuffleIn(Pile1, Pile2):
        list = Pile1 + Pile2
        return Shuffle(list)

def draw(hand, deck):
        hand.append(deck.pop(0))
        return hand

def showHand(hand, isPlayer):
        suitIDs   = ["H", "D", "C", "S",]
        cardIDs   = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suitNames = [" of Hearts", " of Diamonds", " of Clubs", " of Spades"]
        cardNames = ["An Ace", "A Two", "A Three", "A Four", "A Five", "A Six", "A Seven", "An Eight", "A Nine", "A Ten", "A Jack", "A Queen", "A King"]
        x = 0
        score = 0
        aces = 0

        if isPlayer:
                output = "Your hand has "
        else:
                output = "Dealer's Hand"
        handList = []

        for card in hand:
                i = 0
                cardString = ""

                while i < len(cardIDs):
                        if card.endswith(cardIDs[i]):
                                cardString += cardNames[i]
                                i += 1
                                if i > 1:
                                        if i >= 10:
                                                score += 10
                                        else:
                                                score += i
                                else:
                                        aces += 1
                                i = len(cardIDs)

                        i +=1
                i = 0
                while i < len(suitIDs):
                        if card.startswith(suitIDs[i]):
                                cardString += suitNames[i]
                                i = len(suitIDs)
                        i +=1
                handList.append(cardString)

        for card in handList:
                if len(handList)  - x > 2:
                        output += card + ", "
                elif len(handList) - x > 1:
                        output += card + " and "
                else:
                        output += card
                x += 1

        while aces != 0:
                aces -= 1
                if (score + 11 + aces) < 21:
                        score += 11
                else:
                        score += 1


        print(output)
        if isPlayer:
                print("Your Score is: ", score)
        else:
                print("The Dealer's Score is: ", score)
        return score


Hearts   = cardSet("H", False)
Diamonds = cardSet("D", True)
Clubs    = cardSet("C", False)
Spades   = cardSet("S", True)

NewDeck = []
NewDeck = AddCardSuit(Hearts, NewDeck)
NewDeck = AddCardSuit(Clubs, NewDeck)
NewDeck = AddCardSuit(Diamonds, NewDeck)
NewDeck = AddCardSuit(Spades, NewDeck)

#print("Blank Deck: ", NewDeck)

Deck = Shuffle(NewDeck)
#print("Shuffled Deck: ", Deck)
while i > 3:
        print("Please select a difficulty level, Home, Amateur or Casino")
        i = int(input("Enter 1-3 for difficulty or 4 for information: "))
        if i > 3:
                print("Difficulty in Blackjack is increased by adding and removing decks of cards, Home has 1 deck, Amateur has 2 decks, Casino has 4 decks")
Difficulty = i-1
print(difficulties[Difficulty], "Difficulty Selected")

if Difficulty == 1:
        Deck = ShuffleIn(Deck, NewDeck)
elif Difficulty == 2:
        Deck = ShuffleIn(Deck, NewDeck)
        Deck = ShuffleIn(Deck, NewDeck)
        Deck = ShuffleIn(Deck, NewDeck)

while runTime:
        if (input("Play Game?(y/n): ")).capitalize().startswith("Y"):
                inGame = True
                PlayerHand = draw(PlayerHand, Deck)
                PlayerHand = draw(PlayerHand, Deck)
                PlayerHand = draw(PlayerHand, Deck)
                PlayerHand = draw(PlayerHand, Deck)

                while inGame:
                        if len(Deck) == 0:
                                Deck = ShuffleIn(Deck, discardPile)

                        PlayerScore = showHand(PlayerHand, True)
                        DealerScore = showHand(DealerHand, False)

                        print("Dealer: Do you wish to Hit or Stand")
                        if (input()).capitalize().startswith("H"):
                                PlayerHand = draw(PlayerHand, Deck)
                        elif (input()).capitalize().startswith("S"):
                                break