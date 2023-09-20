list1 = []
list2 = []
list_resultado = []
soma = 0

for i in range (3):
    num1 = int(input('Digite um numero: '))
    list1.append(num1)
for i in range (3):
    num2 = int(input('Digite um numero: '))
    list2.append(num2)

soma = list1[0] + list2[0]
list_resultado.append(soma)
soma = list1[1] +  list2[1]
list_resultado.append(soma)
soma = list1[2] +  list2[2]
list_resultado.append(soma)

print(list1,list2)    
print(list_resultado)
   