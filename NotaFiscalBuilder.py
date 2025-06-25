from datetime import datetime
from typing import List


class ItemDaNota:
    def __init__(self, nome: str, valor: float):
        self.Nome = nome
        self.Valor = valor
        
class NotaFiscal:
    def __init__(self, razao_social: str, cnpj: str, data: datetime, valor_total: float, impostos: float, observacoes: str, todos_itens: List[ItemDaNota]):
        self.RazaoSocial = razao_social
        self.Cnpj = cnpj
        self.Data = data
        self.ValorTotal = valor_total
        self.Impostos = impostos
        self.Observacoes = observacoes
        self.TodosItens = todos_itens

    def __str__(self):
        return f"Empresa: {self.RazaoSocial}\nCNPJ: {self.Cnpj}\nData: {self.Data}\nValor total R${self.ValorTotal}\nImpostos R${self.Impostos}\nObservações: {self.Observacoes}\nItens: {[f'{item.Nome}: {item.Valor}' for item in self.TodosItens]}"

class NotaFiscalBuilder:
    def __init__(self):
        self._razao_social = None
        self._cnpj = None
        self._valor_total = 0.0
        self._impostos = 0.0
        self._data = None
        self._observacoes = ""
        self._todos_itens: List[ItemDaNota] = []
        
    def ParaEmpresa(self, razao_social: str) -> 'NotaFiscalBuilder':
        self._razao_social = razao_social
        return self
    
    def ComCnpj(self, cnpj: str) -> 'NotaFiscalBuilder':
        self._cnpj = cnpj
        return self
    
    def ComItem(self, item: ItemDaNota) -> 'NotaFiscalBuilder':
        self._todos_itens.append(item)
        self._valor_total += item.Valor
        self._impostos += item.Valor * 0.05
        return self
    
    def NaDataAtual(self) -> 'NotaFiscalBuilder':
        self._data = datetime.now()
        return self
    
    def ComObservacoes(self, observacoes: str) -> 'NotaFiscalBuilder':
        self._observacoes = observacoes
        return self
    
    def Constroi(self) -> NotaFiscal:
        return NotaFiscal(
            razao_social=self._razao_social,
            cnpj=self._cnpj,
            data=self._data,
            valor_total=self._valor_total,
            impostos=self._impostos,
            observacoes=self._observacoes,
            todos_itens=self._todos_itens
        )