"""
Ejemplo de fibunnacci
autor: Carlos Delgado
"""
import time

def fib(n):
    if n == 0:
        return 1
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)



def fib_memorizacion(n):
    arr = [0]*(n+1)
    arr[0] = 1 
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]

if __name__ == "__main__":
    t1 = time.time()
    n = 20
    print(fib(n),end ="\n")
    print("Tiempo de ejecucion divide y vencerás: ",time.time()-t1)
    t2 = time.time()
    print(fib_memorizacion(n),end ="\n")
    print("Tiempo de ejecucion memorizacion: ",time.time()-t2)
