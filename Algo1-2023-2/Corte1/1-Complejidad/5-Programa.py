"""
Carlos A Delgado
Fecha: 07 Sep 2023
Solución programa5 diapositivas
"""

def programa5(n):
    cnt = 0
    i = 1
    cnt += 1
    while i <= n:
        cnt += 1 # Entrada while ext
        k = i
        cnt += 1
        while k<=n:
            cnt += 1 # Entrada while int
            k = k+2
            cnt += 1
        cnt += 1 # Salida while int
        k = 1
        cnt += 1
        while k<=i:
            cnt += 1 # Entrada while int
            k = k+1
            cnt += 1
        cnt += 1 # Salida while int
        i = i+2
        cnt += 1
    cnt += 1 # Salida while ext
    return cnt

def fprograma5(n):
    l1 = 1
    l2 = (n+3)/2
    l3_l6_l9 = 3*(n+1)/2
    l4 = (n+1)*(n+7)/8
    l5 = (n+1)*(n+3)/8   #Otra manera l4 - n(n+1)/2
    l7 = (n+1)*(n+3)/4
    l8 = (n+1)**2/4
    return l1+l2+l3_l6_l9+l4+l5+l7+l8

#Pruebas
for i in range(1,50,4):
    print("n=",i,"Programa5:",programa5(i),"Fprograma5:",fprograma5(i))
