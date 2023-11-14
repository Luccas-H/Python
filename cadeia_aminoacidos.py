cadeia_aminoacido = str(input("Com base nas trincas abaixo:\nUUU|CUU|UUA|AAG|UCU|UAU|CAA\nDigite uma cadeia de aminoácidos: "))

rna_trinca = {
    'UUU' : 'Phe',
    'CUU' : 'Leu',
    'UUA' : 'Leucina',
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

def get_key (val):
    for key, value in rna_trinca.items():
        if val == value:
            return key    

chaves = []
for valor in valores:
    chaves.append(get_key(valor))
    

traducao = []
for trinca in list_trincas:
    if trinca in chaves:
        traducao.append(rna_trinca.get(trinca))

for trinca_traduzida in traducao:
    print(f"{trinca_traduzida}", end ="")

