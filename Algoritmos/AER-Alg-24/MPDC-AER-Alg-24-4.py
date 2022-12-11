listX = []
listNegativo = []
listaPositivo = []
print("Digite numeros para que os mesmos sejam ordenados!")
while True:
    n = int(input("Digite um número: "))
    para = n
    if para == "":
        break
    if n <= 0:
        lista = [n]
        listNegativo += lista
    if n >= 0:
        lista1 = [n]
        listaPositivo += lista1
print(listNegativo)
print(listaPositivo)