#Asuma n par
def algoritmo1(n):
	i = 0
	res = 0
	while i<n:
		#print(i,res)
		j = 0
		u = 1
		while j <= n:
			print(j,u)
			j+=1
			u += 2*j
		i+=1
		res+=u
	return res

def algoritmo2(n):
	i = 1
	res = 1
	while i<= n:
		print(i,res)
		j=n
		s=3
		while j >= 0:
			print(j,s)
			s+=2*j
			j-=1
		res += 2*s
		i+=1
	return res


algoritmo1(10)
#algoritmo2(15)
