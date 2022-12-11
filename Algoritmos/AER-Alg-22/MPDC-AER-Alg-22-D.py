def impressao(frase, comprimento):
    print(frase)
    for i in range(1,comprimento):
        print(frase[:-i])

def main():
    frase = input("Digite a String: ")
    comprimento = len(frase)
    impressao(frase, comprimento)
    

if __name__ == "__main__":
    main()