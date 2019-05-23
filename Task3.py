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

# Test case 1
# final=add(num(3),mul(num(6),add(num(7),num(8))))
# print(final)
# (+ 3 (* 6 (+ 7 8 ) ) )

# Test case 2
# final=mul(add(6,10),8)
# print(final)
# (* (+ 6 10 ) 8 )

# Test case 3
# first=mul(8,add(7,12))
# final=add(2,first)
# print(final)
# (+ 2 (* 8 (+ 7 12 ) ) )

# Test case 4
# first=mul(8,add(7,12))
# second=(add(7,first))
# final=add(2,second)
# print(final)
# (+ 2 (+ 7 (* 8 (+ 7 12 ) ) ) )

# Test case 5
# first=mul(8,add(7,12))
# final=add(add(50,40),first)
# print(final)
# (+ (+ 50 40 ) (* 8 (+ 7 12 ) ) )

# Test case 6
# first=mul(8,add(7,12))
# final=add(add(50,mul(70,80)),first)
# print(final)
# (+ (+ 50 (* 70 80 ) ) (* 8 (+ 7 12 ) ) )

# Test case 7
# first=mul(8,add(7,mul(14,add(16,20))))
# final=add(add(50,mul(70,80)),first)
# print(final)
# (+ (+ 50 (* 70 80 ) ) (* 8 (+ 7 (* 14 (+ 16 20 ) ) ) ) )

# Test case 8
# first=mul(5,add(11,mul(14,add(16,20))))
# second=(add(7,first))
# final=add(add(22,mul(70,80)),mul(20,second))
# print(final)
# (+ (+ 22 (* 70 80 ) ) (* 20 (+ 7 (* 5 (+ 11 (* 14 (+ 16 20 ) ) ) ) ) ) )

# Test case 9
# first=add(5,add(11,mul(14,add(16,20))))
# second=(mul(7,add(7,first)))
# third=add(first,second)
# final=add(add(22,mul(70,80)),mul(20,third))
# print(final)
# (+ (+ 22 (* 70 80 ) ) (* 20 (+ (+ 5 (+ 11 (* 14 (+ 16 20 ) ) ) ) (* 7 (+ 7 (+ 5 (+ 11 (* 14 (+ 16 20 ) ) ) ) ) ) ) ) )

# Test case 10
# first=mul(20,add(7,add(8,mul(20,19))))
# final=mul(add(22,mul(70,80)),mul(20,first))
# print(final)
# (* (+ 22 (* 70 80 ) ) (* 20 (* 20 (+ 7 (+ 8 (* 20 19 ) ) ) ) ) )

# Test case 11
# final=mul(add(22,mul(70,80)),mul(20,mul(20,add(70,add(100,40)))))
# print(final)
# (* (+ 22 (* 70 80 ) ) (* 20 (* 20 (+ 70 (+ 100 40 ) ) ) ) )

# Test case 12
# first=add(20,mul(20,30))
# final=mul(add(22,mul(70,80)),mul(20,mul(20,add(70,add(100,first)))))
# print(final)
# (* (+ 22 (* 70 80 ) ) (* 20 (* 20 (+ 70 (+ 100 (+ 20 (* 20 30 ) ) ) ) ) ) )