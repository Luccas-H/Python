list_data = []
list_data_comparar = []
list_data_maior = []

n = 0 
while n!=3:
    d = int(input("Digite a data começando pelo dia e utilizando esse formato (dd/mm/yyyy): "))
    list_data.append(d)
    n += 1 
l = 0
while l!=3:
    dt = int(input("Digite a proxima data começando pelo dia e utilizando esse formato (dd/mm/yyyy):"))
    list_data_comparar.append(dt)
    l +=1 

if list_data[0] <= list_data_comparar[0]:
    list_data_maior.append(list_data_comparar[0])  
if list_data[1] <= list_data_comparar[1]:
    list_data_maior.append(list_data_comparar[1])  
if list_data[2] <= list_data_comparar[2]:
    list_data_maior.append(list_data_comparar[2])  
    
else:
    list_data_maior.append(list_data[0])  
    list_data_maior.append(list_data[1])  
    list_data_maior.append(list_data[2])  



print(list_data_maior)