"""
Implementación del monticulo binario
Autor: Carlos Delgado
Fecha: 31-Oct-2023
"""


class Monticulo:
    def __init__(self, size):
        self.lista = []
        self.size = size

    def padre(self, i):
        return i // 2

    def izq(self, i):
        return 2 * i

    def der(self, i):
        return 2 * i + 1

    def heapify(self, i):
        l = self.izq(i)
        r = self.der(i)
        if l <= self.size and r <= self.size:
            vl = self.lista[l - 1]  # Valor izquierda
            vr = self.lista[r - 1]  # Valor derecha
            ind_mayor = l if vl > vr else r
            if self.lista[ind_mayor - 1] > self.lista[i - 1]:
                self.lista[ind_mayor - 1], self.lista[i - 1] = self.lista[i - 1], self.lista[ind_mayor - 1]
                self.heapify(ind_mayor)
        elif l <= self.size:
            if self.lista[l - 1] > self.lista[i - 1]:  # Cambiamos por el valor de la izquierda
                self.lista[l - 1], self.lista[i - 1] = self.lista[i - 1], self.lista[l - 1]
                self.heapify(l)



    def build_heap(self): 
        for i in range(self.size // 2, 0, -1):
            self.heapify(i)

    
    def heap_sort(self):
        self.build_heap()
        for i in range(self.size, 1, -1):
            self.lista[0], self.lista[i - 1] = self.lista[i - 1], self.lista[0]
            self.size -= 1
            self.heapify(1)
