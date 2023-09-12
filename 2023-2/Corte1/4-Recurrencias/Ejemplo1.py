"""
Carlos A Delgado
12 de Septiembre 2023
Ejemplo de las diapositivas T(n) = 2T(n/4)+2n)
"""
from math import log
def T(n):
    if n==1:
        return 1
    else:
        return 2*T(n/4)+2*n

def f(n):
    return n**0.5-4*n*(0.5**(log(n,4))-1)

lst = [4**x for x in range(1,10)]

for n in lst:
    print(f"{n} {T(n)} {f(n)}")
