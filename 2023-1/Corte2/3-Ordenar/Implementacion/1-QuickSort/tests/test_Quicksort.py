"""
Autor: Carlos A Delgado
Fecha: 13/06/2023
Pruebas
"""
from quicksort.QuickSort import QuickSort
import numpy as np

def test_partition():
  arr = np.array([10, 7, 8, 9, 1, 5])
  objQuickSort = QuickSort(arr)

  assert objQuickSort.partition(0, arr.shape[0]-1) == 4
  assert np.array_equal(objQuickSort.arr, np.array([5,7,8,9,1,10]))

def test_partition2():
  arr = np.array([5,3,2,6,4,1,3,7])
  objQuickSort = QuickSort(arr)

  j = objQuickSort.partition(0, arr.shape[0]-1)
  assert np.array_equal(objQuickSort.arr, np.array([3,3,2,1,4,6,5,7]))
  assert j == 4

def test_quicksort():
  arr = np.array([10, 7, 8, 9, 1, 5])
  objQuickSort = QuickSort(arr)
  objQuickSort.quicksort(0, arr.shape[0]-1)
  assert np.array_equal(objQuickSort.arr, np.array([1,5,7,8,9,10]))

def test_violence_quicksort():
  arr = np.array([2,3,2,4,2,123,13,123,12,312,312,312,3,123,124,12,412,412,4])
  objQuickSort = QuickSort(arr)
  objQuickSort.quicksort(0, arr.shape[0]-1)
  assert np.array_equal(objQuickSort.arr, np.array([2,2,2,3,3,4,4,12,12,13,123,123,123,124,312,312,312,412,412]))


def test_quicksort_randomized():
  arr = np.array([10, 7, 8, 9, 1, 5])
  objQuickSort = QuickSort(arr)
  objQuickSort.quicksort_randomized(0, arr.shape[0]-1)
  assert np.array_equal(objQuickSort.arr, np.array([1,5,7,8,9,10]))

def test_violence_quicksort_randomized():
  arr = np.array([2,3,2,4,2,123,13,123,12,312,312,312,3,123,124,12,412,412,4])
  objQuickSort = QuickSort(arr)
  objQuickSort.quicksort_randomized(0, arr.shape[0]-1)
  assert np.array_equal(objQuickSort.arr, np.array([2,2,2,3,3,4,4,12,12,13,123,123,123,124,312,312,312,412,412]))
