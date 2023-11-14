"""
Implementación de algoritmo Radix Sort

"""
import numpy as np


def radix_sort(A):
    #A es una lista de enteros con d digitos
    d = len(str(max(A)))
    for i in range(d):
        #Ordenar por el digito i (de derecha a izquierda)
        factor = 10**i
        An = (A // factor) % 10 
        indices = np.argsort(An)
        A = A[indices]
    return A

if __name__ == '__main__':
    A = np.array([123, 450, 678, 190, 120, 345, 67, 89, 10])
    B = radix_sort(A)
    print(B)

    print(radix_sort(np.array([23023,23210,45000,67089,10011,1,2,3,4,5,6,7,8,9,10,11,12,13,14])))
