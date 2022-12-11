def longest_word(filename):
    words = filename.read().split()
    max_len = len(max(words, key=len))
    longa = ([word for word in words if len(word) == max_len])
    print(f"Palavra mais longa do arquivo é:{longa}")


def main():
    filename = open(r"C:\Users\Matheus\Google Drive\Faculdade - Disciplinas\Algoritmos\AER-Alg-28\cabeçalho.txt") 
    longest_word(filename)

if __name__ == "__main__":
    main()