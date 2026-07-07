with open("practice_python/chapter9/file.txt","r")  as f:
    lines = f.readlines()
lineno=1
for line in lines:
    if("python" in line):
        print(f"yes the word python is present in the text, In line no {lineno}")
        break
    lineno += 1

else:
    print("the linne is not present in the text") 
