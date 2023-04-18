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
      return 5*T(n/4,C)+n

#n es potencia de 4

def f(n,C):
   return C*n**math.log(5,4)+4*n*(n**math.log(5/4,4)-1)

cte = [1,2,3,4,5]

lst = [4**n for n in range(0,10)]

for C in cte:
   for n in lst:
      print("cte=",C,"n=",n,"val:",T(n,C),f(n,C))
