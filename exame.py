

notas = []

n = 0 
while n!=12:
    p = float(input("Digite cada nota em ordem de aluno: "))
    notas.append(p)
    n += 1

len_l = len(notas)
k = 6 
notas_separadas = []

for i in range(k):
    start = int(i*len_l/k)
    end = int((i+1)*len_l/k)
    notas_separadas.append(notas[start:end])


media = 0 
media_sala = 0 

for i in range(len(notas_separadas)):
    media_sala = notas_separadas[i][0] + notas_separadas[i][1] + media_sala

print("A média da sala é {:.3}".format(media_sala/6))

aprovados = []
reprovados = []
exame = []

for i in range(len(notas_separadas)):
    media = notas_separadas[i][0] + notas_separadas[i][1] 
    if media/2 >= 7:
        aprovados.append("Um aprovado")
    if media/2 <3:
        reprovados.append("Um reprovado")
    elif media/2 < 7 or media/2>3:
        exame.append("Tem direito")





print("O número de alunos aprovados é {}".format(len(aprovados)))
print("O número de alunos reprovados é {}".format(len(reprovados)))
print("O número com direito a exame é {}".format(len(exame)))


