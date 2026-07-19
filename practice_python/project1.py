import random
#Snake water gun game 
yourstr=input("Enter your choice ")

yourdic={"snake":1, 
         "water":-1,
         "gun":0}

reversedict={1:"snake",
             -1:"water",
             0:"gun"}

you = yourdic[yourstr]
computer=random.choice([1,-1,0])

print(f"You chose {reversedict[you]}  computer chose {reversedict[computer]}")

if (computer == you):
    print("It is a draw")

else:
    if (computer==-1 and you==1):
        print("you win")
    
    elif (computer==-1 and you==0):
        print("you lose")
    
    elif(computer==1 and you==-1):
        print("you lose")
    
    elif(computer==1 and you==0):
        print("you win ")

    elif(computer==0 and you==-1):
        print("you win ")

    elif(computer==0 and you==1):
        print("you lose")

    else:
        print("something wwent wrong")