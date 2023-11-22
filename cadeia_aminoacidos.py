cadeia_aminoacido = str(input("Com base nas trincas abaixo:\nUUU|CUU|UUA|AAG|UCU|UAU|CAA\nDigite uma cadeia de aminoácidos: "))

rna_trinca = {
    'UUU' : 'Phe',
    'CUU' : 'Leu',
    'UUA' : 'Leu',
    'AAG' : 'Lisina',
    'UCU' : 'Ser',
    'UAU' : 'Tyr',
    'CAA' : 'Gln'
}

list_trio = []
list_trincas = []

limite_inicio = 0
incremento_pos_inicio = 3 
incremento_loop = 3

while incremento_loop != 0:
    list_trio = cadeia_aminoacido[limite_inicio:incremento_pos_inicio:]
    list_trincas.append(list_trio)
    limite_inicio +=3
    incremento_pos_inicio+=3
    incremento_loop -=1

valores = []
for rna in rna_trinca:    
    valores.append(rna_trinca.get(f"{rna}"))
 
chaves = []
for chave in rna_trinca.keys():
    chaves.append(chave)
    
traducao = []
for trinca in list_trincas:
    if trinca in chaves:
        traducao.append(rna_trinca.get(trinca))

for trinca_traduzida in traducao:
    print(trinca_traduzida, end ="")