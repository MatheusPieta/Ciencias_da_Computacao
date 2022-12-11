def primo(valor):
    if valor%2==1:
        return True
    else: 
        return False


def main():
    valor = int(input("Digite um numero: "))
    print(primo(valor))


if __name__ == "__main__":
    main()