numero_horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
numero_horas_extras = float(input("Digite as horas extras: "))
valor_salario_minimo = float(input("Digite o valor do salario minimo: "))

salario_bruto = 0 
salario_extra = 0 

valor_hora_trabalho = valor_salario_minimo/8
valor_hora_extra = valor_salario_minimo/4

salario_bruto = numero_horas_trabalhadas*valor_hora_trabalho
salario_extra = numero_horas_extras*valor_hora_extra

print('O salário divido em horas trabalhadas e horas extra equivale a {} + {} = {}'.format(salario_bruto, salario_extra, salario_bruto + salario_extra))