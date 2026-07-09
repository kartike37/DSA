class Employee:
    salary=2000
    increment=20
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary* (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncement(self,salary):
        self.increment= ((salary/self.salary)-1)*100

e=Employee
e.salaryAfterIncement=280
print(e.increment9)
        