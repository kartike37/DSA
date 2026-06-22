def comp():

    a=int(input("eneter the first no : "))
    b=int(input("eneter the first no : "))
    c=int(input("eneter the first no : "))

    if (a>b and a>c):
        print(f"The greatest no is :{a}")
    
    elif(b>a and b>c):
        print(f"The greatest no is : {b}")

    else:
        print(f"The gretest no is : {c}")

comp()