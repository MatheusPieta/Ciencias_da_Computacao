g = input("selecione o objeto - quadrado, retangulo, ou circulo: ")
entrada_valida = True

if g == "quadrado":
    lado = float (input("fornceça o lado do quadrado: "))
    area = lado * lado
    objeto = "quadrado"

elif g == "retangulo":
    a = float(input("forneça o lado a do retangulo: "))
    b = float(input("forneça o lado b do retangulo: "))
    area = a * b
    objeto = "retangulo"

elif g == "c":
    r = float(input("fornceça o raio do circulo: "))
    area = 3.14 * r ** 2
    objeto = "circulo"

else: 
    print ("Entrada Inválida!")
    entrada_valida = False

if entrada_valida:
    print(f"A área do {objeto} é {area}")