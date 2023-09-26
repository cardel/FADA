"""
Carlos A Delgado
21 de Sep de 2023
Solución R.R T(n) = 2T(n/2)+n, T(1) = 1
"""
import math
def T(n):
    if n==1:
        return 1
    else:
        return 2*T(n/2)+n

def f(n):
    return n+math.log2(n)*n

lst = [2**x for x in range(1,11)]

for n in lst:
    print(f"n = {n}, f(n) = {f(n)}, T(n) = {T(n)}")


