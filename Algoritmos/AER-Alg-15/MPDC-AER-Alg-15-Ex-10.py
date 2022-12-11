numero = int(input('Digite a tabuada desejada: '))
divisor = 1

print(20*'-')

while(divisor<=10):
    na = numero * divisor
    print(numero, 'x' ,divisor, '=' ,na)
    divisor = divisor + 1

print(20*'-')