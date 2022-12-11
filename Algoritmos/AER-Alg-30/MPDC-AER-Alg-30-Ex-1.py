def fatorial(n):
    if n==0 or n==1:
        return 1
    return n * fatorial(n-1)

def main():
    n = int(input("Digite um numero para o fatorial: "))
    fatorial(n)
    print(fatorial(n))

main()