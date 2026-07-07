import random

def game():
    print("You are playing the the game")
    score=random.randint(1,70)
    # fetch the previous code

    with open("practice_python/chapter9/hiscore.txt") as f:
        hiscore=f.read()
        if (hiscore!=""):
            hiscore=int(hiscore)

        else:
            hiscore =0

    print(f"your score is {score}")

    # writindg new score in the file 

    if (hiscore<score):
        with open("practice_python/chapter9/hiscore.txt","w") as f:
            f.write(str(score))
    
    return score

game()
