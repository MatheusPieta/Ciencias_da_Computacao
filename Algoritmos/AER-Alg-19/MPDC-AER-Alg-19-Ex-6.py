def bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))


def dias_do_mes(mes, ano):
    if (mes==4) or (mes==6) or (mes==9) or (mes==11):
        return 30
    elif (mes==2) and bissexto(ano):
        return 29
    elif (mes==2):
        return 28
    else:
        return 31

def main():
    mes = int(input("digite um mes (1 a 12): "))
    ano = int(input("digite um ano (aaaa): "))
    dias = dias_do_mes(mes, ano)
    print("O mes {0} do ano {1} tem {2} dias.".format(mes, ano, dias))

if __name__ == "__main__":
    main()