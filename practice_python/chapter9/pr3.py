def generatetable(n):
    table=""

    for i in range(1,11):
        table+=f"{n} x {i} = {n*i}\n"

    with open (f"practice_python/chapter9/tables/table_{n}","w") as f:
        f.write(table)


for i in range(1,21):
    generatetable(i)


