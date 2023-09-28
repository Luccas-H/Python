list_termos = []

x1=0
x2=0

i = 0
while i!=3:
    t = int(input("Digite o termo e seu respectivo sinal:"))
    list_termos.append(t)
    if list_termos[0] == 0:
        print("Erro..")
        break
    i = i + 1 

delta = 0 
delta = (list_termos[1]**2) - 4*list_termos[0]*list_termos[2]

if delta < 0: 
    print("Não a raizes reais")

if delta == 0:
    print("possui uma soluçaõ sendo x = {}".format(((list_termos[1]*-1) + (delta**1/2))/(2*list_termos[0])))

if delta > 0:
    x1 = ((-1*list_termos[1]) - (delta**1/2))/(2*list_termos[0])
    x2 = ((-1*list_termos[1]) + (delta**1/2))/(2*list_termos[0])
    print(x1,x2)
    

print(delta)



