list_numbers = []
numbers_input = 3 

while numbers_input != 0: 
    list_numbers.append(int(input("Type 3 numbers: ")))
    numbers_input -=1 

itens_sum = 0
equation = 0
while list_numbers[2] != 0:
    itens_sum = list_numbers[0] + list_numbers[1]*list_numbers[2]
    equation = itens_sum**3 + 3*(itens_sum**2) + equation
    list_numbers[2] -= 1 

print(equation)