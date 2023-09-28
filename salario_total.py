salario_base = float(input("Digite seu salário base: "))
salario_total = 0

salario_total = (((salario_base*0.05) + salario_base) - (salario_base*0.07))

print('Seu salário base é de {}, com os descontos de 7% e o acressimo de 5%, seu salário total é de {}'.format(salario_base, salario_total))