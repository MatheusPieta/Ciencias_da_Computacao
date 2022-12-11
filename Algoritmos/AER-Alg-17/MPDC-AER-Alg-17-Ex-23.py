num = int(input("Digite o valor de N: "))
soma = 0
x = 1
for i in range(0,num):
    if x%2==0:
        soma = soma - (1/x)
        x += 1
    else:
        soma = soma + (1/x)
        x += 1
print("O resultado de A é: ", soma)