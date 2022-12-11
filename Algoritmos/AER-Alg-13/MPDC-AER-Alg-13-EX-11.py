dia = int(input('digite qual dia é: '))
mes = int(input('digite qual mês é: '))
ano = int(input('digite que ano é: '))

a = (ano-1900)
b = (a/4)
c = 0
d = 0
S = -1
R = 0

if (ano%4==0 and ano%100!=0) or (ano%400==0):
     b = b + 1
else:
    b = b + 0

if(b == 1) and (dia == 29) and (mes == 2):
  b = b - 1

if ( b != 1):
  b = b + 0

if (mes == 1) or (mes == 10):
    c = c + 0

if(mes == 2) or (mes == 3) or (mes == 11):
    c = c + 3

if(mes == 4) or (mes == 7):
    c = c + 6

if(mes == 5):
    c = c + 1

if(mes == 6):
    c = c + 4

if(mes == 8):
    c = c + 2

if(mes == 9) or (mes == 12):
    c = c + 5

d = d + dia
d = d -1
S = (S + a + b + c + d ) % 7
R = R + S

if(R == 0):
  print("O dia é Segunda Feira")

if(R == 1):
  print("O dia é Terça Feira")

if(R == 2):
  print("O dia é Quarta Feira")

if(R == 3):
  print("O dia é Quinta Feira")

if(R == 4):
  print("O dia é Sexta Feira")

if(R == 5):
  print("O dia é Sabado")

if(R == 6):
  print("O dia é Domingo")
