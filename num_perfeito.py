n = int(input('Digite um numero: '))
d = 1
m = 0 
c = []
soma_divi = 0

while n//d !=0 and m!=1:
    m = n//d
    c.append(m)
    d = d + 1 

del c[0]
soma_divi = sum(c)

if soma_divi == n:
    print("é perfeito")
else:
    print("não é perfeito")

