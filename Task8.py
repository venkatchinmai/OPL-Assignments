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
        return "(* "+str(self.number3)+" "+str(self.number4)+" )"
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

class cons:
    def __init__(self,left,right):
        self.left=left
        self.right=right 
    
class atom:
    def __init__(self,at):
        self.at=at

class empty:
    def __inint__(self):
        self.a=None



    
class eee:
    def __init__(self,e):
        self.e=e

class If:
    def __init__(self,con,num1,num2):
        self.con=con
        self.num1=num1
        self.num2=num2

class Bool:
    def __init__(self,oper):
        self.opr=oper


def desugar(sexpr):
    if isinstance(sexpr,If):
        if isinstance(sexpr.left,Bool):
            if (sexpr.left.e=="+"):
                a=desugar(sexpr.num1.num2)
                b=desugar(sexpr.num1.num1.num2)
                return add(a,b)
            elif (sexpr.left.e=="*"):
                a=desugar(sexpr.num1.num2)
                b=desugar(sexpr.num1.num1.num2)
                return mul(a,b)
    else:
        return num(sexpr.e)


a = add(3,mul(5,3))
k=cons(atom("+"),cons(atom("3"),cons(cons(atom("*"),cons(atom("5"),cons(atom("3"),empty()))),empty())))
objc=desugar(k)
print(objc)

j1=desugar(If( Bool(true),num(5),num(6)))
print(j1)



# Cons( Atom("if"),  Cons( Atom("true"),  Cons( Atom("5",  Cons( Atom("6"),  Empty()))))