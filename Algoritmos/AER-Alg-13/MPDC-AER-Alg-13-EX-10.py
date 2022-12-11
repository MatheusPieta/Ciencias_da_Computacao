altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio dos cilindros: "))
area = (raio**2)
diametro = (area*altura)

quantidade = (diametro/15)
latas = (quantidade*20)


print('A quantidade necessária de latas serão: ',quantidade,'\n O total gasto será: ', latas ,)
