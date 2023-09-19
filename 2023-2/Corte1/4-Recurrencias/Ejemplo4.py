"""
Carlos A Delgado
19 de Septiembre de 2023
Ejemplo T(n) = 2T(n/2)+n^2 T(1)=1
"""
def T(n):
    if n==1:
        return 1
    else:
        return 2*T(n/2)+n**2

def f(n):
    return 2*n**2-n

#Prueba
lst = [2**x for x in range(0,11)]

for n in lst:
    print(f"n = {n} T(n) = {T(n)} f(n) = {f(n)}")
