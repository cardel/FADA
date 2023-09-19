"""
Carlos A Delgado
19 de Septiembre 2023
Analisis de la R.R T(n) = T(n/3)+T(2n/3)+n
"""
import matplotlib.pyplot as plt
import math

def T(n):
    if n<=1:
        return 1
    else:
        return T(n/3)+T(2*n/3)+n

def Omega(c,n):
    return c*n*math.log(n,3)

def O(c,n):
    return c*n**1.7

lst = [3**x for x in range(0,11)]

plt.figure(dpi=300)
plt.plot(lst,[T(x) for x in lst],label='T(n)',color='black')
plt.plot(lst,[Omega(1,x) for x in lst],label=r'$\Omega(nlog_n(n))$',color='red')
plt.plot(lst,[O(1,x) for x in lst],label=r'$O(n^{1.7})$',color='blue')
plt.yscale('log')
plt.legend()
plt.show()


