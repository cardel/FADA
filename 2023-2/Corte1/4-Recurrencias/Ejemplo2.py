"""
Carlos A Delgado
19 de Septiembre de 2023
Ejemplo solución R.R T(n) = 2T(n/2)+1
"""
def T(n):
    if n==1:
        return 3
    else:
        return 2*T(n/2)+1

def f(n):
    return 4*n-1

lst = [2**x for x in range(0,11)]

#Prueba
for n in lst:
    print(f"n={n} T(n)={T(n)} f(n)={f(n)}")
