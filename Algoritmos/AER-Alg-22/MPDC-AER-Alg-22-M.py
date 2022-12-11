def palindroma(junto):
    n = len(junto)
    k = 0
    while k<n/2:
        if junto[k] != junto[n-k-1]:
            print("Essa palavra não é palindroma")
            return
        k = k+1
    print("Essa palavra é palindroma")
    return


def main():
    string = str(input("Digite uma frase! ")).upper()
    palavras = string.split()
    junto = "".join(palavras)
    palindroma(junto)

if __name__ == "__main__":
    main()