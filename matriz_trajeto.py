matrix = [ [0 for i in range(8)] for j in range(8)]
size = 8


position = []
for i in range(size + 1):
    for x in range(i):
        for y in range(i-1,-1,-1):
            if [x,y] in position:
                pass
            else:
                position.append([x,y])

test = []   
n = 1
for i in range(len(position)):
    soma = sum(position[i])
    test.append(soma)


for line in range(size):
    for column in range(0,size,1):
        matrix[line][column] = n
        n +=1 

for line in range(8):
    for column in range(8):
        print( "%4d"% matrix[line][column], end='')
    print()


print(position)
print()
print(test)
print()
print(matrix)
#Not finished 