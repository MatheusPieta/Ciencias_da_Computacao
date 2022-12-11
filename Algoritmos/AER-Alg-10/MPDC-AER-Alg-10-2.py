venda = (input("Forneça o Valor total das vendas: "))
if not venda . isdecimal ():
    print ("valor fornecido invalido")

else:
    if (float(venda) <= 2500):
        c = 30 + 0.017 * (float(venda))
        if c <= 39:
            c = 39
    elif (float(venda) <= 6250):
        c = 56 + 0.0066 * (float(venda))
    elif (float(venda) <= 20000):
        c = 76 + 0.0034 * (float(venda))
    elif (float(venda) <= 50000):
        c = 100 + 0.0022 * (float(venda))
    elif (float(venda) <= 500000):
        c = 255 + 0.0009 * (float(venda))
    print (f"Sua comissão foi: R$ {c}")