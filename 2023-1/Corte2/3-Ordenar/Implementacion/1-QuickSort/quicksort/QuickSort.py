"""
Autor: Carlos Andres Delgado
Fecha: 13/06/2023

Implementación de QuickSort
"""
import numpy as np
import random
class QuickSort:

  def __init__(self, arr) -> None:
    self.arr = arr
    self.n = arr.shape[0]
  
  """
  Procedimiento partition
  Estructura el arreglo de tal manera que los elementos menores al pivote queden al principio y los mayores queden al final
  
  """
  def quicksort(self, low, high):
    if low < high:
      j = self.partition(low, high)
      self.quicksort(low, j)
      self.quicksort(j+1, high)

  def partition(self, low, high):
    i = low
    j = high

    pivot = self.arr[low]

    while i < j:
      while not(self.arr[i] >= pivot) and i < high:
        i += 1
      while not(self.arr[j] < pivot) and j > low:
        j -= 1
      if i < j:
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
    return j

  def quicksort_randomized(self, low, high):
    if low < high:
      j = self.partition_randomized(low, high)
      self.quicksort(low, j)
      self.quicksort(j+1, high)

  def partition_randomized(self, low, high):
    i = low
    j = high

    pivot = self.arr[random.randint(low, high-1)]

    while i < j:
      while not(self.arr[i] >= pivot) and i < high:
        i += 1
      while not(self.arr[j] < pivot) and j > low:
        j -= 1
      if i < j:
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
    return j
