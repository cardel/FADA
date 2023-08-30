"""
Carlos A Delgado
Fecha: 29 de Agosto de 2023
"""
def primo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        for i in range(2,n):
            if n%i==0:
                return 0
        return 1

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for elm in lista:
    if primo(elm)==1:
        print(elm)
