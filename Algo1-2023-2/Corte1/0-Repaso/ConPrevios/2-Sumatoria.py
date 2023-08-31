"""
Carlos A Delgado
31 de Agosto de 2023
Sumatoria 2
"""

def suma2(n):
    suma = 0
    for i in range(-40,2*n+1):
        for j in range(40,n**2+1):
            suma += 2*j*i+8*j

    return suma

def fsuma2(n):
    a = (2*n+41)*(2*n+42)/2
    b = (2*n+41)
    return a*n**4+a*n**2-1560*a-37*n**4*b-37*n**2*b+57720*b

#Pruebas de la sumatoria externa
def prueba_sumatoria_externa():
    lst = [x for x in range(0,80,5)]
    for n in lst:
        print(f"Suma {suma2(n)} - {fsuma2(n)} = {suma2(n)-fsuma2(n)}")

#Pruebas de la sumatoria interna
#Sumatoria interna
def sumaI2(n,i):
    suma = 0
    for j in range(40,n**2+1):
        suma += 2*j*i+8*j
    
    return suma

#Sumatoria interna
def fsumaI2(n,i):
    return (2*i+8)*(n**2-39)*(n**2-38)/2+(78*i+312)*(n**2-39)

def prueba_sumatoria_interna():
    lst = [x for x in range(10,90,5)]
    
    for i in range(10,50,3):
        for n in lst:
            print(f"Suma {sumaI2(n,i)} - {fsumaI2(n,i)} = {sumaI2(n,i)-fsumaI2(n,i)}")



prueba_sumatoria_externa()
