def ocorrencia(c, f):
    return f.count(c)

def main():
    c = str(input("Qual caractere voce deseja selecionar? "))
    f = str(input("Digite uma frase! "))
    o = ocorrencia(c, f)
    print('O caractere "{}" aparece {} vezes na string!'.format(c, o))

if __name__ == "__main__":
    main()
