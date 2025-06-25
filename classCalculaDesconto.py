import Desconto
import classSemDesconto
import classDescpor5itens
import classDescpormaisde500reais

class calculadesconto():
    def calcula(Orcamento):
          Desconto.d1 = classDescpor5itens.Descpor5itens()
          Desconto.d2 = classDescpormaisde500reais.DescontoPorMaisDeQuinhentosReais()
          Desconto.d3 = classSemDesconto.SemDesconto()

          Desconto.d1.setNext(Desconto.d2)
          Desconto.d2.setNext(Desconto.d3)

          return Desconto.d1.calcula(Orcamento)