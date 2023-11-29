"""
Problema de la mochila
"""
import numpy as np
def mochila(M,w,b):
    """
    M: capacidad de la mochila
    w: lista de pesos
    b: lista de beneficios
    """
    n = len(w) # número de objetos
    bmax = np.zeros((M+1,n+1))# matriz de beneficios máximos

    for i in range(1,M+1): #Capacidad
        for j in range(1,n+1): #Numero de objetos 
            if i - w[j-1] >= 0:
                bmax[i,j] = max(bmax[i,j-1],bmax[i-w[j-1],j-1] + b[j-1])
            else:
                bmax[i,j] = bmax[i,j-1] #No lo meto porque no cabe
    
    #Calcular la solución
    i = M
    j = n
    sal = np.zeros(n)
    while i>0 and j>0:
        if i - w[j-1] >= 0: #Si cabe
            if bmax[i,j-1] > bmax[i-w[j-1],j-1] + b[j-1]:
                sal[j-1] = 0 #No lo llevo
            else:
                sal[j-1] = 1
                i -= w[j-1] #Le quito la capcidad
        else:
            sal[j-1] = 0 #No lo llevo porque no cabe
        
        j = j-1 #quito un elemento
    return bmax,sal


if __name__ == "__main__":
    M = 20
    b = [3,2,1,4]
    w = [7,5,6,8]
    sol = mochila(M,w,b)
    print(sol)


    M = 9
    b = [10,6,8]
    w = [7,4,5]
    sol = mochila(M,w,b)
    print(sol)
