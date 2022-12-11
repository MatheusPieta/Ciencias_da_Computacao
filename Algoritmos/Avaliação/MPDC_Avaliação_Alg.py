# Respostas Atividade Avaliativa
# Autor: Matheus Pieta da Cunha

#Questão 1

def div_inteiros(num):
    num = int(input("Vamos verificar seus divisores: "))
    lista = []
    divisor = 1
    if num == 1:
        print(20*"-")
        print("Numero somente divisivel por ele mesmo")
        print(20*"-")
    for divisor in range(1, num):
        if (num / divisor) == (num // divisor):
            lista.append(divisor)
    return lista


#Questão 2

def numeros_perfeitos(num):
    lista = []
    divisor = 1
    soma = 0
    if num == 1:
        print(20*"-")
        print("Numero somente divisivel por ele mesmo")
        print(20*"-")
    for divisor in range(1, num):
        if (num / divisor) == (num // divisor):
            lista.append(divisor)
    for listas in lista:
        soma += listas
    if soma == num:
        print("Seu numero tem a divisão perfeita")
    else:
        print("Este numero não tem a divisão perfeita")

#Questão 3

def data_extenso(data):
    meses = ('janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    dia, mes, ano = data.split("/")
    mes = int(mes)-1
    print ("Voce nasceu em %s de %s de %s"%(dia, meses[mes], ano))

#questão 4

def busca_reversa(chave):
    chave = chave.lower()
    dados = {'nome': "Matheus Pieta da Cunha", 'idade': "19", 'trabalho:': "Hospital", 'bebida favorita:': "Suco de Laranja"}
    if chave in dados:
        final = dados[chave]
        print(final)
    else:
        print("Busca não encontrada!")

def main():
#Bote aqui a chamada do exercicio que voce deseja ver a solução!


if __name__ == "__main__":
    main()