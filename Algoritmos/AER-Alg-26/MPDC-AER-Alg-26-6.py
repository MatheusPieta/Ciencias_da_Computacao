def anagrama(palavra1, palavra2):
    minusculo1 = palavra1.lower()
    sem_espacos1 = ''.join([x for x in minusculo1 if x != ' '])
    minusculo2 = palavra2.lower()
    sem_espacos2 = ''.join([x for x in minusculo2 if x != ' '])
    c1 = set(sem_espacos1)
    c2 = set(sem_espacos2)
    if len(c1) == (len(c2)):
        print("É um anagrama")
    else:
        print("Não é um anagrama")

def main():
    palavra1 = str(input("escreva a primeira palavra: "))
    palavra2 = str(input("Insira outra palavra: "))
    anagrama(palavra1, palavra2)

if __name__ == "__main__":
    main()