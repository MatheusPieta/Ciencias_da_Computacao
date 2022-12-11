numero1 = int(input("Digite o inicio do intervalo: "))
numero2 = int(input("Digite o Fim do intervalo: "))
soma = 0
for i in range(numero1,numero2+1):
    if i%2 ==0:
        print(i)
        soma = soma + i
print(20*"-")
print("Soma dos numeros pares entre", numero1, "a", numero2, "é:", soma)
print(20*"-")