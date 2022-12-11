valor_compra = int(input("Digite o valor da compra: "))
valor_pago = int(input("Digite o valor pago: "))

troco = valor_pago - valor_compra

x= troco // 100
x1=troco%100
y= x1 //10
y1= x1%10
z= y1 //1

print('O troco com notas de 100 é:',x)
print('O troco com notas de 10 é:',y)
print('O troco com notas de 1 é:',z)