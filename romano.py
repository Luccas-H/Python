ask = str(input("Digite um número romano: "))
base_dict = {
    "M" : 1000,
    "D" : 500,
    "C" : 100,
    "L": 50,
    "X":10,
    "V":5,
    "I":1
    
}
list_conjunto  =[]
list_split = []
quantia = []

for i in ask: 
    list_split.append(i)
print(list_split)

limite = len(list_split)
for i in range(len(list_split)):
    x = base_dict[list_split[i]]
    quantia.append(x)

maior = 0 
igual = 0 
for i in quantia:
    if quantia.index(min(quantia)) < quantia.index(max(quantia)):
        maior = (max(quantia) - min(quantia))
    else:
        igual = sum(quantia)


print(quantia)
print(maior)
print(igual)