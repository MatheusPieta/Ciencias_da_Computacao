a = 0
maior = 0
while a < 12:
    num = int(input("Digite um número: "))
    a += 1
    if num > maior:
        maior = num

print("O maior valor foi: ", maior)