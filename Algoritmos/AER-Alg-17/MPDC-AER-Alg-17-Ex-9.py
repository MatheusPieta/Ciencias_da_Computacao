soma = 0
final = int(input("Digite o numero: "))
for i in range(1,final+1):
    if i%2 ==1:
        print("impares=", i)
        soma = soma + i
print("Soma total=", soma)