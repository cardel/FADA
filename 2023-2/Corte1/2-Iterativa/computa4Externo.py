"""
Carlos A Delgado
Sep 12 de 2023
Ejercicio de computa 4
"""
def computa4(n):
    i = 0
    s = 3
    while i <= n:
        inv = 3 + (8*n+12)*(i/2)
        print(f"s = {s}, inv = {inv}")
        s += 8*n+12
        i+=2

computa4(10)
