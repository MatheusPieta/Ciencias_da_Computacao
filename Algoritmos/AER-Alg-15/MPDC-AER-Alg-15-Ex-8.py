numero1 = 1
numero2 = int(input("Digite o o final da contagem: "))
soma = 0
contador = 0
while numero1<=numero2:
    numero2 = numero2-contador
    contador = 1
    if numero2%2==0:
            print("Números: ", numero2)
            soma = soma + numero2
print("soma de todos os numeros= ", soma)
print ("Fim do programa...")
