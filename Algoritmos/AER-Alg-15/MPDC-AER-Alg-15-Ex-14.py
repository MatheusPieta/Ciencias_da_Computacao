a = 0
maior = menor = quant = 0
while a < 12:
    num = int(input("Digite um número: "))
    a += 1
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print("O menor numero digitado é: ", menor, " ------------ " "O maior digitado é: ", maior)
