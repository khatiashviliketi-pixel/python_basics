from OopsDemo import calculator

class ChildImp(calculator):
    num2= 200

    def __init__(self):
        calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj = ChildImp()
print(obj.getCompleteData())