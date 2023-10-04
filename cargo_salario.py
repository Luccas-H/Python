n = int(input("A partir da tabela:\n 1->Escriturário\n 2->Secretário\n 3->Caixa\n 4->Gerente\n 5->Diretor\nDigite o numero requerido para saber qual será o percentual: "))

if  n>5 or n<1:
    print("ERRO.......\n O número digitado não esta na tabela, reavalie e tente novamente")
    n = "Erro"
else:
    s = float(input("Digite o salário que essa função recebe: "))


    if n == 1:
        print('O Escriturário receberá {} e com isso seu salário será de {}'.format(s*0.5, s + (s*0.5)))
    if n == 2:
        print('O Secretário receberá {} e com isso seu salário será de {}'.format(s*0.35, s + (s*0.35)))
    if n == 3:
        print('O Caixa receberá {} e com isso seu salário será de {}'.format(s*0.2, s + (s*0.2)))
    if n == 4:
        print('O Gerente receberá {} e com isso seu salário será de {}'.format(s*0.1, s + (s*0.1)))
    if n == 5:
        print("O Diretor não receberá aumento, logo seu salário permanece igual a {}".format(s))
