def comparacao(frase1, frase2):
    if frase1 == frase2:
        print("as frases são iguais")
    else:
        print("As frases são diferentes")


def main():
    frase1 = str(input("Digite uma frase! "))
    frase2 = str(input("Digite uma frase! "))
    comparacao(frase1, frase2)

if __name__ == "__main__":
    main()
