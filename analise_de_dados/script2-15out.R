# criando distribuição de frequencia no R

# install.packages('fdth')

library(fdth)
library(dplyr)

dados <- c(151  , 152  , 154  , 155 , 158 , 159 , 159 , 160 ,  161  , 161 ,
           161  , 162  , 163  , 163 , 163 , 164 , 165 , 165 ,  165  , 166,
           166  , 166  , 166  , 167 , 167 , 167 , 167 , 167 ,  168  , 168 ,
           168  , 168  , 168  , 168 , 168 , 168 , 168 , 168 ,  169  , 169 ,
           169  , 169  , 169  , 169 , 169 , 169 , 170 , 170 ,  170  , 170 ,
           173  , 173  , 174  , 174 , 174 , 175 , 175 , 175 ,  175  , 176 ,
           176  , 176  , 176  , 177 , 177 , 177 , 177 , 178 ,  178  , 178 ,
           179  , 179  , 180  , 180 , 180 , 180 , 181 , 181 ,  181  , 182 ,
           182  , 182  , 183  , 184 , 185 , 186 , 187 , 188 ,  190  , 190 )

dados <- dados/100
table(dados)

# criar distribuição
distribuicao <- fdt(dados)
distribuicao

n <- length(dados)
n

at <- max(dados) - min(dados)
at

k <- 1 + (3.3*log10(n))
k

# arredondar K
ceiling(k) # arredonda p/ cima
floor(k) # arredonda p/ baixo
round(k,digits = 2) # arredonda com 2 decimais

k_a <- ceiling(k)

# criar tamanho dos intervalos de classe
h <- round(at/k_a,2)

# criar distribuicao estabelecendo minimo e maximo
comeco = round(min(dados),2)
fim = k_a * h + comeco

d <- fdt(dados, start = comeco, end = fim, h = h)
d

# distribuição com 5 classes
k <- 5

h <- round(at/k,digits = 2)
h

comeco = 1.5#round(min(dados),2)
fim = k * h + comeco

d2 <- fdt(dados, start = comeco, end = fim, h = h)
d2




