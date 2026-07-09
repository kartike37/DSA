from random import randint

class Train :
    def __init__(self,trainno):
        self.trainno=trainno

    def Book(self,fro,to):
       print(f"Ticket is booked in tain : {self.trainno} from {fro} to {to}")

    def getstatus(self):
        print(f"Train {self.trainno} is on time ")

    def getfair(self,fro,to):
        print(f"Train ticket for train {self.trainno} from {fro}  to {to} is {randint(222,5555)}") 

a=Train(1200)
a.Book("Delhi","Mumbai")
a.getstatus()
a.getfair("Delhi","Mumbai")