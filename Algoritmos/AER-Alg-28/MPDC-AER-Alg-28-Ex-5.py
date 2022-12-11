f = open(r"C:\Users\Matheus\Google Drive\Faculdade - Disciplinas\Algoritmos\AER-Alg-28\cabeçalho.txt") 
cont = 0
for line in f: 
    cont = cont + 1
    print(f"linha {cont}:", line.rstrip()) 

