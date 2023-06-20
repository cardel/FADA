"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Algoritmo para aplicar busqueda binaria en un arreglo ordenado
"""

import numpy as np
class BinarySearch:
  
  def __init__(self,array):
    self.array = array

  def search(self, p, r, x):
    if p>r:
      raise Exception("El elemento no se encuentra en el arreglo")
    else:
      q = (p+r)//2
      if x == self.array[q]:
        return q
      elif x < self.array[q]:
        return self.search(p,q-1,x)
      else:
        return self.search(q+1,r,x)
