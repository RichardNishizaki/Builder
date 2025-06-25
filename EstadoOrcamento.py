from abc import ABC, abstractmethod


class EstadoOrcamento(ABC):
    @abstractmethod
    def aplica_desconto_extra(orcamento):
        return

    def aprova(orcamento):
        return

    def reprova(orcamento):
        return

    def finaliza(orcamento):
        return