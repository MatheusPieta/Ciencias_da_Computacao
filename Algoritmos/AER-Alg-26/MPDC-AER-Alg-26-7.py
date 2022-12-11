import random

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


def main():
    carta = generate_carta()
    print(20*"==")
    print("Sua carta:")
    print(20*"==")
    print_carta(carta)
    print(20*"==")


main()