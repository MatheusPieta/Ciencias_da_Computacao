def total(x):
    if x==1:
        return 10.95
    else:
        return (x-1)*2.95+10.95

def main():
    x = int(input("digite a quantidade de itens adquiridos: "))
    print('Seu frete deu o total de: {}'.format(total(x)))

if __name__ == "__main__":
    main()