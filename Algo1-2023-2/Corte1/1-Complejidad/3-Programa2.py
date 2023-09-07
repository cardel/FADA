"""
Carlos A Delgado
Fecha: 07/Sep/2023
Solución ejercicio programa2 de las diapositivas de la clase 3
"""

def programa2(n):
    cnt = 0
    s = 0
    cnt += 1
    i = 1
    cnt += 1
    while i <= n:
        cnt += 1 #Entrada del while
        t = 0
        cnt += 1
        j = 1
        cnt += 1
        while j <= i:
            cnt += 1 #Entrada del while
            t = t + 1
            cnt += 1
            j = j + 1
            cnt += 1
        cnt += 1 #Salida del while
        s = s + t
        cnt += 1
        i = i + 1
        cnt += 1
    cnt += 1 #Salida del while
    return cnt


def fprograma2(n):
    return 5*n+3+n*(n+3)/2+n*(n+1)


#Pruebas
for i in range(0,100,5):
    print("n=",i,"pasos=",programa2(i),"f(n)=",fprograma2(i))

