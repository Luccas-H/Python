list_num = []

def add(**num):
    list_num.append(num["insert"])
    
n = 0
while n!=3:
    add(insert = int(input("Digite um numero: ")))    
    n += 1
    
def bigger(top):
    maior = max(top)
    menor = min(top)
    print("Esse é o maior número {}".format(maior))
    print("Esse é o menor número {}".format(menor))
    
bigger(list_num)