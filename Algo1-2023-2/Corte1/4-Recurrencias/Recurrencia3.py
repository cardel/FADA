"""
Carlos A Delgado
21 de Sep de 2023
T(n) = T(n/2)+1
"""
import math
def T(n):
    if n==1:
        return 1
    else:
        return T(n/2)+1

def f(n):
    return 1+math.log2(n)

lst = [2**x for x in range(0,20)]

for n in lst:
    print(f"n = {n}, f(n) = {f(n)}, T(n) = {T(n)}")
