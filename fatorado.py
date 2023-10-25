n = int(input('Digite um número inteiro e positivo: '))
t= 1
e = 0

for i in range(1,n+1):
    t = i*t
    e= (1/t) + e 


print("O total da soma é {:.5}".format(e))