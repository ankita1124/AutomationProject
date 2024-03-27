#inherited base class calcualtor in childClass
from oopsconcepts import calculator

class childClass(calculator):
    num2=200

    def __init__(self):
        calculator. __init__(self,1,2)

    def getCompleteData(self):
        return self.num2+self.num+self.summation()


obj2=childClass()
print(obj2.getCompleteData())
