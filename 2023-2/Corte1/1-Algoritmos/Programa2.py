"""
Carlos A Delgado
05 de Sep de 2023
Programa2 de las diapositivas
"""
def programa2(n):
    cnt = 1
    s = 0
    i = 1
    cnt+=1
    while i<= n:
        cnt+=1 #Entrada primer while
        t = 0
        cnt+=1
        j = 1
        cnt+=1
        while j <= i:
            cnt+=1 #Entrada segundo while
            t = t +1
            cnt+=1
            j = j + 1
            cnt+=1
        cnt+=1 #Salida segundo while
        s = s + t
        cnt+=1
        i = i + 1
        cnt+=1
    cnt+=1 #Salida primer while
    return cnt

def f2(n):
    return 3+6*n+3*n*(n+1)/2


lst = [x for x in range(0,20)]

for n in lst:
    print(n, programa2(n), f2(n))
    

