from carro import *
from listaContig import *

carroA = Carro('AAA123', 2020)
carroB = Carro('BBB456', 2009)
carroC = Carro('CCC789', 1985)

lista = Lista(5)
if (lista.Inserir(1,carroA)) :
    print(lista)
if (lista.Inserir(1,carroB)) :
    print(lista)
if (lista.Inserir(1,carroC)) :
    print(lista)
if (lista.Inserir(1,carroA)) :
    print(lista)
if (lista.Inserir(1,carroB)) :
    print(lista)
if (lista.Inserir(1,carroC)) :
    print(lista)

meuCarro = lista.Consultar(5)
print(meuCarro)