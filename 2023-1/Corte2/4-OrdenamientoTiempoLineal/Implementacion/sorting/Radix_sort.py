"""
Autor: Carlos A Delgado
Fecha: 13/06/2023

Implementación del algoritmo radix sort
"""
import numpy as np
class Radix_sort:
  def __init__(self,arr,n_digits) -> None:
    self.arr = arr
    self.n = arr.shape[0]
    self.n_digits = n_digits

  def sort(self):
    for i in range(self.n_digits):
      factor = 10**i
      val = self.arr / factor % 10 #Digitos
      index = np.argsort(val)
      self.arr = self.arr[index]

