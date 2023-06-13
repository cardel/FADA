"""
Autor: Carlos A Delgado
Fecha: 13/06/2023

Implementación del algoritmo bucket sort
"""
import numpy as np
class Bucket_sort:
  def __init__(self,arr,n) -> None:
    self.arr = arr
    self.n = n
    self.size = arr.shape[0]

  def sort(self):
    n = self.n
    buckets = [[] for _ in range(n)]

    for i in range(self.size):
      buckets[int(n*self.arr[i])].append(self.arr[i])

    for i in range(n):
      buckets[i].sort()

    index = 0
    for i in range(self.n):
      for j in range(len(buckets[i])):
        self.arr[index] = buckets[i][j]
        index += 1

    return self.arr
