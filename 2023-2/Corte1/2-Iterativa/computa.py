"""
Carlos A Delgado
05 de Sep
Ejemplo del algoritmo computa de las diapositivas
"""
def computa(A,B):
    res = 0
    i = 1
    while i <= B:
        print(f"Si ({i},{res}) res = {(i-1)*A}")
        res += A
        i += 1

computa(10,5)
