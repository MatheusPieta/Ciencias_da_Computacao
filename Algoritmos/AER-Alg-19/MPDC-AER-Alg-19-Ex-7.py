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

def data_magica(dia, mes, ano):
  return  (dia * mes == ano%100)

def main():
    i = 1
    for ano in range(1900, 2000):
        for mes in range(1, 13):
            for dia in range(1, dias_do_mes(mes, ano)+1):
                if data_magica(dia, mes, ano):
                    print("Data magica {3}: {0}/{1}/{2}".format(dia, mes, ano, i))
                    i += 1



if __name__ == "__main__":
    main()