nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua nota em Português: "))
nota2 = float(input("Digite sua nota em Matemática: "))

media = (nota1+nota2)/2
print('Nome: ',nome,'\n Nota 1: ', nota1, '\n Nota 2: ', nota2 ,"\n Sua média é igual a: ",media)

if(media>=5):
    print('Nome: ',nome,"\n Parabens, Você foi aprovado")
else:
    print('Nome: ',nome, '\n Você foi reprovado')