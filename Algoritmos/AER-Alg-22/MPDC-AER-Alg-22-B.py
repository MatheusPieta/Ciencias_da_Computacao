def impressao(frase):
    for letra in frase:
        print(letra)

def main():
    frase = str(input("Digite uma frase! "))
    impressao(frase)
    

if __name__ == "__main__":
    main()