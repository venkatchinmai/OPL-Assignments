# Test case 1
# final=add(num(3),mul(num(6),add(num(7),num(8))))
# print(final)
# (+ 3 (* 6 (+ 7 8 ) ) )
#cons(atom(+),cons(atom(3),cons(cons(atom(*),cons(6))cons(cons(atom(+),cons(atom(7),cons(atom(8))empty()))empty()))empty()))

# Test case 2
# final=mul(add(6,10),8)
# print(final)
# (* (+ 6 10 ) 8 )
#cons(atom(*)cons(atom(+),cons(atom(6)cons(atom(10))cons(atom(8))empty())empty()))

# Test case 3
# first=mul(8,add(7,12))
# final=add(2,first)
# print(final)
# (+ 2 (* 8 (+ 7 12 ) ) )
#cons(atom(+),cons(atom(2),cons(cons(atom(*),cons(8))cons(cons(atom(+),cons(atom(7),cons(atom(12))empty()))empty()))empty()))


# Test case 4
# first=mul(8,add(7,12))
# print(final)
#(* 8 (+ 7 12 ) )
#cons(atom(*),cons(atom(8),cons(cons(atom(+)cons(atom(7),cons(atom(12))empty()))empty())))

# Test case 5
# first=add(8,mul(7,12))
# final=mul(5,first)
# print(final)
# (* 2 (+ 8 (* 7 12 ) ) )
#cons(atom(*),cons(atom(2),cons(cons(atom(+),cons(8))cons(cons(atom(*),cons(atom(7),cons(atom(12))empty()))empty()))empty()))


# Test case 6
# final=mul(num(5),add(num(6),mul(num(9),num(8))))
# print(final)
# (* 5 (+ 6 (* 9 8 ) ) )
#cons(atom(*),cons(atom(5),cons(cons(atom(+),cons(6))cons(cons(atom(*),cons(atom(9),cons(atom(8))empty()))empty()))empty()))

# Test case 7
# final=add(add(4,1),8)
# print(final)
# (+ (+ 4 1 ) 8 )
#cons(atom(+)cons(atom(+),cons(atom(4)cons(atom(1))cons(atom(8))empty())empty()))

# Test case 8
# first=mul(7,mul(7,12))
# final=mul(4,first)
# print(final)
# (* 2 (+ 8 (* 7 12 ) ) )
#cons(atom(*),cons(atom(7),cons(cons(atom(*),cons(1))cons(cons(atom(*),cons(atom(7),cons(atom(12))empty()))empty()))empty()))

# Test case 9
# first=add(8,mul(7,12))
# final=add(5,first)
# print(final)
# (* 2 (+ 8 (* 7 12 ) ) )
#cons(atom(*),cons(atom(5),cons(cons(atom(+),cons(8))cons(cons(atom(+),cons(atom(7),cons(atom(12))empty()))empty()))empty()))

# Test case 10
# final=add(add(6,1),8)
# print(final)
# (+ (+ 6 1 ) 8 )
#cons(atom(+)cons(atom(+),cons(atom(6)cons(atom(1))cons(atom(8))empty())empty())

# Test case 11
# final=mul(num(7),mul(num(6),add(num(7),num(10))))
# print(final)
# (* 7 (* 6 (+ 7 10 ) ) )
#cons(atom(*),cons(atom(7),cons(cons(atom(*),cons(6))cons(cons(atom(+),cons(atom(7),cons(atom(10))empty()))empty()))empty()))

# Test case 12
# first=add(10,mul(7,12))
# final=add(7,first)
# print(final)
# (* 2 (+ 8 (* 7 12 ) ) )
#cons(atom(*),cons(atom(7),cons(cons(atom(+),cons(10))cons(cons(atom(+),cons(atom(7),cons(atom(12))empty()))empty()))empty()))