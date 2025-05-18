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