# INSERTION-SORT

A = [31, 41, 59, 26, 41, 58]
n = len(A)

for j in range(1, n):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key

'''
PSEUDO-CÓDIGO (n = length[A])
INSERTION-SORT(A)                           CUSTO        ITERAÇÕES
1. for j ← 2 to length[A] do                 C1         n-2+1+1 = n
2.      key ← A[j]                           C2         n-2+1 = n-1
3.      # insere A[j] na sequencia           C3=0           n-1
3.      i ← j - 1                            C4             n-1
4.      while i >= 0 and A[i] > key do       C5     ∑_{j = 2}^{n} (tj)
5.          A[i+1] ← A[i]                    C6     ∑_{j = 2}^{n} (tj - 1)
6.          i ← i -1                         C7     ∑_{j = 2}^{n} (tj - 1)
7.      A[i+1] ← key                         C8             n-1
'''

#FUNÇÃO DE TEMPO DE EXECUÇÃO GERAL:
# C1.n + C2.(n-1) + C4.(n-1) + C5.(∑_{j = 2}^{n} (tj)) + C6.(∑_{j = 2}^{n} (tj - 1)) + C7.(∑_{j = 2}^{n} (tj - 1)) + C8.(n-1)

#FUNÇÃO DE TEMPO DO MELHOR CASO (VETOR DE ENTRADA ORDENADO); A[i] > key sempre FALSE:
# iteração da linha 5: ∑_{j=2}^{n} tj = ((1+1).(n-1))/2 = n-1
# iterações das linhas 6 e 7: 0
# C1 + C2.n + C3.(n-1) + C4.((n²+n-2)/2) + C5.(n-1) + C9.(n-1) + C10.(n-1) + C11.(n-1)

#FUNÇÃO DE TEMPO DO PIOR CASO (VETOR NA ORDEM INVERSA); A[i] > key sempre True:
# iteração da linha 5: vai ser executado a depender do valor de J,
# se j = 2, i = 1; i = 0 > executado 2 vezes
# se j = 3, i = 2; i = 1, i = 0 > executado 3 vezes
# se j = n, i = n-1, i = n-2 ... i = 0 > executado n vezes
# então, iteração da linha 5: ∑_{j=2}^{n} tj = ((n+2).(n-1))/2 = (n²+n-2)/2
# já as linhas 6 e 7 serão executados -1 vezes, já que estão dentro do while, ou seja, ∑_{j=2}^{n} tj - 1 = ((1+(n-1)).(n-1))/2 = (n²-n)/2
# C1 + C2.n + C3.(n-1) + C4.((n²+n-2)/2) + C5.((n²+n-2)/2) + C6.((n²-n)/2) + C7.((n²-n)/2) + C9.(n-1) + C10.(n-1) + C11.(n-1)