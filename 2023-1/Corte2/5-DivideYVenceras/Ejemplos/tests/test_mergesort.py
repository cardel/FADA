"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Pruebas del algoritmo Mergesort
"""

import unittest
import numpy as np

from sorting.Mergesort import MergeSort

class TestMergeSort(unittest.TestCase):
      
  def test_sort(self):
    array = np.array([5,2,4,6,1,3])
    mergesort = MergeSort(array)
    mergesort.sort(0,array.shape[0]-1)
    self.assertTrue(np.array_equal(mergesort.array,np.array([1,2,3,4,5,6])))

  def test_sort_2(self):
    array = np.array([31,41,59,26,41,58])
    mergesort = MergeSort(array)
    mergesort.sort(0,array.shape[0]-1)
    self.assertTrue(np.array_equal(mergesort.array,np.array([26,31,41,41,58,59])))

  def test_sort_3(self):
    array = np.array([5,2,4,6,1,3,-2,3,23,123,123,123,12,312,354,53,4,4,13,12,312,4523,64,634,5,34])
    mergesort = MergeSort(array)
    mergesort.sort(0,array.shape[0]-1)
    self.assertTrue(np.array_equal(mergesort.array,np.array([-2,1,2,3,3,4,4,4,5,5,6,12,12,13,23,34,53,64,123,123,123,312,312,354,634,4523])))
