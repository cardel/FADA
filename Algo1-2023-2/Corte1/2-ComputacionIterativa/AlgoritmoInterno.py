"""
Carlos A Delgado S
14 de Sep de 2013
Ejemplo ciclo interno ejemplo Algoritmo de de las diapositivas
"""

def algoritmo(n):
    j = 0
    p = 4
    print(f"S0 j = {j}, p = {p}, inv = {4+2*j}")
    while j<=2*n:
        print(f"p = {p}, inv = {4+2*j}")
        p += 2
        j += 1
    print(f"Sf j = {j}, p = {p} inv = {4+2*j}")
   
algoritmo(20) 
