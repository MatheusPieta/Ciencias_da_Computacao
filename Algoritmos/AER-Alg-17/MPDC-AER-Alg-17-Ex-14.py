maior = menor = quant = 0
for i in range (1,13):
    num = int(input("Digite um número: "))
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print("O menor numero digitado é: ", menor, "e o maior digitado é: ", maior)
