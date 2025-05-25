# SELECTION-SORT

A = [20,12,10,15,2]
n = len(A)

for i in range(n-1) :
    menor = i
    for j in range(i+1, n) :
        if A[j] < A[menor] :
            menor = j
    temp = A[i]
    A[i] = A[menor]
    A[menor] = temp

'''
PSEUDO-CÓDIGO
SELECTION-SORT(A)                         CUSTO        ITERAÇÕES
1. n ← length[A];                          C1              1
2. for j ← 1 to n - 1 do                   C2       (n-1)- 1 + 1 + 1 = n       
3.      smallest ← j;                      C3       (n-1)- 1 + 1 = n-1
4.      for i ← j + 1 to n do              C4   ∑_{j = 1}^{n-1} (n - (j+1) + 1 + 1) = ∑_{j = 1}^{n-1} (n - j + 1) = (n²+n-2)/2
5.          if A[ i ] < A[smallest] then   C5   ∑_{j = 1}^{n-1} (n - (j+1) +1) = ∑_{j = 1}^{n-1} (n - j) = (n²-n)/2
6.              smallest ← i;              C6          t6 = ? depende
7.          end if;                        C7=0           n²/n/2
8.      end for;                           C8=0            n-1
9.      tmp ← A[ j ];                      C9              n-1
10.     A[ j ] ← A[smallest];              C10             n-1
11.     A[smallest] ← tmp;                 C11             n-1
12. end for;                               C12=0            1
13. end procedure.                         C13=0            1
'''

#FUNÇÃO DE TEMPO DE EXECUÇÃO GERAL:
# C1 + C2.n + C3.(n-1) + C4.((n²+n-2)/2) + C5.((n²-n)2) + C6.t6 + C9.(n-1) + C10.(n-1) + C11.(n-1)

#FUNÇÃO DE TEMPO DO MELHOR CASO (VETOR DE ENTRADA ORDENADO), t6 = 0:
# C1 + C2.n + C3.(n-1) + C4.((n²+n-2)/2) + C5.((n²-n)2) + C9.(n-1) + C10.(n-1) + C11.(n-1)

#FUNÇÃO DE TEMPO DO PIOR CASO (VETOR NA ORDEM INVERSA), t6 = ((n²-n)/2):
# C1 + C2.n + C3.(n-1) + C4.((n²+n-2)/2) + C5.((n²-n)2) + C6.((n²-n)/2) + C9.(n-1) + C10.(n-1) + C11.(n-1)