def soma_dig(d):
    return d//10 + d%10


def soma_dig2(m):
    return m//10 + m%10


def soma_dig3(ano):
    return ano//10 + ano%10


def main():
    d = int(input("Digite um dia de nascimento(XX): "))
    m = int(input("Digite o seu mes de nascimento(DD): "))
    a = int(input("Digite o seu ano de nascimento algarismos(YYYY): "))
    ano = a%100
    print("A sua senha é:",soma_dig(d), soma_dig2(m),soma_dig3(ano))

if __name__ == "__main__":
    main()
