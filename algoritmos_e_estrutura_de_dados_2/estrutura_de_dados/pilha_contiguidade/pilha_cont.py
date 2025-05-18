class pilhaCont :
    def __init__ (self, tam) :
        self.limite = tam - 1
        self.topo = -1
        self.base = 0
        self.vetor = [None] * tam

    def inserir(self, dado) :
        if self.topo != self.limite :
            self.topo += 1
            self.vetor[self.topo] = dado
            return True
        return False

    def remover(self) :
        if self.topo >= self.base :
            self.vetor[self.topo] = None
            self.topo -= 1
            return True
        return False
    
    def consultar(self):
        if self.topo >= self.base:
            return self.vetor[self.topo]
        return False

    def destruir(self):
        self.topo = -1
        self.vetor = None
        self.limite = 0