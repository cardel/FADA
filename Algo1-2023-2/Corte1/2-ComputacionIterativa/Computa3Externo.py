"""
Carlos A Delgado
14 de Septiembre de 2023
Ejercicio computa3 ciclo externo
"""
def computa3(n):
    i = 1
    A = 0
    while i<=n:
        print(f"A = {A}, inv = {sum([k**3 for k in range(0,i)])}")
        A = A + i**3
        i = i+1
   
computa3(10) 
