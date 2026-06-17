# problem 1

a=int(input("enter the first number:"))
b=int(input("enter the seceond number:"))
c=int(input("enter the third number:"))
d=int(input("enter the fourth number:"))

if(a>b and a>c and a>d):
    print("a is the greates number:",a)

elif (b>a and b>c and b>d):
    print("b is the greatest number:",b)

elif (c>a and c>b and c>d):
    print("c is the greatest number:",c)

elif (d>a and d>b and c<d):
    print("d is the greatest number:",d)