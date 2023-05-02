"""
Comprobación inducción recurrencia
T(n) = 4T(n/2)+n^2
T(n) = Thetha(n^2log(n))
"""
import math
import matplotlib.pyplot as plt

def O(n):
    return 100*n**2*math.log2(n/2)+n**2

def Omega(n):
    return n**2*math.log2(n/2)+n**2

def T(n):
  if n==1:
     return 10
  else:
     return 4*T(n/2)+n**2
  

n = [2**x for x in range(0,20)]

for ni in n:
   print(ni,T(ni),O(ni), O(ni)>=T(ni), Omega(ni), Omega(ni)<=T(ni))

plt.figure(dpi=150)
plt.plot(n,list(map(lambda x:O(x),n)),"r-",label=r"$O(n^2log(n))$")
plt.plot(n,list(map(lambda x:Omega(x),n)),"b-",label=r"$\Omega(n^2log(n))$")
plt.plot(n,list(map(lambda x:T(x),n)),"g-",label=r"$T(n)$")
plt.legend()
plt.yscale("log")
plt.grid()
plt.show()

