#Ele identifica se o numero que voce digitou é um divisor perfeito
def div_inteiros(num):
    lista = []
    divisor = 1
    soma = 0
    if num == 1:
        print(20*"-")
        print("Numero somente divisivel por ele mesmo")
        print(20*"-")
    for divisor in range(1, num):
        if (num / divisor) == (num // divisor):
            lista.append(divisor)
    for listas in lista:
        soma += listas
    if soma == num:
        print("Seu numero tem a divisão perfeita")
    else:
        print("Este numero não tem a divisão perfeita")

def main():
    num = int(input("Vamos verificar seus divisores: "))
    div_inteiros(num)

if __name__ == "__main__":
    main()