maior = 0
for i in range (1,13):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num

print("O maior valor foi: ", maior)