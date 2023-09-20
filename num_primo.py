n = int(input("Digite a quantia de números:"))
d= 2
list_num = []
list_tip = []
while n>0:
    m = int(input ("Digite o número escolhido: "))
    n = n - 1
    list_num.append(m)

while m%d!=0 and d*d<=m:
    d = d + 1

if d*d<=m:
    list_tip.append("m não é primo")
else:
    list_tip.append("m é primo")

print(list_tip)

print(list_num)