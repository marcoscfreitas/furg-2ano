def fatorial(n) :
    if n <= 1 :
        return 1 # caso base
    return n * fatorial(n-1) # passo recursivo

print('O fatorial de 3 é', fatorial(3))