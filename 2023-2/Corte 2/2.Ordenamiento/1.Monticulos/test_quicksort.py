import unittest
from QuickSort import QuickSort


class test_QuickSort(unittest.TestCase):
    def test_partition(self):
        obj = QuickSort([8,6,9,1,2,3,7])
        j = obj.partition(1,7)
        self.assertEqual(obj.lst,[7,6,3,1,2,9,8])
        self.assertEqual(5,j)

    def test_partitionB(self):
        obj = QuickSort([10,2,3,4,5,6,7,8,9,1])
        j = obj.partition(1,10)
        self.assertEqual(obj.lst,[1,2,3,4,5,6,7,8,9,10])
        assert j == 9

    def test_partitionC(self):
        obj = QuickSort([0,2,3,4,5,6,7,8,9,1])
        j = obj.partition(1,10)
        self.assertEqual(obj.lst,[0,2,3,4,5,6,7,8,9,1])
        assert j == 1

    def test_partitionD(self):
        obj = QuickSort([0,2,3,4,-5,6,7,8,9,1])
        j = obj.partition(5,10)
        self.assertEqual(obj.lst,[0,2,3,4,-5,6,7,8,9,1])
        assert j == 5

    def test_sortA(self):
        obj = QuickSort([8,6,9,1,2,3,7])
        obj.sort(1,7)
        self.assertEqual(obj.lst,[1,2,3,6,7,8,9])

    def test_sortB(self):
        obj = QuickSort([10,2,3,4,5,6,7,8,9,1])
        obj.sort(1,10)
        self.assertEqual(obj.lst,[1,2,3,4,5,6,7,8,9,10])
