"""
Carlos A Delgado
29 de Agosto de 2023
"""

def R1(n):
    if n==1:
        return 8
    else: 
        return 2*R1(n/2)+n

lst = [2,4,8,16,32,64,128,256,512,1024,2048,4096]

for i in lst:
    print(R1(i))

def R2(n):
    if n==1:
        return 9
    else:
        return 5*R2(n/3)+2*n

lst = [3,9,27,81,243,729,2187,6561,19683,59049,177147,531441]

for i in lst:
    print(i,R2(i))
