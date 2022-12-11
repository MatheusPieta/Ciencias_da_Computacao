resp = 'S'
while resp in "Ss":
    num = int(input('Digite um numero:' ))
    print(20*"-")
    if num%2==1:
        print("o numero" ,num , "é somente divisivel por 1 e por ele mesmo!")
        num = num - 2
    if num%2==0:
        for i in range (1 , num+1):
            if (num % i) == 0:
                print("Os numeros divisiveis por", num , "são:", i)
    

    print(20*"-")
    resp = str(input("Quer continuar? [S/N] "))[0]
    print(20*"-")
print ("Então encerramos por hoje, obrigado!")
print(20*"-")

