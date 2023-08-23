
def sumatoria1(n):
	suma = 0
	for i in range(-40,2*n+1):
		for j in range(40,n**2+1):
			suma+=2*i*j+8*j
	return suma

def sumatoria2(n):
	suma = 0
	for i in range(1,2*n+41+1):
		for j in range(1,n**2-39+1):
			suma+=2*(i-41)*(j+39)
			suma+=8*(j+39)
	return suma

for n in range(10,30):
	print(n,sumatoria1(n), sumatoria2(n))

