"""
Carlos A Delgado
21 de Sep de 2023
Solución T(n) = 3T(n/4) + n, T(1) = 1
"""
import math
def T(n):
    if n==1:
        return 1
    else:
        return 3*T(n/4)+n

def f(n):
    return -4*n**(math.log(3,4))+4*n+n**(math.log(3,4))

lst = [4**x for x in range(1,11)]

for n in lst:
    print(f"n={n}, T(n)={T(n)}, f(n)={f(n)}")






