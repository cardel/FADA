"""
Algoritmo de la busqueda binaria
"""

def busqueda_binaria(A,p,r,x):
    if p>r:
        return False
    else:
        q = (p+r)//2
        if A[q] == x:
            return True
        elif A[q] > x:
            return busqueda_binaria(A,p,q-1,x)
        else:
            return busqueda_binaria(A,q+1,r,x)


if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9,10]
    print(busqueda_binaria(A,0,len(A)-1,5)) #True
    print(busqueda_binaria(A,0,len(A)-1,11)) #False
