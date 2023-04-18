"""
Solución R.R 
T(n) = T(n/3)+T(2n/3)+n
Carlos A Delgado
18 de Abril de 2023
"""
import matplotlib.pyplot as plt

nter = [100/3**i for i in range(0,10)]
ndoster = [100*(2/3)**i for i in range(0,10)]

plt.figure(dpi=150)
plt.plot(nter,"b.",label=r"$\frac{n}{3^i}$")
plt.plot(ndoster,"r-",label=r"$\frac{2}{3}^i*n$")
plt.legend()
plt.show()


