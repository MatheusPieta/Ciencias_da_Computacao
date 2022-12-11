listX = []
while True:
    n = int(input("Numero: "))
    if n == 0:
        break
    listY = [n]
    listX += listY
lista_ordenada = sorted(listX)
print("Numeros ordenados:", lista_ordenada)