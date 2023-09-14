"""
Carlos A Delgado
14 de Septiembre de 2023
"""

def algoritmo1(n):
    i = 0
    s = 3
    print(f"s={s},inv={3+0.5*i*(8*n+12)}")
    while i <= n:

        print(f"inv={3+0.5*i*(8*n+12)},s={s}")
        j = 0
        p = 4
        while j<= 2*n:
            p+=2
            j+=1
        s+=2*p
        i+=2
    print(f"inv={3+0.5*i*(8*n+12)},s={s}")

algoritmo1(12)
