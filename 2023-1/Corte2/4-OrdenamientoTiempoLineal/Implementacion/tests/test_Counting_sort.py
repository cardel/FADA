"""
Autor: Carlos A Delgado
Fecha: 13/06/2023

Pruebas del algoritmo counting sort
"""
from sorting.Counting_sort import Counting_sort
import numpy as np

def test_counting():
  obj_counting = Counting_sort(np.array([2,5,3,1,2,3,4,3]))
  assert np.array_equal(obj_counting.sort(),np.array([1,2,2,3,3,3,4,5]))

def test_counting2():
  obj_counting = Counting_sort(np.array([2,5,3,1,2,3,4,3,5,6,7,8,9,10,11,12,13,14,15,16]))
  assert np.array_equal(obj_counting.sort(),np.array([1,2,2,3,3,3,4,5,5,6,7,8,9,10,11,12,13,14,15,16]))
