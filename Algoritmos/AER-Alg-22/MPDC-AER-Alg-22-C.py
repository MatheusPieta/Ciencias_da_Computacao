def impressao(frase, comprimento):
    for linha in range(comprimento):
        for col in range(linha+1):
            print(frase[col], end="")
        print()

def main():
    frase = input("Digite a String: ")
    comprimento = len(frase)
    impressao(frase, comprimento)
    

if __name__ == "__main__":
    main()