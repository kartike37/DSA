f=open("practice_python/chapter9/dumy.txt")
content=f.read()

if "twinkle" in content :
    print("The word present in the text")

else:
    print("the word is not present in the text")

f.close() 