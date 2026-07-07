Words=["Donkey","bad"]


with open("practice_python/chapter9/file.txt","r") as f:
    content=f.read()
for word in Words:
    content=content.replace(word,"#" * len(word))

with open("practice_python/chapter9/file.txt","w") as f:
    f.write(content)