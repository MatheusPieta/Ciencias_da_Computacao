divisor = 1
num = int(input("Digite o valor de N: "))
soma = 0
x = 1
for i in range(0,num):
    divisor = num - divisor
    soma = soma + (divisor/x)
    divisor += 1
    x += 1
soma = soma + num
print("O resultado de A é: ", soma)