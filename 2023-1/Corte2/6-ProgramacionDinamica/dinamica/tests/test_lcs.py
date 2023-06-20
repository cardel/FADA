"""
Autor: Carlos A Delgado
Fecha: 20-06-2023
Pruebas del algoritmo de la subsecuencia más larga
"""

import unittest
import numpy as np  

from algorithms.lcs import lcs

class TestLCS(unittest.TestCase):
  def test_lcs1(self):
    x = "ABCBDAB"
    y = "BDCABA"
    lcsobj = lcs()
    self.assertEqual(lcsobj.cost_lcs(x, y), 4)

  def test_matrix_lcs1(self):
    x = "ABCBDAB"
    y = "BDCABA"
    lcsobj = lcs()
    lcsobj.cost_lcs(x, y)
    self.assertTrue(np.array_equal(lcsobj.c, np.array([[0., 0., 0., 0., 0., 0., 0.],[0., 0., 0.,0, 1., 1., 1.],[0., 1., 1., 1., 1., 2., 2.],[0., 1., 1., 2., 2., 2., 2.],[0., 1., 1., 2., 2., 3., 3.],[0., 1., 2., 2., 2., 3., 3.],[0., 1., 2., 2., 3., 3., 4.],[0., 1., 2., 2., 3., 4., 4.]])))

  def test_lcs2(self):
    x = "ABCDADAADADADADADDCCCCBBBMNJEDSSSA"
    y = "BABBBNMJEDSSSA"
    lcsobj = lcs()
    self.assertEqual(lcsobj.cost_lcs(x, y), 13)

