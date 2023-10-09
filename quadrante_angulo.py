grau = int(input("Digite o angulo desejado: "))


if grau < 0:
    print("Sentido horário")
    grau = grau%360
    if grau <= 0 and grau >= -90:
        print("Pertence ao quarto quadrante")

    if grau < -90 and grau >= -180:
        print("Pertence ao terceiro quadrante")

    if grau < -180 and grau >= -270:
        print("Pertence ao segundo quadrante")

    if grau < -270 and grau >= -360:   
        print("Pertence ao primeiro quadrante")
        
if grau > 360:
    print("anti-horário")
    print('O número de voltas é igual a {:.2}'.format(grau/360))
    grau = grau%360
    if grau >= 0 and grau <= 90:
        print("Pertence ao primeiro quadrante")

    if grau > 90 and grau <= 180:
        print("Pertence ao segundo quadrante")

    if grau > 180 and grau <= 270:
        print("Pertence ao terceiro quadrante")

    if grau > 270 and grau <= 360:   
        print("Pertence ao quarto quadrante")
    
else:
    if grau >= 0 and grau <= 90:
        print("Pertence ao primeiro quadrante")

    if grau > 90 and grau <= 180:
        print("Pertence ao segundo quadrante")

    if grau > 180 and grau <= 270:
        print("Pertence ao terceiro quadrante")

    if grau > 270 and grau <= 360:   
        print("Pertence ao quarto quadrante")

