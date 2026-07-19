import random

n=random.randint(1,100)
Guesses=0
a=-1
while (a!=n):
    a=int(input("Guess the numbe : "))
    if(a>n):
        print("Smaller please")

    elif (a<n):
        print("Higher please")

    Guesses+=1

print(f"You have guess thee correct number in {Guesses} guesses")