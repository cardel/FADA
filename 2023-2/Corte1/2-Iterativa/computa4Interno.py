"""
Carlos A Delgado
12 de Septiembre de 2023
Ejercicio computa4 de las diapositivas ciclo interno
"""
def computa4(n):
    j = 0
    p = 4
    while j <= 2*n:
        inv = 4+2*j
        print(f"p = {p}, inv = {inv}")
        p += 2
        j += 1
   
computa4(10) 
