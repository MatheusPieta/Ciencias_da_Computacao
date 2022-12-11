gm = float(input("Digite o valor gasto em material: "))
tc = float(input("Digite o Tempo em horas da duração da construção: "))
cmo = float(input("Digite o custo por hora da mão de obra: "))
ac = float(input("Digite a Metragem da área construida: "))
r = ac/tc

if (r<0.035):
    cmo = (cmo)*0.3

print (cmo)




