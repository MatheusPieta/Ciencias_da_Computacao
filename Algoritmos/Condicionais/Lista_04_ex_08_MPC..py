nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua nota em Português: "))
nota2 = float(input("Digite sua nota em Matemática: "))
nota3 = float(input("Digite sua nota em Conhecimentos Gerais: "))

media = (nota1+nota2+nota3)/3
print('Nome: ',nome,'\n Nota 1: ', nota1, '\n Nota 2: ', nota2 ,'\n Nota 3: ', nota3,"\n Sua média é igual a: ",media)

if(((media>=7) and (nota1>5) and (nota2>5) and (nota3>5))):
    print('Nome: ',nome,"\n Você foi aprovado")
else:
    print('Nome: ',nome, '\n Você foi reprovado')