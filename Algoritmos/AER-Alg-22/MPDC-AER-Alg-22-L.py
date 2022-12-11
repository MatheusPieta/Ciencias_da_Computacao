def isCpfValid(cpf):
  
    if cpf=='00000000000' or cpf=='11111111111' or cpf=='22222222222' or cpf=='33333333333' or cpf=='44444444444' or cpf=='55555555555' or cpf=='66666666666' or cpf=='77777777777' or cpf=='88888888888' or cpf=='99999999999':
        print("Cpf Invalido")
        return

    if len(cpf) != 11:
        print("Cpf Invalido")
        return
    sum = 0
    peso = 10

    for n in range(9):
        sum = sum + int(cpf[n]) * peso

        peso = peso - 1

    verifica1 = 11 -  sum % 11

    if verifica1 > 9 :
        primeiro = 0
    else:
        primeiro = verifica1
    
    sum = 0
    peso = 11

    for n in range(10):
        sum = sum + int(cpf[n]) * peso

        peso = peso - 1

    verifica1 = 11 -  sum % 11

    if verifica1 > 9 :
        verifica2 = 0
    else:
        verifica2 = verifica1

    if cpf[-2:] == "%s%s" % (primeiro,verifica2):
        print("Cpf valido")
        return

def main():
    cpf = (input("Digite seu CPF sem pontuação: "))
    isCpfValid(cpf)

if __name__ == "__main__":
    main()