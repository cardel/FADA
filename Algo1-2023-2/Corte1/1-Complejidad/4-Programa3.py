"""
Carlos A Delgado
Fecha 07 Septiembre 2023
Ejemplo programa3 de la clase
"""

def programa3(n):
    cnt = 0
    i = 1
    cnt += 1
    while i <= n:
        cnt += 1 #Entrada while ext
        k = i
        cnt += 1
        while k <= n:
            cnt += 1 #Entrada while int
            k = k+1
            cnt += 1
        cnt += 1 #Salida while int
        k = 1
        cnt += 1
        while k <= i:
            cnt += 1 #Entrada while int
            k = k+1
            cnt += 1
        cnt += 1 #Salida while int
        i = i+1
        cnt += 1
    cnt += 1 #Salida while ext
    return cnt

def fprograma3(n):
    return 4*n+2+n*(n+3)+n*(n+1)


print("n\tConteo\tFormula")
for i in range(100, 1100, 100):
    print("%d\t%d\t%d"%(i, programa3(i), fprograma3(i)))
