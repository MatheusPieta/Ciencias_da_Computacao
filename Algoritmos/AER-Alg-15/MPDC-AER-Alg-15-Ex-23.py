num = int(input("Digite um numero: "))
soma = 0
x = 1
while x <= num:
    if x%2==0:
        soma = soma - (1/x)
        x += 1
    else:
        soma = soma + (1/x)
        x += 1
print("O resultado de A é: ", soma)