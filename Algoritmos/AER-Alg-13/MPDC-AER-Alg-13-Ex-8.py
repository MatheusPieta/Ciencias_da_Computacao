quantidade = int(input("Digite quantos produtos voce comprou: "))
valor = float(input("Digite o valor unitario do item: "))
total = (quantidade*valor)

print('total da sua compra sem descontos: ',total,)

if(quantidade>=15):
    conta = (total*0.10)
    desconto10 = (total-conta)
    print('sua compra com desconto de 10% é: ',desconto10,)
if(total>=100) and (quantidade>=15):
    conta2 = (desconto10*0.20)
    desconto1020 = (desconto10-conta2)
    print('sua compra com todos os descontos deu: ',desconto1020,)