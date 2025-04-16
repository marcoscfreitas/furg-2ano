class Lista :
    def __init__ (self,max) :
        self.max = max
        self.vetor = [None] * self.max
        self.ini = None
        self.fim = None
    
    def __repr__ (self) :
        string = '[ini '
        for i in range(self.ini, self.fim+1) :
            string = string + ' --> ' + str(self.vetor[i])
        return string + ']'

    def Vazia (self) :
        return self.ini == None or self.fim == None

    def Limpar (self) :
        self.ini = None
        self.fim = None

    def Excluir (self) :
        return 0
    
    def Tamanho (self) :
        if self.Vazia() :
            return 0 
        else :
            return self.fim - self.ini + 1

    def encontraValor (self, posicao) :
        if not self.Vazia() and posicao < self.Tamanho() and posicao >= 0 :
            return self.vetor[self.ini + posicao]

    def encontraPosicao(self,valor) :
        for i in range(self.ini, self.fim + 1) :
            if valor == self.vetor[i]
                return i - self.ini
        return None
        
    def Inserir (self, posicao, valor) :
        #verificar se existe espaço e se a posição é valida
        if (self.ini != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.Tamanho() :
            if (self.Vazia()) :
                self.ini = 0
                self.fim = 0
            elif (self.fim != self.max - 1) : # se tem espaço, deslocar para o fim
                for i in range(self.fim, self.ini + posicao - 2, -1) :
                    self.vetor[i+1] = self.vetor[i]
                    print('moveu')
                self.fim = self.fim + 1
            else : # deslocar para o inicio
                for i in range(self.ini, self.ini + posicao) :
                    self.vetor[i-1] = self.vetor[i]
                    print('moveu')
                self.ini = self.ini - 1
            self.vetor[self.ini + posicao] = valor
            return True
        else :
            return False


    def inserirAlt(self, pos, valor) :
        if pos >= 0 and pos <= self.Tamanho() and self.Tamanho() < self.max
            if self.Vazia() : # se a lista for vazia, insere no meio
                self.ini = self.max//2
                self.fim = self.max//2
                self.vetor[self.ini] = valor
            elif pos == 0 and self.ini != 0 : # 
                self.ini = self.ini - 1
                self.vetor[self.ini] = valor
            elif pos == self.Tamanho() and self.fim != max - 1 # 
                self.fim = self.fim + 1
                self.vetor[self.fim] = valor
            elif self.fim == max - 1 : # 
                for i in range(self.ini, self.ini + pos) :
                    self.vetor[i] = self.vetor[i+1]
                self.vetor[self.ini+pos] = valor
            else : #
                self.fim = self.fim + 1
                for i in range(self.fim, self.ini + pos) : 
                    vetor[i] = self.vetor[i-1]
                self.vetor[self.ini+pos] = valor




        return False