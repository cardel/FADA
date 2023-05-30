"""
Carlos A Delgado
30 de Mayo de 2023
Pruebas sobre los montones
"""
from Monton import heap

def test_heapity():
  monton = heap(10)
  monton.arr = [4,14,7,2,8,1,0,0,0,0]
  monton.heapify(1)
  assert [14,8,7,2,4,1,0,0,0,0] == monton.arr


  monton = heap(13)
  monton.arr = [10,15,12,8,13,7,8,6,7,2,11,3,4]
  monton.heapify(1)
  assert [15,13,12,8,11,7,8,6,7,2,10,3,4] == monton.arr
