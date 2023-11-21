"""
Problema de la subsecuencia común más larga con programación dinámica.
"""
import numpy as np
def lsc(a:str, b:str) -> int:
    """
    Calcula la longitud de la subsecuencia común más larga entre dos cadenas.
    """
    n = len(a)
    m = len(b)
    #Tabla de costos de tamaño n+1 x m+1
    c = np.zeros((n+1,m+1))
    #Inicialización de la tabla
    for i in range(n+1):
        c[i,0] = 0
    for j in range(m+1):
        c[0,j] = 0
    #Calcula de la tabla
    """
    c[i,j] = 0 si j = 0 o i = 0 #Aqui comparamos contra la cadena vacía
    c[i,j] = c[i-1,j-1] + 1 si a[i] = b[j]
    c[i,j] = max(c[i-1,j], c[i,j-1]) si a[i] != b[j]
    """
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                c[i,j] = c[i-1,j-1] + 1
            else:
                c[i,j] = max(c[i-1,j], c[i,j-1])
    cadena = ""
    i = n
    j = m
    while True:
        if i == 0 or j == 0: #Terminé
            break
        if a[i - 1] == b[j - 1]:
            cadena = a[i - 1] + cadena
            i -= 1
            j -= 1
        elif c[i,j-1] >= c[i-1,j]:
            j -= 1 #Si el arriba es mejor me voy a arriba
        else:
            i -= 1 #Me voy a la izquierda
            
    return c, cadena

if __name__ == "__main__":
    a = "AFAAAB"
    b = "AAABAFA"
    c = lsc(a,b)
    print(c)
    
    d = "I like racecars that go fast"
    d = d.replace(" ","").lower()
    print(d)
    print(d[-1::-1])
    print(lsc(d,d[-1::-1]))



