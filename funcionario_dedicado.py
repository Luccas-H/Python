#Não pronto
import random
funcionarios = [1,2,3,4,5]
pontuacao = []

n = 0
while n!=15:
    p = random.randint(1,10)
    pontuacao.append([p])
    n += 1
for i in pontuacao:
    soma = 1
    if pontuacao.index(i) >= 0 and pontuacao.index(i)<=3:
        soma = i + soma
    if pontuacao.index(i) > 3 and pontuacao.index(i)<=6:
        soma = i + soma
    if pontuacao.index(i) > 6 and pontuacao.index(i)<=9:
        soma = i + soma
    if pontuacao.index(i) > 9 and pontuacao.index(i)<=12:
        soma = i + soma
    if pontuacao.index(i) > 12 and pontuacao.index(i)<=15:
        soma = i + soma
    
    
   
print(soma)








print(pontuacao)