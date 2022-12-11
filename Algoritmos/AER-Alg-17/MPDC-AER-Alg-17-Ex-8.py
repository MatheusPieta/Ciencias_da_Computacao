final = int(input("Digite um numero para o final da contagem: "))
soma = 0
for i in range(1,final+1):
    if i%2 ==0:
        soma = soma + i
        print("O numeros pares até", final, "são: ", i)
print("A Soma total é igual a: ", soma)