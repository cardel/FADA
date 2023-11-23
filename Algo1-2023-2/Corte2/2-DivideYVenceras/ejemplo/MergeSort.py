"""
Implementación del algoritmo MergeSort
23/11/2023
"""

class MergeSort:
    def merge(self,arr,p,q,r):
        left = arr[p:q+1]
        right = arr[q+1:r+1]
        left.append(float("inf"))
        right.append(float("inf"))
        i = 0
        j = 0
        for k in range(p,r+1):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
    
    def sort(self,arr,p,r):
        if p<r:
            q = (p+r)//2
            self.sort(arr,p,q)
            self.sort(arr,q+1,r)
            self.merge(arr,p,q,r)



if __name__ == "__main__":
    obj = MergeSort()
    arr = [2,1,4,6,3,2,12,231,31231,313,13123,13,12]
    obj.sort(arr,0,len(arr)-1)
    print(arr)

