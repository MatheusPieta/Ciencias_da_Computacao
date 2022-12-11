def caracteres_unicos(palavra, c):
    if (len(c)) == (len(palavra)):
        return True
    else:
        return False

def main():
    palavra = str(input("escreva a palavra: "))
    c = set(palavra)
    print(caracteres_unicos(palavra, c))

if __name__ == "__main__":
    main()