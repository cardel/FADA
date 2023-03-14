"""
Carlos A Delgado
14 de Marzo de 2023
Ejemplo de sumatoria doble del taller de conocimientos previos
"""
def f_sum(n):
  suma = 0
  for i in range(-40,2*n+1):
    for j in range(40,n**2+1):
      suma+= 2*i*j + 8*j
  return suma

def sol_sum(n):
  x = (n**2*(n**2+1))/2 - 39*20
  parte1 = -40*41+2*n*(2*n + 1)
  parte2 = 8*(2*n + 41)
  return x*(parte1 + parte2) 


for n in [10,20,40,60,80,100]:
  print(n,f_sum(n),sol_sum(n))
