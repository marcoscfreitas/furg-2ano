def fibonacci_rec(n) :
        if n == 0 :
            return 0
        if n == 1 :
            return 1
        else :
            return fibonacci_rec(n-1) + fibonacci_rec(n-2)

n = 5
saida = fibonacci_rec(n)
print(saida)

# Solução Rodrigo
'''
def fibonacci(n) :
    if n <= 1 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

        print('o 5º número de fibonnaci é ', fibonacci(9))
'''

# Função T(n)
'''
        | θ(1)                   ; n >= 1 (caso base)
T(n) =  |
        | θ(1) + T(n-1) + T(n-2) ; n > 1
'''