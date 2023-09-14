"""
Carlos A Delgado
14 de Septiembre de 2023
Estimación de la raiz cuadrada
"""

def raiz(x,d):
    a = 1
    while abs(x - a**2) > d:
        a = (x/a + a)/2
    return a

print(raiz(9,0.0000001))
print(raiz(4563,0.0000001))
print(raiz(42,0.0000001))

