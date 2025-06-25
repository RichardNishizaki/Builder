from EmAprovacao import EmAprovacao
from EstadoOrcamento import EstadoOrcamento
import classItem


class Orcamento(EstadoOrcamento):
    def __init__(self,valor):
        self.itens = []
        self.valor = valor
        self.estadoatual = EmAprovacao()
    
    def add_itens(self, nome, valor):
        self.itens.append(classItem.item(nome, valor))

    def obter_itens(self):
        return self.itens
    
    def aplica_desconto_extra(self):
        self.estadoatual.aplica_desconto_extra(self)

    def aprova(self,orcamento):
        self.estadoatual.aprova(orcamento)

    def reprova(self,orcamneto):
        self.estadoatual.reprova(orcamneto)

    def finaliza(self,Orcamento):
        self.estadoatual.finaliza(Orcamento)
