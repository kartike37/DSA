class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self, C2):
        return Complex(self.r+ C2.r , self.i + C2.i)
    
    def __mul__(self, C2):
        real_part= (self.r*C2.r - self.i*C2.i)
        image_part= (self.r * C2.i + self.i*C2.r)
        return Complex(real_part,image_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    

C1=Complex(2,6)
C2=Complex(4,9)
print(C1+C2)
print(C1*C2)