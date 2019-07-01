
#j0
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

#Sexpr
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

#J1   
opt=[]
# class E:
#     def __init__(self,*args):
#         self.opt=args
#         self.i=0
#     def EV(self):
#         if len(self.opt)==1:
#             return str(self.opt)
#         elif len(self.opt)==3:
#             for opt in args:
#                 opt[self.i]=args
                
#             return iff(str(self.opt[1]),str(self.opt[2]),str(self.opt[3]))
#         else:
#             return E(self.opt)
    
class iff:
    def __init__(self,op1,op2,op3):
        self.op1=op1
        self.op2=op2
        self.op3=op3
    def __str__(self):
        if self.op2==' ':
            return "if(" + str(self.op1) + "," +"hole()"+ "," + str(self.op3) + ")"
        elif self.op3==' ':
            return "if(" + str(self.op1) + "," +str(self.op2)+ "," + "hole()" + ")"
        else:
            return "if(" + str(self.op1) + "," +str(self.op2)+ "," + str(self.op3) + ")"
def ee(*do):
    for i in do:
        opt=i
        return(str(opt))

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
        
def desugar(sexpr):
    if isinstance(sexpr,cons):
        if isinstance(sexpr.left,atom):
            if (sexpr.left.at=="if"):
                a=desugar(sexpr.right.left)
                b=desugar(sexpr.right.right.left)
                c=desugar(sexpr.right .right.right.left)
                return iff(a,b,c)
            elif isinstance(sexpr.left,val):
                a=desugar(sexpr.right.left)
                return val(a)
    else:
        return num(sexpr.at)


#j=cons(atom("if"),cons(atom(">"),cons(atom(num(8)),cons(atom(num(9)),empty()))))
#print(desugar(j))



#Data structure to represent Contexts

class Context:
    def __init__(self,args):
        self.srgs=args
    
    
class ifcee:
    def __init__(self,c,e1,e2):
        self.c=c
        self.e1=e1
        self.e2=e2
    def __str__(self):
        return iff(self.c,self.e1,self.e2)

class ifece:
    def __init__(self,c,e1,e2):
        self.c=c
        self.e1=e1
        self.e2=e2
    def __str__(self):
        return iff(self.e1,self.c,self.e2)

class ifeec:
    def __init__(self,c,e1,e2):
        self.c=c
        self.e1=e1
        self.e2=e2
    def __str__(self):
        return iff(self.e1,self.e2,self.c)

        
j=(iff('>',6,' '))
print(j)
