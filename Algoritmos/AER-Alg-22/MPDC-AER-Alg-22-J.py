def substituir_brancos(frase, vezes, brancos):
    for i in range (0,vezes):
        if frase[i]==" ":
            brancos = brancos + 1
    print (f"Quantidade de brancos: {brancos}")

def main():
    frase = str(input("Digite uma frase! "))
    vezes = len(frase)
    brancos = 0
    substituir_brancos(frase, vezes, brancos)

if __name__ == "__main__":
    main()
