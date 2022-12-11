def separar_frase(lista, palavra):
    lista.append(palavra)
    lista2 = palavra.split()
    print(lista2)



def main():
    lista = []
    palavra = str(input("Insira uma frase: "))
    separar_frase(lista, palavra)


if __name__ == "__main__":
    main()