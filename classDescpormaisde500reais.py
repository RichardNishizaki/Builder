from classOrçamento import Orcamento

class DescontoPorMaisDeQuinhentosReais():
    def calcula(self, Orcamento):
        if( Orcamento.valor > 500 ):
            return Orcamento.valor * 0.07
        
        return self.classe.calcula(Orcamento)
    
    def setNext(self, classe):
        self.classe = classe
