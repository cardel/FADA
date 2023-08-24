"""
Carlos A Delgado
24 Agosto de 2023
Sumatoria desde i = -3 hasta n de i^2
"""

def suma(n):
    suma = 0
    for i in range(-3,n+1):
        suma+=i**2
    return suma

def fsuma(n):
    a = (n+4)*(n+5)*(2*n+9)/6
    b = -8*(n+4)*(n+5)/2
    c = 16*(n+4)
    return a+b+c

for n in range(0,40):
    print(suma(n),fsuma(n))
