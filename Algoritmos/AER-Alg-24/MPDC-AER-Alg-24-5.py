def div_inteiros(num):
    num = int(input("Vamos verificar seus divisores: "))
    lista = []
    divisor = 1
    if num == 1:
        print(20*"-")
        print("Numero somente divisivel por ele mesmo")
        print(20*"-")
    for divisor in range(1, num):
        if (num / divisor) == (num // divisor):
            lista.append(divisor)
    return lista

def main(div_inteiros):
    num = (input("quer começar? "))
    print(div_inteiros(num))


if __name__ == "__main__":
    main(div_inteiros)