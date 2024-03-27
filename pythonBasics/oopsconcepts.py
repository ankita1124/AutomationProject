class calculator:
    num=100

    #default constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("This is a default constructor")

    def getData(self):
        print("Hello, I am function inside a class")

    def summation(self):
        return self.firstNumber+self.secondNumber+calculator.num
        # or self.num


obj=calculator(2,3)
obj.getData()
print(obj.num)
print(obj.summation())

obj1=calculator(4,3)
obj1.getData()
print(obj1.num)
print(obj1.summation())