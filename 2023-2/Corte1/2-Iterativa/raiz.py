"""
Carlos A Delgado
05 de Sep de 2023
Estimación de la raiz cuadrada por método de Newton
"""
def raiz(x,d):
    print(f"Raiz de {x} con tolerancia {d}")
    a = 1 #raiz inicial
    while abs(a*a-x) > d:
        a = (a+x/a)/2
        print(a, abs(a*a-x))
    return a

print(raiz(2,0.0001))
print(raiz(3,0.0001))
print(raiz(1460021,0.0001))
