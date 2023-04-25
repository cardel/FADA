"""
Este programa nos ayuda a comprender las condiciones del metodo del maestro

T(n) = 3T(n/4)+log(n)

"""
import matplotlib.pyplot as plt
import math
import numpy as np

def caso1():
  n = [x for x in range(1,1000)]
  logn = [x*math.log2(x) for x in n]
  n075 = np.array([x**0.75 for x in n])
  plt.figure(dpi=150)
  plt.plot(n,logn,"r-",label=r"$log(n)$")
  plt.plot(n,n075,"b-",label=r"$n^{0.75}$")
  plt.plot(n,2*n075,"c-",label=r"$2*n^{0.75}$")
  plt.plot(n,4*n075,"y-",label=r"$4*n^{0.75}$")
  plt.plot(n,20*n075,"g-",label=r"$20*n^{0.75}$")
  plt.legend()
  plt.show()

caso1()
