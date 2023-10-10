import random 

pontos_total_cada = []
media_cada = []
list_pontos = []
maximo = 0 
minimo = 0

n = 0 
while n !=45:
    p = random.randint(1,15)
    list_pontos.append(p)
    n +=1 
k = 15

splited = []
len_l = len(list_pontos)
for i in range(k):
    start = int(i*len_l/k)
    end = int((i+1)*len_l/k)
    splited.append(list_pontos[start:end])


for s in range(len(splited)):
    r = splited[s][0] + splited[s][1] + splited[s][2]  
    pontos_total_cada.append(r)  

print('Segue a baixo os valores de cada funcionário do 1 ao 15:\n')

for j in range(len(pontos_total_cada)):
        print('funcionário  -> {}'.format(pontos_total_cada[j]))

for m in range(len(splited)):
    r = (splited[m][0] + splited[m][1] + splited[m][2])/3  
    media_cada.append(r)  

print('Segue a baixo as médias de cada funcionário do 1 ao 15:\n')

for j in range(len(media_cada)):
        print('funcionário  -> {:.3}'.format(media_cada[j]))

maximo = max(pontos_total_cada)
posicao_maximo = pontos_total_cada.index(max(pontos_total_cada))
print("\nA maior pontuação atingida foi pelo funcionário {} com um total de {} pontos".format(posicao_maximo + 1,maximo))