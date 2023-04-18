"""
Solución R.R 2T(n/2)+1, T(1)=O(1)
Carlos A Delgado
18 de Abril de 2023
"""
import math
def T(n,C):
    if n==1:
      return C
    else:
      return 2*T(n/2,C)+1

#n es potencia de 2

def f(n,C):
   return (C+1)*n-1

cte = [1,2,3,4,5]

lst = [2**n for n in range(0,10)]

for C in cte:
   for n in lst:
      print("cte=",C,"n=",n,"val:",T(n,C),f(n,C))
