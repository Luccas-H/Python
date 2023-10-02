list_notas = []
list_pesos = [2,3,5]
list_conjunto = []

n = 0
while n!=3:
    p = float(input("Digite uma nota: "))
    list_notas.append(p)
    n += 1

for k in range(len(list_notas)):
    tupla = (list_notas[k], list_pesos[k])
    list_conjunto.append(tupla)



media_ponderada = 0
for i in range(len(list_conjunto)):
    media_ponderada = list_conjunto[i][0]*list_conjunto[i][1] + media_ponderada

media_ponderada = media_ponderada/sum(list_pesos)

if 8.0<=media_ponderada<=10.0:
    print('A média é {} e o conceito é A'.format(media_ponderada))
if 7.0<=media_ponderada<8.0:
    print('A média é {} e o conceito é B'.format(media_ponderada))
if 6.0<=media_ponderada<7.0:
    print('A média é {} e o conceito é C'.format(media_ponderada))
if 5.0<=media_ponderada<6.0:
    print('A média é {} e o conceito é D'.format(media_ponderada))
elif 0<=media_ponderada<5.0:
    print('A média é {} e o conceito é E'.format(media_ponderada))
