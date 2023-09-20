ask = str(input("Digite um número romano: "))
rom = [1000,500,100,50,10,5,1]
let = ['M', 'D', 'C', 'L', 'X','V', 'I']
deco = []
union = []
count = []

for sim in ask: 
    deco.append(sim)


for i in range(len(let)):
    tupla = (let[i], rom[i])
    union.append(tupla)


for i in range(len(deco)):
    valor = 0 
    for j in range(len(union)):
        if deco[i] == union[j][0]:
            valor = valor + union[j][1]
            count.append(valor)

soma = 0 

for z in range(len(union) -1,-1,-1):
    for n in range(len(count)):
        if count[n] == union[z][1]:
            soma = count[n] - soma
        
            
loop = 0 

for d in range(len(count)):
    loop = count[d] + loop 
    
    
    
    


print(loop)
print(union)
print(deco)
print(valor)
print(soma)
print(count)
