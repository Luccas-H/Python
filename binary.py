binary_digits = str(input("Type a 0 or 1 sequence: "))

list_binary = []
for number in binary_digits:
    list_binary.append(number)

count_zero = 0 
count_one = 0 

for zero_one in list_binary:
    if count_one <= 2:
        if zero_one == '0':
            count_zero += 1
            count_one = 0 
    if count_zero <= 2:
        if zero_one == '1':
            count_one += 1
            count_zero = 0
    else:
        break

if count_one > 2 or count_zero > 2:
    print("This code is invalid")
else:
    print("This code is valid")