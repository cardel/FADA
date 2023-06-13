"""
Autor: Carlos A Delgado
Fecha: 13/06/2023
Implementación del algoritmo counting sort
"""
import numpy as np
class Counting_sort:
  def __init__(self,arr) -> None:
    self.arr = arr
    self.k = np.max(arr)
    self.n = arr.shape[0]

  """
  Para ordenar, vamos a hacerlo lo siguiente
  1. Creamos el arreglo B de tamaño n
  2. Creamos el arreglo C de tamaño k
  3. Recorremos el arreglo A y contamos cuantas veces aparece cada elemento y lo mapeamos en C
  4. Recorremos el arreglo C y sumamos el valor de la posición i con el valor de la posición i-1
  5. Recorremos el arreglo A desde el final hasta el inicio y vamos colocando los elementos en el arreglo B de acuerdo al conteo que tenemos en C
  """
  def sort(self):
    B = np.zeros(self.n,dtype=int)
    C = np.zeros(self.k,dtype=int)

    for i in range(self.n):
      C[self.arr[i]-1] += 1

    for i in range(1,self.k):
      C[i] += C[i-1]

    for i in range(self.n-1,-1,-1):
      B[C[self.arr[i]-1]-1] = self.arr[i]
      C[self.arr[i]-1] -= 1

    return B
