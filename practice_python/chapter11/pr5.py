class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y , self.z + other.z)
    
    def __mul__(self, other):
        result= (self.x*other.x + self.y*other.y + self.z*other.z)
        return result
    
    def __str__(self):
        return f" Vector{self.x},{self.y},{self.z}"
    

V1=Vector(3,5,1)
V2=Vector(4,5,2)

print(V1+V2)
print(V1*V2)