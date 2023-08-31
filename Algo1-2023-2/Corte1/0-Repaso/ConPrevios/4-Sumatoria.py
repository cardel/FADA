"""
Carlos A Delgado
Solución segunda sumatoria
31 de Agosto de 2023
"""

def suma(n):
    suma = 0
    for i in range(1,n+1):
        suma += i**2-5
    return suma

def prueba():
    lst = [x for x in range(0,55)]
    for i in lst:
        print("n = ",i," Suma = ",suma(i))

prueba()
