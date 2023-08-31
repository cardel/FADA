"""
Carlos A Delgado
31 de Agosto
Punto 1 y 2 de recurrencias
"""

def T1(n):
    if n==1:
        return 8
    else:
        return 2*T1(n/2)+n

def T2(n):
    if n==1:
        return 9
    else:
        return 5*T2(n/3)+2*n

lst = [2**x for x in range(1,11)]
for i in lst:
    print("T1({}) = {}".format(i,T1(i)))

lst = [3**x for x in range(1,11)]
for i in lst:
    print("T2({}) = {}".format(i,T2(i)))
