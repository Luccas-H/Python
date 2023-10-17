list_notas = []

def add(**num):
    list_notas.append(num["insert"])
    
n = 0
while n!=3:
    add(insert = int(input("Digite um número: ")))    
    n += 1


def media(notas):
    final = sum(notas)/3
    print("A média final do trimestre é {}".format(final))
    
media(list_notas)