"""
Carlos A Delgado
30 de Mayo de 2023
Ejemplo de implementación de un arbol binario de búsqueda
"""

class ArbolBB:
  def __init__(self,key,left,right) -> None:
    self.key = key
    self.left = left
    self.right = right
    self.father = None

  def set_father(self,father):
    self.father = father
    if self.left is not None:
      self.left.set_father(self)
    if self.right is not None:
      self.right.set_father(self)


  def flat(self,lst):
    sal = []
    for e in lst:
      if type(e) is list:
        f = self.flat(e)
        for fi in f:
          sal.append(fi)
      else:
        sal.append(e)
    return sal

  def innorder_search(self):
    salida = []
    if self.left is not None:
      salida.append(self.left.innorder_search())

    salida.append(self.key)
    
    if self.right is not None:
      salida.append(self.right.innorder_search())


    return self.flat(salida)
  

  def __format__(self) -> str:
    if self.left is None and self.right is None:
      return str(self.key)
    sal = "(" + str(self.key)
    if self.left is not None:
      sal += " " +self.left.__format__()
    else:
      sal += " "
    if self.right is not None:
      sal += " " + self.right.__format__()
    else:
      sal += " "
    sal += ")"
    return sal.strip(" ")


  def minimum(self):
    if self.left is None:
      return self.key
    else:
      return self.left.minimum()
    
  def maximum(self):
    if self.right is None:
      return self.key
    else:
      return self.right.maximum()
    
  def search(self,x):
    if x == self.key:
      return self
    if x < self.key and self.left is not None:
      return self.left.search(x)
    elif self.right is not None:
      return self.right.search(x)
    else:
      return None
    
  def successor(self, val):
    x = self.search(val)
    if x.right is not None:
      return x.right.minimum()
    
    y = x.father
    while y is not None and x == y.right:
      x = y
      y = y.father
    
    return y.key
    
      
  def insertion(self,x):
    if x < self.key:
      if self.left is not None:
        self.left.insertion(x)
      else:
        self.left = ArbolBB(x,None,None)
    else:
      if self.right is not None:
        self.right.insertion(x)
      else:
        self.right = ArbolBB(x,None,None)

  def elimitation(self,val):
    z = self.search(val)
    if z is not None:
      #Evaluar los casos
      if z.left is None and z.right is None:
        father = z.father
        if z == father.left:
          father.left = None
        else:
          father.right = None
        
        z.father = None
      elif z.left is None:
        father = z.father
        if z == father.left:
          father.left = z.right
        else:
          father.right = z.right
        z.right.father = father
      elif z.right is None:
        father = z.father
        if z == father.left:
          father.left = z.left
        else:
          father.right = z.left
        z.right.father = father
      else:
        succ = z.search(z.successor(val))
        self.elimitation(succ.key)
        z.key = succ.key        
    else:
      raise AttributeError
