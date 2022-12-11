divisor = 1
numero=1

print(20*'-')

for i in range(divisor,11):
    numero = 1
    for c in range(numero,11):
        na = numero * divisor
        print(divisor, 'x' ,numero, '=' ,na)
        numero+=1
    print(20*"-")
    divisor = divisor + 1


