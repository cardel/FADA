"""
Autor: Carlos A Delgado
Fecha: 13/06/2023

Pruebas del algoritmo radix sort
"""
import numpy as np
from sorting.Radix_sort import Radix_sort
def test_radix_sort1():
  obj_radix = Radix_sort(np.array([2,5,3,1,2,3,4,3]),1)
  obj_radix.sort()
  assert np.array_equal(obj_radix.arr,np.array([1,2,2,3,3,3,4,5]))

def test_radix_sort2():
  obj_radix = Radix_sort(np.array([200,101,290,389,123,655,999,103]),3)
  obj_radix.sort()  
  assert np.array_equal(obj_radix.arr,np.array([101,103,123,200,290,389,655,999]))

  obj_radix = Radix_sort(np.array([200,90,290,901,123,655,9,103]),3)
  obj_radix.sort()
  assert np.array_equal(obj_radix.arr,np.array([9,90,103,123,200,290,655,901]))
