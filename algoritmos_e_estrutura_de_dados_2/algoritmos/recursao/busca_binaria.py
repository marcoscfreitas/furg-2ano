def busca_binaria(vetor, valor, inicio, fim) :
    # Caso base: elemento não encontrado
    if inicio > fim :
        return -1
    
    # Calcula o meio
    meio = inicio + (fim-inicio) // 2
    # Elemento encontrado
    if vetor[meio] == valor :
        return meio
    
    # Busca na metade esquerda
    elif vetor[meio] > valor :
        return busca_binaria(vetor, valor, inicio, meio-1)
    else : # Busca na metade direita
        return busca_binaria(vetor, valor, meio+1, fim)
    
# Exemplo de uso

v = [0,1,1,2,3,5,8,13,21,34]
saida = busca_binaria(v, 21, 0, len(v)-1)
print('o número está na posição',saida)

# Função T(n)
'''
        | θ(1)          ; n < 1 (caso base)
T(n) =  |
        | θ(1) + T(n/2) ; n > 1
'''