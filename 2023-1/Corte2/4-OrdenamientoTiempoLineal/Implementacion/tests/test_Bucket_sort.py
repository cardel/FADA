"""
Autor: Carlos A Delgado
Fecha: 13/06/2023

Pruebas del algoritmo bucket sort
"""
from sorting.Bucket_sort import Bucket_sort
import numpy as np


def test_bucket_sort1():
  obj_bucket = Bucket_sort(np.array([0.2,0.5,0.3,0.1,0.2,0.3,0.4,0.3]),5)
  obj_bucket.sort()
  assert np.array_equal(obj_bucket.arr,np.array([0.1,0.2,0.2,0.3,0.3,0.3,0.4,0.5]))

def test_bucket_sort2():
  obj_bucket = Bucket_sort(np.array([0.2,0.5,0.3,0.1,0.2,0.3,0.4,0.3,0.5,0.6,0.7,0.8,0.9,0.15,0.23,0.09,0.05]),5)
  obj_bucket.sort()
  assert np.array_equal(obj_bucket.arr,np.array([0.05,0.09,0.1,0.15,0.2,0.2,0.23,0.3,0.3,0.3,0.4,0.5,0.5,0.6,0.7,0.8,0.9]))
