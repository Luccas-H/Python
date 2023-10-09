n = int(input('Digite um número inteiro e positivo: '))
t= 1
e = 0

for i in range(n):
    i = i  + 1 
    e= 1 + (1/i*t) + e 
    t = i*t

print(t)
print(e)