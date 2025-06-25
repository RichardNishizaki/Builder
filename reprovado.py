from EstadoOrcamento import EstadoOrcamento

class reprovado(EstadoOrcamento):
    
    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orçamentos reprovados não recebem desconto extra!")
