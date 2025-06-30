def soma_rec(vetor, n) :
    if n == len(vetor) - 1 :
        return vetor[n]
    else :
        return vetor[n] + soma_rec(vetor, n + 1)
    
vetor = [1,2,3,4]
n = 0
saida = soma_rec(vetor,n)
print(saida)

# Solução Rodrigo
'''
def soma(vetor) :
    if len(vetor) == 0 :
        return 0
    return vetor[0] + soma(vetor[1:])

numeros = [1,2,3,4,5]
resultado = soma(numeros)
print('soma do vetor: ', resultado)
'''

# Função T(n)
'''
        | θ(1)          ; n = 0 (caso base)
T(n) =  |
        | θ(1) + T(n-1) ; n >= 1
'''