import random

random_sorteado_list = random.sample(range(1, 76), 75)

def generate_carta():

    carta = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": [],
    }
    min = 1
    max = 15
    for letra in carta:
        carta[letra] = random.sample(range(min, max), 5)
        min += 15
        max += 15
        if letra == "N":
            carta[letra][2] = "X" 
    return carta

def print_carta(carta):

    for letra in carta:
        print(letra, end="\t")
        for numero in carta[letra]:
            print(numero, end="\t")
        print("\n")
    print("\n")

def sorteado(carta, list):

    numero_sorteado = random_sorteado_list.pop()
    for letra in carta:
        i = 0
        for numero in carta[letra]:
            if numero == numero_sorteado:
                carta[letra][i] = "X"
            i += 1
    return numero_sorteado

def check_vencedor(carta):

    vencedor = False
    if carta["B"][0] == "X" and carta["I"][1] == "X" and carta["N"][2] == "X" and carta["G"][3] == "X" and carta["O"][4] == "X":
        vencedor = True
    elif carta["O"][0] == "X" and carta["G"][1] == "X" and carta["N"][2] == "X" and carta["I"][3] == "X" and carta["B"][4] == "X":
        vencedor = True
    elif carta["B"][0] == "X" and carta["O"][4] == "X" and carta["B"][4] == "X" and carta["O"][0] == "X":
        vencedor = True
    for letra in carta:
        if(len(set(carta[letra]))==1):
            vencedor = True
    for i in range(5):
        cnt = 0
        for letra in carta:
            if carta[letra][i] == "X":
                cnt += 1
        print(cnt)
        if cnt == 5:
            vencedor = True
            break
    return vencedor

def main():

    print("Vamos jogar!")
    carta = generate_carta()

    print("\nEssa é sua carta:\n")
    print_carta(carta)

    print("\nAperte enter para continuar.\n")
    user_input = input()
    vencedor = check_vencedor(carta)
    bolas_ate_vencedor = 0

    while vencedor == False and user_input != "quit":
        numero_sorteado = sorteado(carta, random_sorteado_list)
        bolas_ate_vencedor += 1

        print(f"\nSorteio: {numero_sorteado}.")
        print(f"total de bolas sorteadas: {bolas_ate_vencedor}.\n")
        print_carta(carta)

        vencedor = check_vencedor(carta)

        user_input = input()
    if vencedor == True:
        print(f"\nBingo! total de bolas para ganhar: {bolas_ate_vencedor}.")
    else:
        print("Obrigado por jogar!")

main()