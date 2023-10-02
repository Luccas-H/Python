list_dimensoes = []

n = 0
while n!=2:
    t = float(input('Digite a dimensão: '))
    list_dimensoes.append(t)
    n = n + 1 
area_comodo = list_dimensoes[0]*list_dimensoes[1]
potencia_total = area_comodo*18
print('A área total é de {} e a potência necessaria é de {} '.format(area_comodo,potencia_total))