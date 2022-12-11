codigo= int(input('Digite o código de matricula!'))

AA = codigo//10000
X = codigo%10000
S= X//1000
DDD= X% 1000

print('Ano da Matricula: ',AA,'\nE o semestre:',S)