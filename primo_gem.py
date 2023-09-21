n = int(input("Digite um número:"))
m = int(input("Digite um número:"))
list_num = []
list_gem = []
d = 2
s = 0

list_num.append(n)
list_num.append(m)

for i in list_num:

    while i%d != 0 and d*d <= i:
        d = d + 1 
    if d*d >= i:
        print("primo")
        
    else:
        print("não primo")
    list_num.sort()
    s = i - s
    if s == 2:
        print("primo gem")
    d = 2    

    
    
