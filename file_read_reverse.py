with open ("text_real.txt", "w") as file:
    file.write("Hello world, this line must be in second line\n")
    file.write("Hello world, this line must be in first line\n")
    file.close()

lista = []

with open("text_real.txt", "r") as file:
    for i in file.readlines():
        lista.append(i)
    file.close()

lista.reverse()
with open("text_reverse.txt","w") as file:
    for i in lista:
        file.write(i)
           
     