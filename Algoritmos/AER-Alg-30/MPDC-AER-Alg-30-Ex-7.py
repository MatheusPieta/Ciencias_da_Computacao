def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])

def main():
    lista = [1, 0, 3, 5, 7]
    soma_lista(lista)
    print(soma_lista(lista))

main()