"""
Implementación del algoritmo counting Sort
"""

def counting_sort(A):
    """
    Ordena los elementos de A en orden ascendente
    """
    k = max(A)
    C = [0] * k
    B = [0] * len(A)
    #Vamos a llenar el arreglo C
    for i in range(0, len(A)):
        C[A[i] - 1] += 1 #Va a contar los elementos que hay
    #Actualizamos
    for i in range(1, k):
        C[i] += C[i - 1]

    #Generamos al arreglo B
    for i in range(len(A)-1, -1,-1):
        B[C[A[i] - 1] - 1] = A[i]
        C[A[i] - 1] -= 1

    return B

if __name__ == "__main__":
    A = [5, 2, 4, 6, 1, 3, 1, 4, 3, 4]
    B = counting_sort(A)
    print(B)
