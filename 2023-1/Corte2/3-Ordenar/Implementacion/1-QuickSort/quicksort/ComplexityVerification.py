"""
Autor: Carlos A Delgado
Fecha: 13/06/2023

Verificación de complejidad del algoritmo Quicksort en sus diferentes versiones
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import sys

sys.setrecursionlimit(100000000)

from QuickSort import QuickSort

def verify_complexity_quicksort():
  time_quicksort = []
  time_quicksort_randomized = []
  sizes = [1000,2000,5000,10000]
  for n in sizes:
    arr = np.random.randint(0,100000,n)

    arr1 = arr.copy()
    arr1.sort()
    objQuickSort = QuickSort(arr1)
    start = time.time()
    objQuickSort.quicksort(0, arr1.shape[0]-1)
    end = time.time()
    time_quicksort.append(end-start)

    
    arr2 = arr.copy()
    arr2.sort()
    objQuickSort = QuickSort(arr2)
    start2 = time.time()
    objQuickSort.quicksort(0, arr2.shape[0]-1)
    end2 = time.time()
    time_quicksort_randomized.append(end2-start2)

    print("Size ",n)

  plt.figure(dpi=200)
  plt.plot(sizes, time_quicksort, label="Quicksort")
  plt.plot(sizes, time_quicksort_randomized, label="Quicksort Randomized")
  plt.legend()
  plt.show()

verify_complexity_quicksort()
