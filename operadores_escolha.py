operador = int(input("Digite o número da operação desejada pela seguinte lista:\n 1->Média entre os dois números.\n 2->Diferencia entre o maior e o menor.\n 3->O produto entre os dois numeros\n: "))
list_numeros = []

n = 0

if operador <1 or operador >3:
    print("ERRO...") 
    print("Reavalie as operações disponíveis e tente novamente!!") 

else:
    
    while n!=2:
        t = float(input("Digite um numero: "))
        list_numeros.append(t)
        n += 1
    
    if operador == 1:
        print ('A média entre os dois números é {}'.format((list_numeros[0]+list_numeros[1])/2))
    
    if operador == 2:
        if list_numeros[0] >= list_numeros[1]:
            print('A diferença entre o maior e o menor é de {}'.format(list_numeros[0]-list_numeros[1]))
        else:
            print('A diferença entre o maior e o menor é de {}'.format(list_numeros[1]-list_numeros[0]))
    
    if operador ==3:
        print('O produto entre os dois números é igual {}'.format(list_numeros[0]*list_numeros[1]))