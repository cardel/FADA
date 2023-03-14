"""
Carlos A Delgado
14 de Marzo 2023
Ejemplo de sumatoria sencilla del taller de conocimientos previos
"""

def f_sum():
  suma = 0
  for i in range(100,45001):
    suma += 2*i + 8
  
  return suma

def sol_sum():
  return 45000*45001 - 99*100 + 8*45000 -8*99

print(f_sum(),sol_sum())
