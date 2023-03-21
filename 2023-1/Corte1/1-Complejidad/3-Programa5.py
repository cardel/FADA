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

def programa5v2(n):
  i = 1
  cnt = 0
  while i<=n:
    k = i
    while k<=n:
      cnt+=1 #Entrada 
      k=k+2
    cnt+=1 #salida
    i*=2
  return cnt

def fv2(n):
  par1 = (n/2+2)*math.log2(n)
  par2 = -n + 2 + n/2
  return par1+par2

def fv3(n):
  suma = 0
  for c in range(1,int(math.log2(n)+1)):
    suma+=(n/2)+2-2**(c-1)
  return suma+n/2+1

for n in lista:
  print(programa5v2(n),fv2(n),fv3(n))

