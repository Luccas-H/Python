ask = str(input("Digite um número romano: "))
rom = [1000,500,100,50,10,5,1]
let = ['M', 'D', 'C', 'L', 'X','V', 'I']
deco = []
union = []
count = []
valores = []
repetidos = [0]

s = 0
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

for r in count:
    if r not in valores:
        valores.append(r)
    else:
        repetidos.append(r)

for l in range(len(valores)):
    for h in range(len(repetidos)):
        if repetidos[h] == valores[l]:
            del repetidos[0]
            s = repetidos[0] + valores[l]
        else:
            s = valores[l] - s
           

           
print(s)

#tentar percorrer repetidos duas vezes pra ele pegar mais de uma valor