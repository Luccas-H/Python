matrix = [ [0 for i in range(8)] for j in range(8)]

in_p = 0
position = 0
while in_p != 1:
    position = input("line/colunn: ")
    if position == 'stop':
        in_p += 1
    else:
        position_line = int(position[0]) - 1
        position_colunn = int(position[1]) -1 
        matrix[position_line][position_colunn] = 1

for line in range(8):
    for column in range(8):
        print( "%4d"% matrix[line][column], end='')
    print()

count_B = 0
count_P = 0
code = []
for line in range(8): 
    for column in range(8):
       
        if matrix[line][column] == 0:
            count_B +=1
            if count_P > 0:
                code.append(f"{count_P}P")
                count_P = 0
    
        elif matrix[line][column] == 1:
            count_P += 1
            if count_B> 0:
                code.append(f"{count_B}B")            
                count_B = 0   
    
    if count_P > 0:
        code.append(f"{count_P}P")
        count_P = 0
    elif count_B > 0:
        code.append(f"{count_B}B")
        count_B = 0
        
    code.append("0")

code.insert(len(code) -1, "00")
code.pop()

for i in code:
    print(i, end = " ")


