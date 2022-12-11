def anagrama(palavra1, c1, palavra2, c2):
    if len(c1) == (len(c2)):
        return True
    else:
        return False

def main():
    palavra1 = str(input("escreva a primeira palavra: "))
    palavra2 = str(input("Insira outra palavra: "))
    c1 = set(palavra1)
    c2 = set(palavra2)
    print(anagrama(palavra1, c1, palavra2, c2))

if __name__ == "__main__":
    main()