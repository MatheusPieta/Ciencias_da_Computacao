def ocorrencia(c, f, v):
    for i in range(0,v):
        f=f.replace(c[i],"")
        print(f)

def main():
    c = str(input("Qual caractere voce deseja selecionar? "))
    f = str(input("Digite uma frase! "))
    v = len(c)
    ocorrencia(c, f, v)

if __name__ == "__main__":
    main()
