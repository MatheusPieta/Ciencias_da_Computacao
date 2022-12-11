N = int(input('Digite um número até 999!'))

C= N // 100
X= N % 100
D = X // 10
U = X % 10

resultado= U*100 + D*10 + C



print('N=', resultado)