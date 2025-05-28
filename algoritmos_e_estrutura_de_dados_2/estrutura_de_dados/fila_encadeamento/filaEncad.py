class Nodo :
    def __init__(self, dado) :
        self.dado = dado
        self.prox = None

class FilaEncad :
    def __init__ (self) :
        self.ini = None
        self.fim = None

    def consultar(self) :
        if not self.vazia() :
            return self.ini.valor
        
    def inserir (self,dado) :
        novo = Nodo(dado)
        if self.vazia() :
            self.ini = novo
            self.fim = novo
        else :
            self.fim.prox = novo
            self.fim = novo

    def excluir(self) :
        if not self.vazia() :
            self.ini = self.ini.prox
    
    def destruir(self) :
        while not self.vazia() :
            self.excluir()