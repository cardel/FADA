"""
Algoritmo insertion Sort
Autor: Carlos A Delgado
Fecha: 29 de Agosto de 2023
"""
import numpy as np
def insertion_sort(arreglo):
    cnt = 0
    for j in range(2,len(arreglo)+1):
        cnt += 1 #Elemento valido del primer while
        key = arreglo[j-1]
        cnt += 1
        i = j-1
        cnt += 1 
        while i>0 and arreglo[i-1]>key:
            cnt += 1 #Elemento valido del segundo while
            arreglo[i+1-1] = arreglo[i-1]
            cnt += 1
            i = i-1
            cnt += 1
        cnt += 1 #Salida del segundo while
        arreglo[i+1-1] = key
        cnt += 1
    cnt += 1 #Salida del primer while
    return cnt

def mejor_caso(n):
    return n+4*(n-1)
#Ejemplo del mejor caso
listaA = [1,2,3,4,5,6,7,8,9,10]
listaB = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print(insertion_sort(listaA),mejor_caso(len(listaA)))
print(insertion_sort(listaB),mejor_caso(len(listaB)))


def peor_caso(n):
    return n+3*(n-1)+(n-1)*(n+2)/2+n*(n-1)

def caso_promedio(n):
    return n+3*(n-1)+(n-1)*(n+2)/4+(n-2)*(n-1)/2

#Ejemplo del peor caso
listaC = [10,9,8,7,6,5,4,3,2,1]
listaD = [14,13,12,11,10,9,8,7,6,5,4,3,2,1]

print(insertion_sort(listaC),peor_caso(len(listaC)))
print(insertion_sort(listaD),peor_caso(len(listaD)))

#Ejemplo del caso promedio
calculo_promedio = 0
for i in range(0,1000):
    lista = np.random.randint(0,10000,100)
    calculo_promedio += insertion_sort(lista)
print(calculo_promedio/1000,caso_promedio(100))
#Ejemplo general
lista = [5,2,4,6,1,3,7,9,8,10,0,13,22,33,44,87,13,12]
insertion_sort(lista)
print(lista)
