cadeia_aminoacido = str(input("Digite uma cadeia de cadeia aminoácido: "))
cadeia_separada = []

cadeia_separada.extend(cadeia_aminoacido)

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
    list_trio = cadeia_separada[limite_inicio:incremento_pos_inicio:]
    separador = ' '
    resultado = [separador.join(list_trio)]
    list_trincas.append(resultado)
    limite_inicio +=3
    incremento_pos_inicio+=3
    incremento_loop -=1


def get_key (val):
    for key, value in rna_trinca.items():
        if val == value:
            return key
        

traduzido = ''
len_l = len(list_trincas)
incremento_ = len(list_trincas)
for i in range(len_l):
    for j in rna_trinca:
        valores = rna_trinca.get(f"{j}")
        print(valores)
        print(get_key(valores))
        while incremento_ !=0:
            print(list_trincas[i])
            if list_trincas[i] == get_key(valores):
                traduzido = rna_trinca.get(f"{valores}")
            incremento_ -=1        

print(traduzido)
print(rna_trinca)
print(list_trincas)






# Falta traduzir as trincas / list_trincas[i] ta dando erro precisa verificar