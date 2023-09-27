n = str(input("Digite uma palavra(em minúsculo): "))
letras = []


for i in n:
    letras.append(i)

if letras == letras[::-1]:
    print("É um palindromo")
else:
    print("Não é um palindromo")
