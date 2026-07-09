class programmer:
    Company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name= name
        self.salary= salary
        self.pin= pin

p=programmer("Kartike",120000,"pin")
print(p.name,p.salary,p.pin,p.Company)

r=programmer("Saina",120000,"pin")
print(r.name,r.salary,r.pin,r.Company)