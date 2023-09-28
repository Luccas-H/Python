ano_nascimento = int(input("Digite o ano que você nasceu: "))
ano_atual = int(input("Digite o ano atual: "))

print("Você nasceu em {} e, sabendo que atualmente estamos em {} e que você tem {} anos, então em 2035 você terá {}".format(ano_nascimento,ano_atual,ano_atual-ano_nascimento,2035-ano_nascimento))