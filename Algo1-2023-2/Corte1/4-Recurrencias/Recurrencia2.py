"""
Carlos A Delgado S
21 de Septiembre de 2023
T(n) = 2T(n/2)+1
"""

def T(n):
    if n==1:
        return 1
    else:
        return 2*T(n/2)+1

def f(n):
    return 2*n-1

lst = [2**x for x in range(0,20)]

for n in lst:
    print(f"n = {n}, T(n) = {T(n)}, f(n) = {f(n)}")
