"""
Carlos A Delgado
Sep 05 de 2023
Algoritmo computa 3 de las diapositivas
"""

def computa3(n,i):
    B = 1
    j = 1
    while j <= 3:
        print(f"j = {j}, B = {B}, inv = {i**(j-1)}")
        B = B * i
        j = j + 1


computa3(8,7)
