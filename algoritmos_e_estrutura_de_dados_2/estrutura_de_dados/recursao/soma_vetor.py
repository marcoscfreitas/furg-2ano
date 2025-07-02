def somaVetor(vetor, indice) :
    if indice >= len(vetor) :
        return 0
    if vetor[indice] > 0 :
        return vetor[indice] + somaVetor(vetor,indice+1)
    else :
        return somaVetor(vetor,indice+1)
    
indice = 0
saida = somaVetor([1,-2,3,4], indice)
print(saida)