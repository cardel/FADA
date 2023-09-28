"""
Ejercicio 4T(n/3)+3n
Carlos A Delgado, 28 de Sep 2023
"""
from math import log
def T(n):
    if n==1:
        return 1
    else:
        return 4*T(n/3)+3*n

def f(n):
    return n**log(4,3) + 3**2*(n**log(4,3)-n)


lst = [3**x for x in range(0,11)]

for n in lst:
    print(f"n = {n}, T(n) = {T(n)}, f(n) = {f(n)}")
