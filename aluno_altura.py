import random
list_num = [1,2,3,4,5,6,7,8,9,10]
list_alt = []
list_dados = []

n=0
while n!=10:
    p = random.uniform(1.50,2.00)
    list_alt.append(p)
    n += 1
for i in range(len(list_alt)):
    j = [list_num[i],list_alt[i]]
    list_dados.append(j)


maximo = max(list_alt)
minimo = min(list_alt)

posicao_maximo = list_alt.index(max(list_alt))
posicao_minimo = list_alt.index(min(list_alt))


print('O mais alto é o aluno {} com {:.3} e o mais baixo é o aluno {} com {:.3}'.format(posicao_maximo + 1,maximo,posicao_minimo + 1, minimo ))



