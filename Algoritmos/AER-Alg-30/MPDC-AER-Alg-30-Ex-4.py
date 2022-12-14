def memoria(f):
    memo = {}
    def ajuda(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return ajuda
    

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(13))