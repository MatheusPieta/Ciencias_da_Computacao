def potencia(a, b):
    if b<0:
        print("Não é possivel calcular pois a potencia é negativa!")
    else:
        resultado = a ** b
        print(resultado)



def main():
    a = int(input("Digite a base: "))
    b = int(input("Digite a potencia: "))
    potencia(a, b)

main()