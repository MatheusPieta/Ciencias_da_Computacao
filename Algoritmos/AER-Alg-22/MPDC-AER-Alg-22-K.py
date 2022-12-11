def data_extenso(data):
    meses = ('janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    dia, mes, ano = data.split("/")
    mes = int(mes)-1
    print ("Voce nasceu em %s de %s de %s"%(dia, meses[mes], ano))


def main():
    data = input("Digite a sua data de nascimento utilizando numeros no formato dia/mes/ano: ")
    data_extenso(data)

if __name__ == "__main__":
    main()