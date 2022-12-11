listX = []
listv = []
while True:
    n = int(input("Numero: "))
    if n == 0:
        break
    listY = [n]
    listX += listY

lista_ordenada = sorted(listX)
for x in lista_ordenada [::-1]:
    lista = [x]
    listv += lista
print(listv)