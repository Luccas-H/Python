lista = [2,5,3,4,5,5,6,7,8,6]
lista_sem_repetidos = []
lista_dos_repetidos = []


def numero_repetido (lista_funcao):
    for numero in lista_funcao:
        if numero in lista_sem_repetidos:
            if numero in lista_dos_repetidos:
                continue    
            else:
                lista_dos_repetidos.append(numero)
        else:
            lista_sem_repetidos.append(numero)
        
    return lista_sem_repetidos, lista_dos_repetidos    
    
print(numero_repetido(lista))