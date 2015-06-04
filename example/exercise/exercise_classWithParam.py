class simpleClass:
    def __init__(self,val):
        #define a private value,prefix '__' define a private value
        self.__val=val
    def setVal(self,val):
        self.__val=val
    def printVal(self):
        print(self.__val)

example=simpleClass(30)
example.printVal()
example.setVal(20)
example.printVal()
