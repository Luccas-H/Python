nome = input('Digite uma palavra:')
lista_nome_separado = []
possi = 1

for i in nome:
    lista_nome_separado.append(i)

n = len(lista_nome_separado)

for k in range(len(lista_nome_separado)):
    possi = (n-k)*possi
                
print(possi)

