def oi(fname, N):
    for line in (fname.readlines() [-N:]): 
        print(line, end ='')

def main():
    fname = open(r"C:\Users\Matheus\Google Drive\Faculdade - Disciplinas\Algoritmos\AER-Alg-28\cabeçalho.txt") 
    N = 10
    try: 
        oi(fname, N) 
    except: 
        print('File not found')

if __name__ == "__main__":
    main()