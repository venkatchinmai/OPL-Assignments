class add:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def __str__(self):
        return "(+ "+str(self.number1)+" "+str(self.number2)+" )"
    def res(self):
        result=self.number1.res() + self.number2.res()
        return result    

class sub:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def __str__(self):
        return "(+ "+str(self.number1)+" "+str(self.number2)+" )"
    def res(self):
        result=self.number1.res() - self.number2.res()
        return result    
class mul:
    def __init__(self,number3,number4):
        self.number3=number3
        self.number4=number4
    def __str__(self):
        return "(* "+str(self.number3)+" "+str(self.number4)+" )"
    def res(self):
        result=self.number3.res() * self.number4.res()
        return result

class div:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def __str__(self):
        return "(+ "+str(self.number1)+" "+str(self.number2)+" )"
    def res(self):
        result=self.number1.res() / self.number2.res()
        return result    

class equal:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def __str__(self):
        return "(+ "+str(self.number1)+" "+str(self.number2)+" )"
    def res(self):
        result="equal"
        return result 

class greater:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def __str__(self):
        return "(+ "+str(self.number1)+" "+str(self.number2)+" )"
    def res(self):
        if self.number1>self.number2:
            result=self.number1
            return result       
        else:
            result=self.number2
            return result 

class lesser:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def __str__(self):
        return "(+ "+str(self.number1)+" "+str(self.number2)+" )"
    def res(self):
        if self.number1<self.number2:
            result=self.number1
            return result       
        else:
            result=self.number2
            return result 


class num:
    def __init__(self,number5):
        self.number5=number5
    def __str__(self):
        return str(self.number5)

    def res(self):
        return int(self.number5)


class cons:
    def __init__(self,left,right):
        self.left=left
        self.right=right 
    
class atom:
    def __init__(self,at):
        self.at=at

   

class E:
    def __init__(self,opt):
        self.opt=opt
    def __str__(self):
        if len(self.opt)==1:
            return self.opt
        elif len(self.opt)==3:
            return iff(str(self.opt[1]),str(self.opt[2]),str(self.opt[3]))
        else:
            return 0
       
class iff:
    def __init__(self,op1,op2,op3):
        self.op1=op1
        self.op2=op2
        self.op3=op3
    def __str__(self):
        return "if(" + str(self.op1) + "," +str(self.op2)+ "," + str(self.op3) + ")"
    def delta(self):
        if self.op1=="+":
            return int(self.op2)+int(self.op3)
        elif self.op1=="-":
            return int(self.op2)-int(self.op3)
        elif self.op1=="*":
            return int(self.op2)*int(self.op3)
        elif self.op1=="/":
            return int(self.op2)/int(self.op3)
        elif self.op1==">":
            return int(self.op2) > int(self.op3)       
                        
        elif self.op1=="<":
            return int(self.op2) < int(self.op3)
        elif self.op1=="=":
            return "equal"
        elif self.op1==">":
            return int(self.op2) >= int(self.op3)       
                        
        elif self.op1=="<":
            return int(self.op2) <= int(self.op3)

def ee(*do):
    for i in do:
        opt=i
        return(opt)

class val:
    def __init__(self,a):
        self.a=a
    def __str__(self):
        return str(self.a)
    def value(self):
        return str(self.a)

class Boo:
    def __init__(self,bo):
        self.bo=bo
    def __str__(self):
        return str(self.bo)

class prim:
    def __init__(self,pr):
        self.pr=pr
    def value(self):
        return str(self.pr)
        

j1=iff('<=',7,7)
print(j1)
print(j1.delta())