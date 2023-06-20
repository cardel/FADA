"""
Autor: Carlos A Delgado
Fecha: 2023-06-20
Descripción: Comparación de rendimiento entre la función de fibunnacci clásica y la función de fibunnacci con memorización
"""

import time

from fibunnacci import Fibunnacci_clasico
from fibunnacci_memorizacion import Fibunnacci

def main():
  fib = Fibunnacci()
  fib_clasico = Fibunnacci_clasico()

  print("Fibunnacci con memorización")
  start_time = time.time()
  print(fib.fib(40))
  print("--- %s seconds ---" % (time.time() - start_time))

  print("Fibunnacci clásico")
  start_time = time.time()
  print(fib_clasico.fib(40))
  print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
  main()
