def ocorrencia(f, v):
    for letra in f:
        print(letra,end="")
        if letra.lower() in "aeiou":
            print(letra, end="")
        


def main():
    f = str(input("Digite uma frase! "))
    v = len(f)
    ocorrencia(f, v)

if __name__ == "__main__":
    main()
