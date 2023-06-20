"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Descripcion: Implementacion de la funcion de fibunnacci con memorizacion
"""
import numpy as np
class Fibunnacci:
  def __init__(self):
    self.mem = np.zeros(1000)

  def fib(self, n):
    if n == 0 or n == 1:
      return n
    if self.mem[n] != 0:
      return self.mem[n]
    self.mem[n] = self.fib(n-1) + self.fib(n-2)
    return self.mem[n]
