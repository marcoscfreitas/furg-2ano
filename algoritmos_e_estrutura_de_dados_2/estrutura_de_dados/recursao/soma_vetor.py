# def somaVetor(vetor, indice) :
#     if indice >= len(vetor) :
#         return 0
#     if vetor[indice] > 0 :
#         return vetor[indice] + somaVetor(vetor,indice+1)
#     else :
#         return somaVetor(vetor,indice+1)
    
# indice = 0
# saida = somaVetor([1,-2,3,4], indice)
# print(saida)

# solução alternativa
def somarVetor(vetor, indice=0) :
    if indice >= len(vetor) :
        return 0
    return vetor[indice] + somarVetor(vetor,indice+1)

r = somarVetor([1,-2,3,4])
print(r)

'''
return 0
return(4 + somarVetor(vetor,4)) => 4 + 0 = 4
return(3 + somarVetor(vetor,3)) => 3 + 4 = 7
return(-2 + somarVetor(vetor,2)) => -2 + 7 = 5
return(1 + somarVetor(vetor,1)) => 1 + 5 = 6
'''