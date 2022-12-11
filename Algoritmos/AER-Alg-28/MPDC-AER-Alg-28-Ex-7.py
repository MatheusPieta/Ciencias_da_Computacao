frequencia = {}
f = open(r"C:\Users\Matheus\Google Drive\Faculdade - Disciplinas\Algoritmos\AER-Alg-28\cabeçalho.txt")
for line in f:
    line = line.upper()
    for char in line:
        if char in frequencia:
            frequencia[char] += 1
        else:
            frequencia[char] = 1
for  key, value in frequencia.items():
    print(key, ":", value)