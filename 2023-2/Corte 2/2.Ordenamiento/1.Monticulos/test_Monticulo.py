"""
Prueba del moniticulo binario
Autor: Carlos A Delgado
Fecha: 31-Oct-2023
"""

import unittest
from Monticulo import Monticulo

class MonticuloTest(unittest.TestCase):
    def test_heapify_1(self):
        m = Monticulo(7)
        m.lista = [8,6,9,1,2,3,7] 
        m.heapify(1)
        self.assertEqual(m.lista,[9,6,8,1,2,3,7] )

    def test_heapify_2(self):
        m = Monticulo(6)
        m.lista = [4,14,7,2,8,1]
        m.heapify(1)
        self.assertEqual(m.lista,[14,8,7,2,4,1])


    def test_build_heap(self):
        m = Monticulo(7)
        m.lista = [8,6,9,1,2,3,7] 
        m.build_heap()
        self.assertEqual(m.lista,[9,6,8,1,2,3,7] )

    def test_heap_sort(self):
        m = Monticulo(10)
        m.lista = [8,6,9,1,2,3,7,5,4,10]
        m.heap_sort()
        self.assertEqual(m.lista,[1,2,3,4,5,6,7,8,9,10])




    
