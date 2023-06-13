import math
class heap:
  def __init__(self,size) -> None:
    self.arr = [0]*size
    self.size = size

  def father(self,i):
    return math.floor(i/2)
  
  def left(self,i):
    return 2*i
  
  def right(self,i):
    return 2*i+1

  def heapify(self, pos):
    if pos <= self.size:
      izq = self.arr[self.left(pos)-1] if self.left(pos) <= self.size else float("-inf")
      der = self.arr[self.right(pos)-1] if self.right(pos) <= self.size  else float("-inf")
      
      if izq == float("-inf") and der == float("-inf") or self.arr[pos-1]>izq and self.arr[pos-1]>der:
        return
      
      if izq >= der:
        self.arr[pos-1],self.arr[self.left(pos)-1] = self.arr[self.left(pos)-1],self.arr[pos-1]
        self.heapify(self.left(pos))
      else:
        self.arr[pos-1],self.arr[self.right(pos)-1] = self.arr[self.right(pos)-1],self.arr[pos-1]
        self.heapify(self.right(pos))

  def build_heap(self):
    for i in range(math.floor(self.size/2),0,-1):
      self.heapify(i)

  def heap_sort(self):
    self.build_heap()
    for i in range(self.size,1,-1):
      self.arr[0],self.arr[i-1] = self.arr[i-1],self.arr[0]
      self.size -= 1
      self.heapify(1)
