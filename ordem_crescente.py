list_num = []

n=0
while n!=3:
    p = float(input("Digite um número: "))
    list_num.append(p)
    n += 1

list_num.sort()
print(list_num)