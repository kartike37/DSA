with open("practice_python/chapter9/file.txt","r") as f:
    content=f.read()

contentNew=content.replace("Donkey","#####")

with open("practice_python/chapter9/file.txt","w") as f:
    f.write(contentNew)
    
