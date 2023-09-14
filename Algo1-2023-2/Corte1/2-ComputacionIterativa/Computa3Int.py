"""
Carlos A Delgado
14 de Septiembre de 2023
Ejercicio computa3 de las diapositivas ciclo interno
"""

def computa3(i):
    j = 1
    B = 1
    while j <= 3:
        print(f"B = {B}, inv = {i**(j-1)}")
        B = B * i
        j = j + 1 

computa3(10)
computa3(12)
