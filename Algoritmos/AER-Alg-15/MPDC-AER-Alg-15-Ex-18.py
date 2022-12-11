a = 0
soma = 0
negativo = 0
while a < 20:
    num = int(input("Digite um número: "))
    a += 1
    if num>=0:
        soma = soma + num
    if num<0:
        negativo += 1

print(20*"-")
print("A soma dos numeros positivos é: ", soma)
print(20*"-")
print("A quantidade de valores negativos digitados foram: ", negativo)
print(20*"-")       
