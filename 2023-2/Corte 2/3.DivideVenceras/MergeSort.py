"""
Implementación del algoritmo Mergesort
"""

def Merge(A,p,q,r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

def Mergesort(A,p,r):
    if p < r:
        q = (p+r)//2
        Mergesort(A,p,q)
        Mergesort(A,q+1,r)
        Merge(A,p,q,r)


if __name__ == "__main__":
    A = [5,2,4,7,1,3,2,6]
    print(A)
    Mergesort(A,0,len(A)-1)
    print(A)
