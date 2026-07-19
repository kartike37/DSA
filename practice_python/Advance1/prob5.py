n=int(input("Enter the number: "))

table=[n*i for i in range(1,11)]
print(table)
with open ("practice_python/Advance1/1.txt","a") as f:
    f.write(f"Table of {n} {str(table)} \n")