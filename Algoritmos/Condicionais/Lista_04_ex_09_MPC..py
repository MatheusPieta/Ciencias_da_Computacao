corretor1 = input("Digite o nome do primeiro corretor: ")
corretor2 = input("Digite o nome do segundo corretor: ")
corretor3 = input("Digite o nome do terceiro corretor: ")

venda1 = float(input("Digite o valor da venda do corretor 1: "))
venda2 = float(input("Digite o valor da venda do corretor 2: "))
venda3 = float(input("Digite o valor da venda do corretor 3: "))

if(venda1>50000):
    print("nome do corretor:" ,corretor1, "valor da comissao", (venda1*0.12))
elif(50000>=venda1>=30000):
    print("nome do corretor:" ,corretor1, "valor da comissao", (venda1*0.095))
elif(venda1<30000):
    print("nome do corretor:" ,corretor1, "valor da comissao", (venda1*0.7))


if(venda2>50000):
    print("nome do corretor:" ,corretor2, "valor da comissao", (venda2*0.12))
elif(50000>=venda2>=30000):
    print("nome do corretor:" ,corretor2, "valor da comissao", (venda2*0.095))
elif(venda2<30000):
    print("nome do corretor:" ,corretor2, "valor da comissao", (venda2*0.7))


if(venda3>50000):
    print("nome do corretor:" ,corretor3, "valor da comissao", (venda3*0.12))
elif(50000>=venda3>=30000):
    print("nome do corretor:" ,corretor3, "valor da comissao", (venda3*0.095))
elif(venda3<30000):
    print("nome do corretor:" ,corretor3, "valor da comissao", (venda3*0.7))