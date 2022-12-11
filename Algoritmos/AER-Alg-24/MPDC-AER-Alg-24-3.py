def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l


def main(remove_repetidos):
    palavra = str(input("Quer começar? "))
    lista = []
    lista = remove_repetidos(lista)
    while palavra != '':
        palavra = str(input("Insira uma palavra: "))
        lista.append(palavra)
    if palavra == '':
        lista.remove('')
    print (remove_repetidos(lista))


if __name__ == "__main__":
    main(remove_repetidos)