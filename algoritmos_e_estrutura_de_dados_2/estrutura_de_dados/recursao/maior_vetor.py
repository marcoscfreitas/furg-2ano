# def maiorVetor(vetor, tamanho) :
#     if tamanho == 1 :
#         return vetor[0]
#     maior = maiorVetor(vetor,tamanho-1)
#     if vetor[tamanho-1] > maior :
#         maior = vetor[tamanho-1]
#     return maior

# vetor = [1,3,5,2,10,2]
# tamanho = len(vetor)

# saida = maiorVetor(vetor,tamanho)

# print(saida)

# solução alternativa
def maximo(vetor,pos=0) :
    if pos == len(vetor) -1 :
        return vetor[pos]
    max_resto = maximo(vetor, pos+1)

    if vetor[pos] > max_resto :
        return vetor[pos]
    else :
        return max_resto

lista = [4,7,1,9,3]
print(maximo(lista))