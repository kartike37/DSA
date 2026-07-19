try:
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")