"""
Carlos A Delgado
21 de Marzo de 2023
Ejemplo programa4 de las diapositivas
"""

def programa4(n):
  i = 1
  cnt = 1 #i=1
  while i <= n:
      cnt+=1 #Entrada
      k = i
      cnt+=1 #k = i
      while k<=n:
         cnt+=1 #Entrada
         k+=2
         cnt+=1 #k+=2
      cnt+=1 #Salida
      k = 1
      cnt+=1 #k=1
      while k<=i:
        cnt +=1 #Entrada
        k=k+1
        cnt+=1 #k=k+1
      cnt+=1 #Salida      
      i+=2
      cnt+=1 #i+=2
  cnt+=1 #Salida
  
  return cnt

def formula(n):
   x =(n+1)/2
   lin1 = 1
   lin2 = (n+3)/2
   lin3 = x
   lin4 = x*((n+3)/2) - x*(x+1)/2+x
   lin5 = x*x - x*(x+1)/2+x
   lin6 = x
   lin7 = x*(x+1)
   lin8 = x*(x+1) - x
   lin9 = x
   return lin1 + lin2 + lin3 + lin4 + lin5 + lin6 + lin7 + lin8 + lin9
   
lista = [21,33,41,91,101,201]

for n in lista:
   print(n,programa4(n),formula(n))

