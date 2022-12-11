def soma_dig(n):
    return n//10 + n%10


def main():
    n = int(input("Digite um numero de 2 algarismos(XX): "))
    print("A soma dos algarismos é igual a: {}".format(soma_dig(n)))

if __name__ == "__main__":
    main()
