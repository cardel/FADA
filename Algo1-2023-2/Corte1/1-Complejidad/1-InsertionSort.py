"""
Ejemplo algoritmo Insertion Sort
Carlos A Delgado
31 de Agosto de 2023
"""
import numpy as np
def insertion_sort(A):
    cnt = 0
    for j in range(2,len(A)+1):
        cnt+=1 #Ingreso al for
        key = A[j-1]
        cnt+=1
        i = j-1
        cnt+=1
        while i>0 and A[i-1]>key:
            cnt+=1 #Ingreso al while
            A[i] = A[i-1]
            cnt+=1
            i = i-1
            cnt+=1
        cnt+=1 #Salida del while
        A[i] = key
        cnt+=1
    cnt+=1 #Salida del for
    return cnt

lista = [5,2,4,6,1,3,7,8,9,10,3,9,16]
insertion_sort(lista)
print(lista)


lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def f_mejor_caso(n):
    return n+4*(n-1)

print(f"Mejor caso: {f_mejor_caso(len(lista))} {insertion_sort(lista)}")

def f_peor_caso(n):
    return n+3*(n-1)+(n+2)*(n-1)/2+(n-1)*n

lista = [13,12,11,10,9,8,7,6,5,4,3,2,1]
print(f"Peor caso: {f_peor_caso(len(lista))} {insertion_sort(lista)}")

def f_caso_promedio(n):
    return n+3*(n-1)+(n-1)*n/4+0.5*(n-1)+(n-1)*n/2-(n-1)


for n in [10,20,30,50,80,90,100,200,300,400,500,600,700,800,900,1000]:
    exp = 100
    tiempo = 0
    for i in range(exp):
        lista = np.random.randint(0,100000,n)
        tiempo += insertion_sort(lista)
    
    tiempo = tiempo/exp
    print(f"Tamaño = {n} Tiempo promedio: {tiempo} {f_caso_promedio(n)} porcentaje {tiempo/f_caso_promedio(n)}%")


