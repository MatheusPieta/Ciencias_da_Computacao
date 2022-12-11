f = open(r"C:\Users\Matheus\Google Drive\Faculdade - Disciplinas\Algoritmos\AER-Alg-28\cabeçalho.txt") 
l = 0 
for line in f: 
    l = l + 1 
    if l <= 10:
        print("Linha", l, line.rstrip()) 
f.close()
