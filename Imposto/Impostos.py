from abc import ABC, abstractmethod #import

class Impostos(ABC):
    @abstractmethod
    def __init__(self, outroImposto):
        self.outroImposto = outroImposto

    @abstractmethod
    def CalculoDoOutroImposto(self, orcamen):
        if self.outroImposto == None:
            return 0
        return self.outroImposto.calcula_imposto(orcamen)

    @abstractmethod
    def calcula_imposto(self, orcamen):
        pass