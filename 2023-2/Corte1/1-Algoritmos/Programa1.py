"""
Carlos A Delgado
Fecha: 29 de Agosto de 2023
Validacion de programa1 diapositivas
"""
import numpy as np
def programa1(n):
    i = 1
    cnt = 1
    while i <= n:
        cnt += 1 # Entrada del while externo
        j = 1
        cnt += 1
        while j <= n:
            cnt += 1 # Entrada del while interno
            #Hace la operación de matrices
            cnt += 1
            j += 1
            cnt +=1 
        cnt+=1 #Salida del while externo
        i += 1
        cnt += 1
    cnt += 1 #Salida del while externo
    return cnt

def fprograma2(n):
    return 1+2*n+(n+1)+n*(n+1)+2*n**2

#Pruebas
valores_aleatorios = np.random.randint(1, 300, 20)

for n in valores_aleatorios:
    c1 = programa1(n)
    c2 = fprograma2(n)
    print(f"{n} , {c1} , {c2}")
