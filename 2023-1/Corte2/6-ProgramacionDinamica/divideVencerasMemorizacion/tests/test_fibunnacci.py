"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Descripcion: Pruebas unitarias para la funcion de fibunnacci con memorizacion
"""

import unittest
from fibunnacci.fibunnacci_memorizacion import Fibunnacci

class TestFibunnacci(unittest.TestCase):
  def test_fib1(self):
    fib = Fibunnacci()
    self.assertEqual(fib.fib(0), 0)

  def test_fib2(self):
    fib = Fibunnacci()
    self.assertEqual(fib.fib(1), 1)

  def test_fib3(self):
    fib = Fibunnacci()
    self.assertEqual(fib.fib(2), 1)

  def test_fib4(self):
    fib = Fibunnacci()
    self.assertEqual(fib.fib(3), 2)

  def test_fib5(self):
    fib = Fibunnacci()
    self.assertEqual(fib.fib(20), 6765)
