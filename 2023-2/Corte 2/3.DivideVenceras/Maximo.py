"""
Maximo de una lista por divide y vencerás
"""

def conquista(A,p,q,r):
    if A[p] <= A[q+1]:
        A[p],A[q+1] = A[q+1],A[p]


def maximo(A,p,r):
    if p<r:
        q = (p+r)//2
        maximo(A,p,q)
        maximo(A,q+1,r) 
        conquista(A,p,q,r)


if __name__ == "__main__":
    A = [5,2,4,7,1,3,2,6]
    print(A)
    maximo(A,0,len(A)-1)
    print(A)
    print("Maximo de la lista: ",A[0])


