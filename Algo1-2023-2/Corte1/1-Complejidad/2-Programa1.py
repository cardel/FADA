"""
Carlos A Delgado
Fecha: 07 de Sep de 2023
Solución del programa1 de las dispositivas
"""

def programa1(n):
    cnt = 0
    i = 1
    cnt += 1
    while i <= n:
        cnt += 1 #Entrada while
        j = 1
        cnt += 1
        while j <= n:
            cnt += 1 #Entrada while interno
            #linea 5 del código
            cnt += 1
            j = j + 1
            cnt += 1
        cnt += 1 #Salida while interno
        i += 1
        cnt += 1
    cnt += 1 #Salida while
    return cnt

def fprograma1(n):
    return 3*n+2+n*(n+1)+2*n**2

#Pruebas
for n in range(100,1100,100):
    T = programa1(n)
    print(f"{n} , {T} , {fprograma1(n)} , {T/fprograma1(n)}")
