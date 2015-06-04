class sample:
    def __init__(self):
        #define a private value,prefix '__' define a private value
        self.__val=0
        #define a public value,empty prefix means this is a public value
        self.gVal=0   
    def setVal(self,val):
        self.__val=val
    def printVal(self):
        print(self.__val)

example=sample()
example.printVal()
example.setVal(10)
#wrong:print example.__a=10
example.printVal()
print(example.gVal)
example.gVal=20;
print(example.gVal)
#wrong:print example.__a
