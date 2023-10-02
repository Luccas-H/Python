#Não está pronto ainda!!!!
list_num = []
list_resu = []
n=0
while n!=3:
    p = float(input("Digite um número: "))
    list_num.append(p)
    n += 1


if list_num[0]>=list_num[1] and list_num[0] <= list_num[2]:
    list_resu.insert(1,list_num[0])
elif list_num[0]<=list_num[1] and list_num[0] >= list_num[2]:
    list_resu.insert(2,list_num[0])
elif list_num[0]<list_num[1] and list_num[0] < list_num[2]:
    list_resu.insert(0,list_num[0])

if list_num[1]>=list_num[0] and list_num[1] <= list_num[2]:
    list_resu.insert(1,list_num[1])
elif list_num[1]<=list_num[0] and list_num[1] >= list_num[2]:
    list_resu.insert(2,list_num[0])
elif list_num[0]<list_num[1] and list_num[0] < list_num[2]:
    list_resu.insert(0,list_num[0])

if list_num[0]>=list_num[1] and list_num[0] <= list_num[2]:
    list_resu.insert(1,list_num[0])
elif list_num[0]<=list_num[1] and list_num[0] >= list_num[2]:
    list_resu.insert(2,list_num[0])
elif list_num[0]<list_num[1] and list_num[0] < list_num[2]:
    list_resu.insert(0,list_num[0])




print(list_resu)