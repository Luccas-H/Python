idade = float(input('Digite a sua idade: '))
peso = float(input('Digite a seu peso: '))
grupo_risco = 0

if idade < 20:
    if peso < 60:
        grupo_risco = 9
        print(grupo_risco)
    if peso >=60 and peso <=90:
        grupo_risco = 8
        print(grupo_risco)
    if peso > 90:
        grupo_risco = 7
        print(grupo_risco)

if idade >= 20 and idade <= 50:
    if peso < 60:
        grupo_risco = 6
        print(grupo_risco)
    if peso >=60 and peso <=90:
        grupo_risco = 5
        print(grupo_risco)
    if peso > 90:
        grupo_risco = 4
        print(grupo_risco)

if idade > 50:
    if peso < 60:
        grupo_risco = 3
        print(grupo_risco)
    if peso >=60 and peso <=90:
        grupo_risco = 2
        print(grupo_risco)
    if peso > 90:
        grupo_risco = 1
        print(grupo_risco)

