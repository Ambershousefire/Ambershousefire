#blackjack
#21 is a black jack 
#2 decks of cards 
#random
#dealr can fold if they have more then 16
#face cards are 10 
#one of the dealrs cards arnt known
#betting
import random
j=0
y=0
f=0
ace=1
jack=10
queen=10
king=10
deck=[]
drd=[]
pld=[]

x=int(input("(1)essy, (2)normal, (3)hard: ")) 
modes = ["essy", "normal", "hard"]
print(modes[x-1], "Selected!")
if x==3:
   x=+1
def hit (i):
    i=deck.pop
    return i
def fill (i):
 while i<(x+x):
    deck=[ace,2,3,4,5,6,7,8,9,10,jack,queen,king]
    i=+1
def shuffle (i):
    i=len(deck)
    if i==0:
        fill
    random.shuffle(deck)
    fill 
    print(deck)
fill
random.shuffle(deck)
i=deck.pop
pld.append(i)
print(deck)
print(pld)
