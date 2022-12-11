def prefixo(palavra1, palavra2):
    if len(palavra1)>len(palavra2):
        print("não pode")
        return
    i = 0
    while i<len(palavra1):
        if palavra1[i]!=palavra2[i]:
            print("Essa palavra é um sufixo da primeira")
            return
        i = i+1


def main():
    palavra1 = str(input("Digite uma frase! "))
    palavra2 = str(input("Digite uma frase! "))
    prefixo(palavra1, palavra2)

if __name__ == "__main__":
    main()