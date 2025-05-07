class Nodo :
    def __init__ (self, v) :
        self.valor = v
        self.prox = None

class ListaEnc :
    def __init__ (self) :
        self.ini = None
        self.fim = None
        self.tam = 0

    def inserir (self, posicao, valor) :
        if posicao >= 0 :
            if self.tam == 0 :
                aux = Nodo(valor)
                self.ini = aux
                self.fim = aux
                self.tam += 1
            elif posicao == self.tam :
                aux = Nodo(valor)
                self.fim.prox = aux
                self.fim = aux
                self.tam += 1
            elif posicao == 0 :
                aux = Nodo(valor)
                aux.prox = self.ini
                self.ini = aux
                self.tam += 1
            else :
                aux = Nodo(valor)
                var = self.ini
                for i in range(posicao) :
                    anterior = var
                    var = var.prox
                aux.prox = var
                anterior.prox = aux
                self.tam += 1

            return True
        else :
            return False

    def imprimir (self) :
        var = self.ini
        while var.prox != None :
            print(var.valor)
            var = var.prox
        if var.prox == None :
            print(var.valor)

    def verificaValor (self, posicao) :
        if posicao <= self.tam :
            cont = 0
            var = self.ini
            if var != None :
                while var.prox != None :
                    if cont == posicao :
                        return var.valor
                    var = var.prox
                    cont += 1
                if var.prox == None :
                    return var.valor

    # def verificaValor (self, valor) :
    #     cont = 0
    #     cont1 = self.tam
    #     var = self.ini
    #     while cont != cont1 :
    #         if var.valor == valor :
    #             return var.posicao

        def remover(self, pos):
        if (pos + 1 <= self.tam and pos >= 0):
            if pos == 0:
                if self.tam == 1:
                    self.fim =  None
                self.ini = self.ini.prox
                else:
                    aux = self.ini
                    for i in range(pos - 1):
                        aux = aux.prox
                    aux.prox = aux.prox.prox
                if pos == self.tam:
                    self.fim = aux
                self.tam -= 1
                return true
        else:
            return false
        
lista = ListaEnc()
lista.inserir(0,'A')
lista.inserir(1,'B')
lista.inserir(2,'C')
lista.inserir(0,'D')
lista.inserir(2,'E')

lista.imprimir()

lista.verificaValor(1)

# print(lista)