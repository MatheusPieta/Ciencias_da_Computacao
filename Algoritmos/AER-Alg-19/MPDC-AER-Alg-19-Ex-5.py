def bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

def main():
    x = int(input("digite um ano (aaaa): "))
    if bissexto(x):
        print("O ano", x, "é bissexto")
    else:
        print("O ano", x, "não é bissexto")

if __name__ == "__main__":
    main()