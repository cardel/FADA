"""
Autor: Carlos A Delgado
Fecha: 20-06-2023
Implementación del algoritmo de la subsecuencia más larga
"""

import numpy as np

class lcs:
  def __init__(self) -> None:
    self.c = None

  def cost_lcs(self, x: str, y: str) -> int:
    """
    Retorna la longitud de la subsecuencia más larga entre dos cadenas
    """
    c = np.zeros((len(x)+1, len(y)+1))
    for i in range(1, len(x)+1):
      for j in range(1, len(y)+1):
        if x[i-1] == y[j-1]:
          c[i,j] = c[i-1,j-1] + 1
        else:
          c[i,j] = max(c[i-1,j], c[i,j-1])

    self.c = c
    return c[len(x), len(y)]
