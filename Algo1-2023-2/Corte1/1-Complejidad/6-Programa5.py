"""
Carlos A Delgado
07 Sep de 2023
Ejemplo5 de las diapositivas
"""
import math
def programa5(n):
    cnt = 0
    i = 1
    cnt += 1
    while i<= n:
        cnt+=1 #Inicio ciclo ext
        k = i
        cnt+=1
        while k <= n:
            cnt+=1 #Inicio ciclo int
            k=k+2
            cnt+=1
        cnt+=1 #Fin ciclo int
        k = 1
        cnt+=1
        while k <= i:
            cnt+=1 #Inicio ciclo int
            k = k+1
            cnt+=1
        cnt+=1 #Fin ciclo int
        i = i*2
        cnt+=1
    cnt+=1 #Fin ciclo ext
    return cnt

def fprograma5(n):
    l1 = 1
    l2 = math.log(n,2)+2
    l3_6_9 = 3*math.log(n,2)+3
    l4 = ((n+4)/2)*math.log(n,2)-n+1+(n+2)/2
    l5 = ((n+2)/2)*math.log(n,2)-n+1+n/2
    l6 = math.log(n,2)+2*n
    l7 = 2*n-1
    return l1+l2+l3_6_9+l4+l5+l6+l7

#Prueba
lst = [2**x for x in range(1,11)]

for x in lst:
    print(programa5(x),fprograma5(x))
