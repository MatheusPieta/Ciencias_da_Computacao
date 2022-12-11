codigo= int(input('Digite um codigo de 5 algarismo:'))

A= codigo//10000
X= codigo%10000
B= X//1000
Z= X%1000
C= Z//100
Y= Z%100
D = Y//10
E= Y%10



S = 6*A + 5*B + 4*C + 3*D + 2*E

digitoV= S % 7


print(digitoV)
