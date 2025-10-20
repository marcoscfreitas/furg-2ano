# exercicio 3

# media
xi <- c(0, 1, 2, 3, 4, 5, 6, 7)
fi <- c(2, 25, 15, 10, 3, 2, 1, 2)
xifi <- xi * fi
n <- sum(fi)
soma <- sum(xifi)
media <- soma / n
media

# moda
posicao_maior <- which.max(fi)
posicao_maior
moda <- xi[posicao_maior]
moda

# mediana
fac <- cumsum(fi)
fac
pos <- n / 2
pos

posicao <- which(fac >= pos)[1]
posicao
mediana <- xi[posicao]
mediana

# criando função de resumo de dados
resumo_de_dados <- function(x = x, f = f)
{
  xifi <- x * f
  n <- sum(f)
  soma <- sum(xifi)
  media <- soma / n
  
  posicao_maior <- which.max(fi)
  moda <- xi[posicao_maior]
  
  fac <- cumsum(fi)
  pos <- n / 2
  posicao <- which(fac >= pos)[1]
  mediana <- xi[posicao]
  
  resultado <- c(media, moda, mediana)
  names(resultado) <- c('média', 'moda', 'mediana')
  resultado
}
resumo_de_dados(xi, fi)

# exercicio 4

lim_inf <- c(0, 4, 8, 12, 16)
lim_sup <- c(4, 8, 12, 16, 20)
fi <- c(8, 15, 24, 20, 13)
xi = pm <- (lim_inf + lim_sup) / 2

# media
xifi <- xi * fi
n <- sum(fi)
media <- sum(xifi) / n

# moda
posicao_maior <- which.max(fi)

# delta 1 = freqModa - freqAnt
delta1 <- fi[posicao_maior] - fi[posicao_maior - 1]

# delta 2 = freqModa - freqPost
delta2 <- fi[posicao_maior] - fi[posicao_maior + 1]

# calcular a moda
li_mo <- lim_inf[posicao_maior]
h <- lim_sup[posicao_maior] - lim_inf[posicao_maior]
moda <- round(li_mo + (delta1 / (delta1 + delta2)) * h, 2)
moda

# mediana

# classe da mediana
fac <- cumsum(fi)
pos <- n / 2
posicao <- which(fac >= pos)[1]
#calcular a mediana
li_me <- lim_inf[posicao]
h <- lim_sup[posicao] - lim_inf[posicao]
soma_ant <- fac[posicao - 1]

mediana <- li_me + ((pos - soma_ant) / fi[posicao]) * h

tabela <- cbind(lim_inf, lim_sup, fi, xi, fac)
tabela

# variancia
xi2fi <- xifi * xi
tabela <- cbind(tabela, xi2fi)
tabela

variancia <- (1 / (n - 1)) * (sum(xi2fi) - ((sum(xifi) ^ 2) / n))
variancia

desviopadrao <- sqrt(variancia)
desviopadrao

coef_vari <- desviopadrao / media * 100
coef_vari

nomes <- c('média','moda','mediana','variância','desvio padrão','coef. variação')
resumo_agrupado <- round(c(media, moda, mediana, variancia, desviopadrao, coef_vari), 2)

names(resumo_agrupado) <- nomes
resumo_agrupado

resumo_dados_agrupados <- function(lim_inf,lim_sup,fi)
{
  xi <- (lim_inf + lim_sup) / 2
  n <- sum(fi)
  
  # media
  xifi <- xi * fi
  media <- sum(xifi) / n
  
  # moda
  posicao_maior <- which.max(fi)
  
  # delta 1 = freqModa - freqAnt
  delta1 <- fi[posicao_maior] - fi[posicao_maior - 1]
  
  # delta 2 = freqModa - freqPost
  delta2 <- fi[posicao_maior] - fi[posicao_maior + 1]
  
  # calcular a moda
  li_mo <- lim_inf[posicao_maior]
  h <- lim_sup[posicao_maior] - lim_inf[posicao_maior]
  moda <- round(li_mo + (delta1 / (delta1 + delta2)) * h, 2)
  
  # mediana
  
  fac <- cumsum(fi)
  pos <- n / 2
  posicao <- which(fac >= pos)[1]
  #calcular a mediana
  li_me <- lim_inf[posicao]
  h <- lim_sup[posicao] - lim_inf[posicao]
  soma_ant <- fac[posicao - 1]
  
  mediana <- li_me + ((pos - soma_ant) / fi[posicao]) * h
  
  # variancia
  xi2fi <- xifi * xi
  variancia <- (1 / (n - 1)) * (sum(xi2fi) - ((sum(xifi) ^ 2) / n))
  
  # desvio padrao
  desviopadrao <- sqrt(variancia)
  
  # coeficiente de variação
  coef_vari <- desviopadrao / media * 100
  
  #tabela de distribuição de frequencia
  tabela <- cbind(lim_inf, lim_sup, fi, xi, fac)
  
  nomes <- c('média','moda','mediana','variância','desvio padrão','coef. variação')
  resumo_agrupado <- round(c(media, moda, mediana, variancia, desviopadrao, coef_vari), 2)
  
  names(resumo_agrupado) <- nomes
  #resumo_agrupado
  return(list(distribuicao_de_frequencia = tabela, resumo = resumo_agrupado))
}

li <- c(0,4,8,12,16)
ls <- c(4,8,12,16,20)
freq <- c(8,15,24,20,13)

resumo_dados_agrupados(li,ls,freq)
resumo_dados_agrupados(lim_inf = li,lim_sup = ls, fi = freq)
resumo_dados_agrupados(ls,li,freq)
resumo_dados_agrupados(fi = freq,lim_sup = ls,lim_inf = li)
