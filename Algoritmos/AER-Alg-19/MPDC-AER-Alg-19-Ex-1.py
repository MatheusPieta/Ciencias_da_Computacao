def hipotenusa(co, ca):
    return (co ** 2 + ca ** 2) ** (1/2)

def main():
    co = float(input("Comprimento do Cateto oposto: "))
    ca = float(input("Comprimento do Cateto adjacente: "))
    hi = hipotenusa(co, ca)
    print('A hipotenusa vai medir {:.2f}'.format(hi))

if __name__ == "__main__":
    main()


    

