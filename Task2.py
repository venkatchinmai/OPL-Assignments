class Add:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def res(self):
        print("(+" +str(self.num1)+" " +self.res(self.num2)+")")
       

class Mul:
    def __init__(self,num3,num4):
        self.num3=num3
        self.num4=num4
    def multiply(self):
        print("(*" +str(self.num3) +" "+str(self.num4)+")")
        
class Num:
    def __init__(self,num5):
        self.num5=num5
    def number(self):
        print(str(self.num5))



a = Add(2,Add(3,4))
a.res()
m = Mul(5,6)
#m.multiply()







# a1=input("Enter number")
# a2=input("Enter number")
# sign=input("enter sign")
# if(sign=="+"):
#     a1=Add(a1,a2)
#     a1.sum()
# else:
#     m1=Mul(a1,a2)
#     m1.multiply()

# n1=Num(50)
# n1.number()







