"""
Multiplicacion de matrices programación dinámica
"""
import numpy as np
def mult_matrices_dinamica(p):
    c = np.zeros((len(p), len(p))) #Costos
    indices = np.zeros((len(p), len(p))) #Indices
    #Rellenar casos base i == j diagonal principal
    for i in range(len(p)-1):
        c[i][i] = 0

    #Rellenar casos base i < j diagonal superior
    for r in range(1,len(p)):
        for i in range(len(p)-r):
            j = i+r 
            minK = i
            costK = c[i][minK] + c[minK+1][j] + p[i-1]*p[minK]*p[j]
            for k in range(i+1,j):
                costKi = c[i][k] + c[k+1][j] + p[i-1]*p[k]*p[j] #Costo de multiplicar las matrices de i a k y de k+1 a j
                if costKi < costK:
                    minK = k
                    costK = costKi
            c[i][j] = costK
            indices[i][j] = minK

    return c[1:,1:], indices[1:,1:]

if __name__ == "__main__":
    p = [30,35,15,5,10,20,25]
    c, indices = mult_matrices_dinamica(p)
    print(c)
    print(indices)
