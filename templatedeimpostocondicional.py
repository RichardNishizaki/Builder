from abc import ABC, abstractmethod

class TemplateDeImpostoCondicional(ABC):
    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass
    
    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass
    
    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass
    
    @abstractmethod
    def calcula(self, orcamento):
        pass
