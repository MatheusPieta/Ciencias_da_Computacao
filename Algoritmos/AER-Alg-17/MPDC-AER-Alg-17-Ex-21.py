num = int(input("Digite o valor de N: "))
soma = 0
x = 1
for i in range(0,num):
    soma = soma + (1/x)
    x += 1
print("O resultado de A é: ", soma)