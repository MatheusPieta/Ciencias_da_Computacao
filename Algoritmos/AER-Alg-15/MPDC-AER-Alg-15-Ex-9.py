numero1 = int(input("Digite o numero: "))
soma = 0
contador = 0
while numero1>0:
    numero1 = numero1-contador
    contador = 1
    if numero1%2==1:
            print("Números impares: ", numero1)
            soma = soma + numero1
print("soma de todos os numeros= ", soma)
print ("Fim do programa...")
