n = int(input("Digite o número de fileiras: "))
p = 1
for i in range(n):
    for j in range(i):
        print(p,end = " ")
        p +=1
    print()
   