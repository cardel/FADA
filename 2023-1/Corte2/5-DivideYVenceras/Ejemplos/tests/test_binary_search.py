"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Pruebas del algoritmo BinarySearch
"""

import unittest
import numpy as np

from algorithms.Binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):
  def test_search_1(self):
    array = np.array([1,2,3,4,5,6])
    binarysearch = BinarySearch(array)
    self.assertEqual(binarysearch.search(0,array.shape[0]-1,6),5)


  def test_search_2(self):
    array = np.array([26,31,41,41,58,59])
    binarysearch = BinarySearch(array)
    self.assertEqual(binarysearch.search(0,array.shape[0]-1,59),5)

  def test_search_3(self):
    array = np.array([-2,1,2,3,3,4,4,4,5,5,6,12,12,13,23,34,53,64,123,123,123,312,312,354,634,4523])
    binarysearch = BinarySearch(array)
    self.assertEqual(binarysearch.search(0,array.shape[0]-1,53),16)

  def test_failed_search(self):
    array = np.array([1,2,3,4,5,6])
    binarysearch = BinarySearch(array)
    with self.assertRaises(Exception):
      binarysearch.search(0,array.shape[0]-1,7)
