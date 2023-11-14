"""
Implementación del Bucket Sort
"""

def bucket_sort(A):
    #10 buckets 
    n = len(A)
    buckets = [[] for i in range(10)]

    for n in A:
        bactual = buckets[int(n*10)]
        ind = 0
        #Buscamos donde debemos insertar el indice
        while ind < len(bactual) and bactual[ind] < n:
            ind += 1
        buckets[int(n*10)].insert(ind, n)
    #Generamos la salida
    sal = []
    for b in buckets:
        sal += b

    return sal 

if __name__ == "__main__":
    A = [0.1,0.3,0.2,0.4,0.6,0.5,0.7,0.9,0.8,0.05,0.58,0.12,0.55,0.39,0.37]
    print(bucket_sort(A))
    
