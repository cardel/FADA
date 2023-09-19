"""
Carlos A Delgado
19 de Septiembre de 2023
Ejemplo T(n) = 2T(n/2) + n
"""
import math
def T(n):
    if n==1:
        return 10
    else:
        return 2*T(n/2)+n

def f(n):
    return 10*n+n*math.log(n,2)

lst = [2**x for x in range(0,11)]

for n in lst:
    print(f"{n} {T(n)} {f(n)}")
