def computa(a,b)
  res = 0
  i = 1
  while i<=b
    i=i+1
    res= res+a
    print(res," ",(i-1)*a,"\n") #Invariante
  end
end

computa(100,20)
