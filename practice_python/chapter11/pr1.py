class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def show(self):
        print(f"The vector is ThreeDVector {self.i}i {self.j}j ")    

class ThreeDVector (TwoDVector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
    def show(self):
        print(f"The vector is ThreeDVector {self.i}i {self.j}j {self.k}k")    


a=TwoDVector(1,2)
a.show()
d=ThreeDVector(3,5,9)
d.show()