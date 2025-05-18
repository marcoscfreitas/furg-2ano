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
    
    def inverter(self) :
        if self.topo >= self.base :
            temp_pilha = []
            while self.topo >= self.base :
                temp_pilha.append(self.remover())
            for item in temp_pilha :
                self.inserir(item)
            return True
        return False

    def iguais(self, outra_pilha):
        if self.topo != outra_pilha.topo:
            return False
        for i in range(self.topo + 1):
            if self.vetor[i] != outra_pilha.vetor[i]:
                return False
        return True

    def menor(self):
        if self.topo >= self.base:
            menor = self.vetor[self.base]
            for i in range(self.base + 1, self.topo + 1):
                if self.vetor[i] < menor:
                    menor = self.vetor[i]
            return menor
        return None