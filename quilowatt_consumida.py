salario_minimo = float(input("Digite o salario minimo atual: "))
quilowatt_consumido = float(input("Digite a quantia de quilowatt que foi consumida: "))


print('valor de um quilowatt é igual a {}'.format(salario_minimo/5))
print('A residencia vai pagar um total de {}'.format((quilowatt_consumido*(salario_minimo/5))))
print('E com o desconto de 15% o total fica {}'.format((quilowatt_consumido*(salario_minimo/5)) - (quilowatt_consumido*(salario_minimo/5)*0.15)))