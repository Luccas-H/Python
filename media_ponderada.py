lista_notas = []
lista_pesos = []
lista_resu = []
i = 0 

while i!=3:
    n = float(input("Digite uma nota: "))
    p = int(input("Digite o peso dessa nota: "))
    lista_notas.append(n)
    lista_pesos.append(p)
    i =  i + 1 

for i in range(len(lista_notas)):
    tupla = (lista_notas[i], lista_pesos[i])
    lista_resu.append(tupla)

m = 0
for k in range(len(lista_resu)):
    m = lista_resu[k][0]*lista_resu[k][1] + m        

print(m/sum(lista_pesos)) 

 