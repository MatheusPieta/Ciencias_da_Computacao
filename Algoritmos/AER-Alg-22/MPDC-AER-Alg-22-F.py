def ocorrencia(f, v):
    indice = 0
    while indice < v:
        letra = f[indice]
        print (letra+letra, end="")
        indice = indice + 1

def main():
    f = str(input("Digite uma frase! "))
    v = len(f)
    ocorrencia(f, v)

if __name__ == "__main__":
    main()
