"""
Carlos A Delgado S
21 de Marzo de 2023
Ejemplo de programa5 (incompleto) de las diapositivas
"""
import math
def programa5(n):
  i = 1
  cnt = 0
  while i<=n:
    cnt+=1 #Entrada
    i*=2
  cnt+=1 #salida
  return cnt

def f(n):
  return math.log2(n) + 2

lista = [2**x for x in range(0,20)]

for n in lista:
  print(n,programa5(n),f(n))
