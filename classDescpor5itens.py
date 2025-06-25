from classOrçamento import Orcamento

class Descpor5itens():
    def calcula(self, Orcamento):
        
        if ( len(Orcamento.itens) > 5 ):
            return Orcamento.valor * 0.1
        
        return self.classe.calcula(Orcamento)
    
    def setNext(self, classe):
        self.classe = classe