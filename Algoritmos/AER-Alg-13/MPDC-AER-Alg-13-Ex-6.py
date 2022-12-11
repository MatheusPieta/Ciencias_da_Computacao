nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

divisor = (altura*altura)
imc = (peso/divisor)

print('Seu IMC é: ',imc,)

if((imc<18.5)):
    print("voce esta abaixo do peso ideal")
