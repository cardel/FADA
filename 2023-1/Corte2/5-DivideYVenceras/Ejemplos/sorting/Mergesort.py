"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Algoritmo Mergesort
"""
import numpy as np
class MergeSort:
  
  def __init__(self, array):
    self.array = array

  """
  Este método divide el arreglo
  """
  def sort( self , p ,r):
    if p<r:
      q = (p+r)//2
      self.sort(p,q)
      self.sort(q+1,r)
      self.merge(p,q,r)

  """
  Este método toma dos arreglos ordenados y los mezcla en un solo arreglo ordenado
  """
  def merge(self,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = np.zeros(n1+1)
    R = np.zeros(n2+1)
    for i in range(n1):
      L[i] = self.array[p+i]
    for j in range(n2):
      R[j] = self.array[q+j+1]
    L[n1] = np.inf
    R[n2] = np.inf
    i = 0
    j = 0
    for k in range(p,r+1):
      if L[i] <= R[j]:
        self.array[k] = L[i]
        i = i+1
      else:
        self.array[k] = R[j]
        j = j+1
