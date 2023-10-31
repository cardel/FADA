"""
Implementación algoritmo Quicksort
"""

class QuickSort:
    def __init__(self,lst):
        self.lst = lst

    def partition(self,p,r):
        x = self.lst[p-1] #Pick the first element as pivot
        i = p
        j = r
        while i<j:
            #i busca al que sea mayor o igual que pivot
            while not(self.lst[i-1] >= x):
                i += 1
            #j busca al que sea menor que el pivote
            while not(self.lst[j-1] < x) and j>p: #paro j cuando llega a p
                j -= 1
            if i<j:
                #swap
                self.lst[i-1],self.lst[j-1] = self.lst[j-1],self.lst[i-1]
        return j

    def sort(self, p, r):
        q = self.partition(p,r)
        if p < r:
            self.sort(p,q)
            self.sort(q+1,r)
