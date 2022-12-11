lista = []
def lista_format(listafinal):
    palavra = str(input("Quer começar? "))
    while palavra != '':
        palavra = str(input("Insira uma palavra: "))
        lista.append(palavra)
    lista.insert((len(lista) - 2), "e")
    return lista


def main(lista_format):
    listafinal = str(lista).strip('[]')
    print(lista_format(listafinal))

if __name__ == "__main__":
    main(lista_format)