def palindromo(f):
    f = f.upper()
    s2 = ""
    for letra in f:
        if letra != " ":
            s2 += letra
    for i in range(len(s2)):
        if s2[i] != s2[len(s2)-i-1]:
            return False
    return True

def main():
    f = input("Digite a frase: ")
    palindromo(f)
    print(palindromo(f))

main()