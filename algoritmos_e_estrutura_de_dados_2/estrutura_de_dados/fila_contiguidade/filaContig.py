class pilhaCont :
    def __init__ (self, tam) :
        self.vetor = [None] * tam
        self.li = 0
        self.ls = tam - 1
        self.ini = self.li - 1
        self.fim = self.ls + 1
    
    def vazia(self) :
        return self.ini < self.li and self.fim > self.ls
    
    def cheia(self) :
        return self.ini == self.li and self.fim == self.ls or self.fim == self.ini - 1
    
    def destruir(self) :
        self.ini = self.li - 1
        self.fim = self.ls + 1

    def consultar(self) :
        if not self.vazia() :
            return self.vetor[self.ini]
    
    def inserir(self,valor) :
        if self.cheia() :
            return False
        else :
            if self.vazia() :
                self.ini = self.li
                self.fim = self.li
                self.vetor[self.ini] = valor
            elif not self.cheia() :
                if self.fim == self.ls :
                    self.fim = self.li
                    self.vetor[self.fim] = valor
                else :
                    self.fim+=1
                    self.vetor[self.fim] = valor
                return True
    
    def excluir(self) :
        if self.vazia():
            return False
        else :
            if not self.vazia() :
                if self.ini > self.fim and self.ini == self.ls :
                    self.vetor[self.ini] = None
                    self.ini = self.li
                elif self.ini == self.fim :
                    self.destruir()
                else :
                    self.vetor[self.ini] = None
                    self.ini+=1