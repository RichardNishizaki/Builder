from finalizado import finalizado

class aprovado():
    
    def aplica_desconto_extra(self, orcamento):
        orcamento.valor -= orcamento.valor * 0.02
    
    def aprova(self, orcamento):
        raise Exception("Orçamento já está em estado de aprovação")
    
    def reprova(self, orcamento):
        raise Exception("Orçamento está em estado de aprovação e não pode ser reprovado")
    
    def finaliza(self, orcamento):
        orcamento.estadoatual = finalizado()
