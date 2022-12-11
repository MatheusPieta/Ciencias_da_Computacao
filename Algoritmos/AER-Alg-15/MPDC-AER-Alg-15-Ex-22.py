num = int(input("Digite um numero: "))
soma = 0
x = 1
divisor = 1
while x <= num:
    divisor = num - divisor
    soma = soma + (divisor/x)
    divisor += 1
    x += 1
soma = soma + num
print("O resultado de A é: ", soma)