def inverter(frase):
    frase2 = " "
    for p in frase:
        frase2 = p + frase2
    print(frase2)

def main():
    frase = str(input("Digite uma frase! "))
    inverter(frase)

if __name__ == "__main__":
    main()
