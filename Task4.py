class add:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def __str__(self):
        return "(+ "+str(self.number1)+" "+str(self.number2)+" )"
    def res(self):
        result=self.number1.res() + self.number2.res()
        return result    
class mul:
    def __init__(self,number3,number4):
        self.number3=number3
        self.number4=number4
    def __str__(self):
        result=self.number3.res() * self.number4.res()
        return result
    def res(self):
        result=self.number3.res() * self.number4.res()
        return result
class num:
    def __init__(self,number5):
        self.number5=number5
    def __str__(self):
        return str(self.number5)

    def res(self):
        return int(self.number5)


final=mul(num(10),add(num(10),num(20)))


print(final.res())


