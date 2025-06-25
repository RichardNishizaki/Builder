from aprovado import aprovado
import reprovado

class EmAprovacao():
    def aplica_desconto_extra(self, orcamento):
        orcamento.valor -= orcamento.valor * 0.05

    def aprova(self, orcamento):
        orcamento.estadoatual = aprovado()

    def reprova(self, orcamento):
        orcamento.estadoatual = reprovado()

    def finaliza(self, orcamento):
        raise Exception("Orcamento em aprovação não podem ir para finalizado diretamente")
