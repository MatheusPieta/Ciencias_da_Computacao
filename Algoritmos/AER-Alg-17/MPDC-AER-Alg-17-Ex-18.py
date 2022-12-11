soma = 0
negativo = 0
for i in range(1,20):
    num = int(input("Digite um número: "))
    if num>=0:
        soma = soma + num
    if num<0:
        negativo += 1

print(20*"-")
print("A soma dos numeros positivos é: ", soma)
print(20*"-")
print("A quantidade de valores negativos digitados foram: ", negativo)
print(20*"-")       
