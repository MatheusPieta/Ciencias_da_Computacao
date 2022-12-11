def triangulo(canudo1, canudo2, canudo3):
    if canudo1>canudo2+canudo3:
        return ("Não é posivel formar um triangulo")
    if canudo2>canudo1+canudo3:
        return ("Não é posivel formar um triangulo")
    if canudo3>canudo2+canudo1:
        return ("Não é posivel formar um triangulo")
    else:
        return ("É possivel formar um triangulo ")

def main():
    canudo1 = float(input("Digite o comprimento do primeiro canudo: "))
    canudo2 = float(input("Digite o comprimento do segundo canudo: "))
    canudo3 = float(input("Digite o comprimento do terceiro canudo: "))
    print(triangulo(canudo1, canudo2, canudo3))

if __name__ == "__main__":
    main()