class Nodo :
    def __init__(self, dado) :
        self.dado = dado
        self.prox = None

class pilhaEncad :
    def __init__(self) :
        self.topo = None

    def vazia(self) :
        if self.topo == None :
            return True
        return False

    def inserir(self, dado) :
        novo = Nodo(dado)

        if not self.vazia() :
            novo.prox = self.topo

        self.topo = novo

    def excluir(self) :
        if not self.vazia() :
            self.topo = self.topo.prox

    def consultar(self) :
        if not self.vazia() :
            return self.topo.dado
        else:
            return None
        
    def destruir(self) :
        while not self.vazia() :
            self.excluir()

    def inverter(self) :
        if not self.vazia() :
            anterior = None
            atual = self.topo
            while atual is not None :
                prox_nodo = atual.prox
                atual.prox = anterior
                anterior = atual
                atual = prox_nodo
            self.topo = anterior

    def iguais(self, outra_pilha) :
        atual1 = self.topo
        atual2 = outra_pilha.topo
        while atual1 is not None and atual2 is not None :
            if atual1.dado != atual2.dado :
                return False
            atual1 = atual1.prox
            atual2 = atual2.prox
        return atual1 is None and atual2 is None

    def menor(self) :
        if self.vazia() :
            return None
        atual = self.topo
        menor = atual.dado
        while atual is not None :
            if atual.dado < menor :
                menor = atual.dado
            atual = atual.prox
        return menor