"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Algoritmo para encontrar el máximo de un arreglo mediante divide y vencerás
"""

import numpy as np
class Maximum:
  def __init__(self,array) -> None:
    self.array = array

  def getMaximum(self,p,r):
    if p==r:
      return self.array[p]
    else:
      q = (p+r)//2
      x = self.getMaximum(p,q)
      y = self.getMaximum(q+1,r)
      return max(x,y)
    
