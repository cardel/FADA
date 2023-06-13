"""
Carlos A Delgado
30 de Mayo de 2023
Pruebas sobre los montones
"""
from Monton import heap

def test_heapify():
  monton = heap(10)
  monton.arr = [4,14,7,2,8,1,0,0,0,0]
  monton.heapify(1)
  assert [14,8,7,2,4,1,0,0,0,0] == monton.arr


  monton = heap(13)
  monton.arr = [10,15,12,8,13,7,8,6,7,2,11,3,4]
  monton.heapify(1)
  assert [15,13,12,8,11,7,8,6,7,2,10,3,4] == monton.arr

def test_build_heap():
  monton = heap(10)
  monton.arr = [1,4,5,10,12,19,22,35,40,2]
  monton.build_heap()
  assert [40,35,22,10,12,19,5,4,1,2] == monton.arr

  monton = heap(9)
  monton.arr = [1,8,6,3,7,9,10,2,4]
  monton.build_heap()
  assert [10,8,9,4,7,1,6,2,3] == monton.arr

def test_heap_sort():
  monton = heap(10)
  monton.arr = [1,4,5,10,12,19,22,35,40,2]
  monton.heap_sort()
  assert [1,2,4,5,10,12,19,22,35,40] == monton.arr

  monton = heap(9)
  monton.arr = [1,8,6,3,7,9,10,2,4]
  monton.heap_sort()
  assert [1,2,3,4,6,7,8,9,10] == monton.arr
