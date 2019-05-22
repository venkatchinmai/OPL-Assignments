class add:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def __str__(self):
        return "(+ "+str(self.number1)+" "+str(self.number2)+" )"
class mul:
    def __init__(self,number3,number4):
        self.number3=number3
        self.number4=number4
    def __str__(self):
        return "(* "+str(self.number3)+" "+str(self.number4)+" )"
class num:
    def __init__(self,number5):
        self.number5=number5
    def __str__(self):
        return str(self.number5)

final=add(num(3),mul(num(6),add(num(7),num(8))))
print(final)

