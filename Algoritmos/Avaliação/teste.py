def busca_reversa(chave):
    chave = chave.lower()
    dados = {'nome': "Matheus Pieta da Cunha", 'idade': "19", 'trabalho:': "Hospital", 'bebida favorita:': "Suco de Laranja"}
    if chave in dados:
        final = dados[chave]
        print(final)
    else:
        print("Busca não encontrada!")


def main():
    chave = str(input("Insira: "))
    busca_reversa(chave)



if __name__ == "__main__":
    main()