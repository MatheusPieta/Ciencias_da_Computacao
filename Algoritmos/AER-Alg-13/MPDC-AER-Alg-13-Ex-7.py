nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua 1° nota: "))
nota2 = float(input("Digite sua 2° nota: "))
faltas = int(input("Digite a sua quantidade de faltas: "))
nf = 5

media = (nota1+nota2)/2
nf = (nf - media)

if(((media>=5) and (nota1>3) and (nota2>3) and (faltas<15))):
    print('Nome: ',nome,"\n Parabens, Você foi aprovado!")
if(((media>=5) and (nota1>3) and (nota2>3) and (faltas>15))):
    print("Reprovado por faltas.")
if(((media<5) and (faltas<15))):
    print('Voce tera que tirar :' , nf , 'no exame final.')