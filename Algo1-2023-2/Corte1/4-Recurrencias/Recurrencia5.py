"""
Carlos A Delgado
21 de Septiembre de 2023
T(n) = 2T(n/2) + n²
"""

def T(n):
    if n == 1:
        return 1
    else:
        return 2*T(n/2) + n*n

def f(n):
    return 2*n*n - n

lst = [2**i for i in range(1, 10)]

for n in lst:
    print(f"n={n} T(n)={int(T(n))} f(n)={int(f(n))}")
