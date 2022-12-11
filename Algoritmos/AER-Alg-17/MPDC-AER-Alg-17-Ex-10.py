numero = int(input('Digite a tabuada desejada: '))
divisor = 1

print(20*'-')

for i in range(1,11):
    na = numero * divisor
    print(numero, 'x' ,divisor, '=' ,na)
    divisor = divisor + 1

print(20*'-')