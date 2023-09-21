n = int(input("Digite um número:"))
m = int(input("Digite um número:"))
list_num = []
d = 2
s = 0

list_num.append(n)
list_num.append(m)

for i in list_num:
    list_num.sort(key=int)
    
    while i%d != 0 and d*d <= i:
        d = d + 1 
    if d*d >= i:
        print("primo")
    else:
        print("não primo")
    d = 2    

for j in list_num:
    s = j - s
    if s == 2:
        print("é gem")
    
