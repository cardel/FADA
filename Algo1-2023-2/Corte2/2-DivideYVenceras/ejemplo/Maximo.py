"""
Carlos A Delgado Saavedra
Implementación de algoritmo de Maximo
23/11/2023
"""
import numpy as np
import time
class Maximo:

    def ligar(self,arr,p,q,r):
        if arr[p] < arr[q+1]:
            arr[p],arr[q+1] = arr[q+1],arr[p]

    def get_maximo(self,arr,p,r):
        if p<r:
            q=(p+r)//2
            self.get_maximo(arr,p,q)
            self.get_maximo(arr,q+1,r)
            self.ligar(arr,p,q,r)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(arr)
    Maximo().get_maximo(arr,0,len(arr)-1)
    print(arr)
    t1 = time.time()
    arr2 = np.random.randint(0,10000,100).tolist()
    print(arr2)
    Maximo().get_maximo(arr2,0,len(arr2)-1)
    print(arr2)
    print("El tiempo de ejecució es de: ",time.time()-t1," segundos")

    


