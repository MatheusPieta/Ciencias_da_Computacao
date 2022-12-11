a = 0
menor = 0
while a < 12:
    num = int(input("Digite um número: "))
    a += 1
    if menor > num:
        menor = num

print("O menor valor foi: ", menor)

