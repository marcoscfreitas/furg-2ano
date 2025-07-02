def maiorVetor(vetor, tamanho) :
    if tamanho == 1 :
        return vetor[0]
    maior = maiorVetor(vetor,tamanho-1)
    if vetor[tamanho-1] > maior :
        maior = vetor[tamanho-1]
    return maior

vetor = [1,3,5,2,10,2]
tamanho = len(vetor)

saida = maiorVetor(vetor,tamanho)

print(saida)