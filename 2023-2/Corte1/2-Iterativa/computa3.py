"""
Carlos A Delgado
Ejercicio computa 3 diapositivas
12 de Septiembre de 2023
"""
def computa3(n):
    a = 0
    i = 1
    while (i<=n):
        inv = sum([i**3 for i in range(0,i*1)])
        print(f"a: {a} y {inv}")
        a += i**3
        i+=1

computa3(20)
