import random 
print("This is black jack, lets have fun")
x=int(input("(1)Test(2)Normal(3)Hard"))

modes=["esay","Normal","hard"]
print(modes[x-1], "Selected!")
if x==3:
    x=x+1

deck=[]
ace=1
jack=queen=king=10
cards=[ace,2,3,4,5,6,7,8,9,10,jack,queen,king]
deck.append(cards[0:12])
hand=[]
random.shuffle(deck)
hand=(deck[-1])