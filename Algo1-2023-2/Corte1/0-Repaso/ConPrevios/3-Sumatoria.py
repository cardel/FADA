"""
Carlos A Delgado
Solución punto sumatoria 1
31 de Agosto de 2023
"""

def suma(n):
    suma = 0
    for i in range(1,n+1):
        suma += 2*i+2

    return suma

def prueba():
    lst = [x for x in range(1,52)]
    for i in lst:
        print(f"n = {i} -> {suma(i)}")

prueba()
