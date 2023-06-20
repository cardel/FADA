"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Pruebas del algoritmo Maximum
"""

import unittest
import numpy as np

from algorithms.Maximum import Maximum

class TestMaximum(unittest.TestCase):
  def test_maximum_1(self):
    array = np.array([5,2,4,6,1,3])
    maximum = Maximum(array)
    self.assertEqual(maximum.getMaximum(0,array.shape[0]-1),6)

  def test_maximum_2(self):
    array = np.array([31,41,59,26,41,58])
    maximum = Maximum(array)
    self.assertEqual(maximum.getMaximum(0,array.shape[0]-1),59)

  def test_maximum_3(self):
    array = np.array([5,2,4,6,1,3,-2,3,23,123,123,123,12,312,354,53,4,4,13,12,312,4523,64,634,5,34])
    maximum = Maximum(array)
    self.assertEqual(maximum.getMaximum(0,array.shape[0]-1),4523)
