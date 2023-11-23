"""
Implementación de la busqueda binaria
Carlos Andres Delgado
Fecha: 23/11/2023
"""

def binary_search(A,x,p,r):
    """
    A: Lista ordenada de forma ascendente
    x: Valor a buscar
    """
    if p<r:
        q = (p+r)//2
        if A[q] == x:    
            return True
        elif A[q] > x: #Busco a la izquierda
            return binary_search(A,x,p,q)
        elif A[q] < x: #Busco a la derecha
            return binary_search(A,x,q+1,r)
        
    else:
        return False

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,10,11]
    x = 5
    print(binary_search(a,x,0,len(a)))
    print(binary_search(a,9,0,len(a)))
    print(binary_search(a,13,0,len(a)))
    print(binary_search(a,11,0,len(a)))
    print(binary_search(a,1,0,len(a)))
    print(binary_search(a,0,0,len(a)))
