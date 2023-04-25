"""
Este programa nos ayuda a comprender las condiciones del metodo del maestro

T(n) = 2T(n/2)+1
T(n) = O(n)
"""

def T(n):
  if n==1:
    return 1
  else:
    return 2*T(n/2)+1
  
def f(n):
  return 10*n+1

n = [2**x for x in range(0,100)]

for ni in n:
  print(ni,T(ni),f(ni),T(ni)<=f(ni))
