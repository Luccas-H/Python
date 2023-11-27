m = int(input ("Digite o número escolhido: "))    
d= 2
while m%d!=0 and d*d<=m:
    d = d + 1

if d*d<=m:
    print(f"{m} não é primo")
else:
    print(f"{m} é primo")
