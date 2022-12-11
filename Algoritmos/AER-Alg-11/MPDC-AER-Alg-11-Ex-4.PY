r = float(input("Digite raio: "))
x = float(input("Digite o X do ponto: "))
y= float(input("Digite o Y do ponto: "))
if (x**2 + y**2 == r**2):
    print("Ponto esta na circunferencia.")
else:
    if (x**2 + y**2 < r**2):
        print("Ponto é interno.")
    else:
        print("Ponto é externo.")