"""
Carlos A Delgado S
14 de Marzo de 2023
Ejemplo de insertion sort
"""
import numpy as np

def insertion_sort(A):
  cnt = 0
  for j in range(2,len(A)+1):
    cnt += 1 #Cuento la entrada del for
    i = j-1
    cnt += 1
    key = A[j-1]
    cnt += 1
    while i>0 and A[i-1]>key:
      cnt += 1 #cuento la entrada del while
      A[i+1-1] = A[i-1]
      cnt += 1
      i = i-1
      cnt += 1
    cnt += 1 #Salida del while
    A[i+1-1] = key
    cnt += 1
  cnt += 1 #Salida del for inicial
  return cnt

def f_best(n):
  return 5*n-4

def f_worst(n):
  return 1.5*n**2 + 3.5*n - 4

def f_average(n):
  return 0.75*n**2 + 2.75*n - 3.5

listaP = [9,0,1,2,7,8,12,3]
insertion_sort(listaP)
print(listaP)

def ordenado(n):
  lista = []
  for i in range(0,n):
    lista.append(i)
  return lista

def ordenado_inverso(n):
  lista = []
  for i in range(n,0,-1):
    lista.append(i)
  
  return lista


def validacion():
  lista_n = [100,200,300,500,800]
  for n in lista_n:
    arr_o = ordenado(n)
    print("Tamaño ",n)
    print("Mejor caso ",insertion_sort(arr_o),f_best(n))
    arr_oi = ordenado_inverso(n)
    print("Peor caso ",insertion_sort(arr_oi),f_worst(n))
    average = 0
    for k in range(0,100):
      arr_av = np.random.randint(0,1000000,n)
      cnt_av = insertion_sort(arr_av)
      average += cnt_av
    average /= 100
    print("Caso promedio ",average, f_average(n))
    print("*****************************")

validacion()
