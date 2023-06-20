"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Implementacion de la funcion de fibunnacci clásica
"""

class Fibunnacci_clasico:
  def fib(self, n):
    if n == 0 or n == 1:
      return n
    return self.fib(n-1) + self.fib(n-2)
