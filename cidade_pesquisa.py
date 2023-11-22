cidades_codigos = []
cidades_numeros = []
cidades_numeros_acidentes = []


n = 0
while n!= 3:
    codigo_cidade = str(input('Digite o codigo da cidade: '))
    cidades_codigos.append(codigo_cidade)
    numero_veiculos = int(input('Digite o número de veiculos de passeio: '))
    cidades_numeros.append(numero_veiculos)
    numero_acidentes = int(input('Digite o número de acidentes com vitimas: '))
    cidades_numeros_acidentes.append(numero_acidentes)
    n +=1 


maximo = max(cidades_numeros_acidentes)
minimo = min(cidades_numeros_acidentes)
posicao_acidente_maior = cidades_numeros_acidentes.index(max(cidades_numeros_acidentes))
posicao_acidente_menor = cidades_numeros_acidentes.index(min(cidades_numeros_acidentes))

print('A cidade com mais acidentes é {} com {} acidentes e a menor cidade é {} com {} acidentes'.format(cidades_codigos[posicao_acidente_maior],maximo,cidades_codigos[posicao_acidente_menor],minimo))
print('A media de veiculos nas cidades é de {}'.format(sum(cidades_numeros)/3))