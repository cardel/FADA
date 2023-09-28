"""
Carlos A Delgado
Evaluación T(n) = 2T(n/2) + n, T(1) = 1
"""

def T(n):
    if n==1:
        return 1
    else:
        return 2*T(n/2)+n

lst = [2**x for x in range(0,4)]

for n in lst:
    print(f"n = {n}, T(n) = {T(n)}")
