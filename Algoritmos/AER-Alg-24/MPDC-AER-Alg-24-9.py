def countRange(lista, minimo, maximo, verificado):
    lista9 = []
    lista8 = []
    for i in range(minimo, maximo):
        lista += [i]
    for listas in lista:
        if listas >= verificado:
            listasY = [listas]
            lista8 += listasY
        if listas <= verificado:
            listasX = [listas]
            lista9 += listasX
    print("numeros menores que o verificador: ", lista9)
    print("numeros maiores que o verificador: ", lista8)

def main():
    lista = []
    minimo = int(input("Digite o valor minimo da lista: "))
    maximo = int(input("Digite o valor maximo da lista: "))
    verificado = int(input("Digite o digito verificador: "))
    countRange(lista, minimo, maximo, verificado)

if __name__ == "__main__":
    main()