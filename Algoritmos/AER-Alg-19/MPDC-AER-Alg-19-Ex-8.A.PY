def calcula_percent(a, b, c, valor):
    return valor + a + b + c
    

def main():
    valor = float(input("Digite o valor do seu produto: "))
    a = valor * 0.50
    b = (valor + a) * 0.03
    c = (valor * 0.10 + b * 0.02)
    print(calcula_percent(valor, a, b, c))

if __name__ == "__main__":
    main()