def calcula_percent(XX, YY):
    return (XX*15+YY)
    
    
def main():
    codigo = int(input("Os codigos do seu produto: "))
    XX = codigo//100
    YY = codigo%100
    menos = YY/100

    total = calcula_percent(XX, YY)
    desconto = calcula_percent(XX, YY)*menos
    total = total - desconto

    print("Total a pagar: R${:.2f}".format(total))

if __name__ == "__main__":
    main()