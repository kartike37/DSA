   # problem2 

marks1=int(input("marks for 1 subject"))
marks2=int(input("marks for 2 subject"))
marks3=int(input("marks for 3 subject"))

Total_percentage=((marks1+marks2+marks3)/300)*100

if(Total_percentage>40):
    print("the student is pass")

else:
    print("the student is fail")