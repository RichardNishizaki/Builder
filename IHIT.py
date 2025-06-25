from templatedeimpostocondicional import TemplateDeImpostoCondicional

class IHIT(TemplateDeImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        nomes = []
        for item in orcamento.obter_itens():
            if item.nome in nomes:
                return True
            nomes.append(item.nome)
        return False

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.13 + 100.0

    def minima_taxacao(self, orcamento):
        return orcamento.valor * (0.01 * len(orcamento.obter_itens()))

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)