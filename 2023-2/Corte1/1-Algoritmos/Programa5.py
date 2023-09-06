"""
Carlos A Delgado
Programa5 diapositivas
05 de Sep de 2023
"""
import math
def programa5(n):
    i = 1
    cnt = 1
    while i<= n:
        cnt = cnt + 1 #Entrada while
        k = i
        cnt+= 1
        while k<= n:
            cnt += 1 #Entrada while
            k = k+2
            cnt += 1
        cnt += 1 #Salida while           
        k = 1
        cnt+= 1
        while k<=i:
            cnt += 1 #Entrada while
            k = k+1
            cnt += 1
        cnt += 1 #Salida while
        i=2*i
        cnt+= 1
    cnt = cnt + 1 #Salida while
    return cnt

def f5(n):
    l1 = 1
    l2 = math.log(n,2)+2
    l3 = math.log(n,2)+1
    l4 = (n/2+2)*math.log(n,2)-n+1 #i = 2,4,8,16,..,n
    l5 = (n/2+1)*math.log(n,2)-n+1 #i = 2,4,8,16,..,n
    l4 += n/2+1 #i = 1
    l5 += n/2+1 #i = 1
    l6 = math.log(n,2)+1
    l7 = math.log(n,2)+2*n
    l8 = 2*n-1
    l9 = math.log(n,2)
    return l1+l2+l3+l9+l6+l4+l5+l7+l8

lst = [2,4,8,16,32,64,128,256,512,1024,2048,4096]

for i in lst:
    print("n = ",i,"pasos = ",programa5(i),"f(n) = ",f5(i))



