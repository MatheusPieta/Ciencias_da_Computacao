nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua nota em Português: "))
nota2 = float(input("Digite sua nota em Matemática: "))
faltas = int(input("Digite a sua quantidade de faltas: "))

media = (nota1+nota2)/2
print('Nome: ',nome,'\n Português: ', nota1, '\n Matemática: ', nota2 ,"\n Sua média é igual a: ",media)

if(((media>=5) and (nota1>3) and (nota2>3) and (faltas<15))):
    print('Nome: ',nome,"\n Parabens, Você foi aprovado!")
elif(((media>=9) and (nota1>3) and (nota2>3) and (faltas<15))):
    print("Vimos que sua media é nove ou mais, Gostaria de se tornar nosso monitor no proximo semestre?")
else:
      print( '',nome,'' '\n Você foi reprovado')