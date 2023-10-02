numero_horas = int(input("Digite o número de horas: "))
numero_minutos = int(input("Digite os minutos: "))

print('{}h são equivalentes a {}min'.format(numero_horas, numero_horas*60))
print('{}min + {}min = {}min'.format(numero_minutos, numero_horas*60, numero_minutos+(numero_horas*60)))
print('{}x60s = {}'.format(numero_minutos+(numero_horas*60),(numero_minutos+(numero_horas*60))*60))