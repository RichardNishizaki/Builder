# from IHIT import IHIT
# import classCalculaDesconto
#from Imposto.classCOFINS import COFINS
#from Imposto.classICMS import ICMS

from NotaFiscalBuilder import NotaFiscalBuilder, ItemDaNota
import classOrçamento

orcamen = classOrçamento.Orcamento(500.00)

nf = NotaFiscalBuilder() \
        .ParaEmpresa("Trevo Ltda") \
        .ComCnpj("728.546.219/0001-10") \
        .ComItem(ItemDaNota("Iphone R$",3000.00)) \
        .ComItem(ItemDaNota("Macbook R$",7000.00)) \
        .ComItem(ItemDaNota("AirPods R$",600.00)) \
        .ComObservacoes("Entregar Nota Fiscal pessoalmente") \
        .NaDataAtual() \
        .Constroi()

print(str(nf))

######################################################################
# orcamen.add_itens('iPhone 1', 100)
# orcamen.add_itens('iPhone 2', 200)
# orcamen.add_itens('iPhone 3', 300)

# ihit = IHIT()
# print('Imposto sem itens iguais R$',ihit.calcula(orcamen))

# orcamen.add_itens('iPhone 1', 100)
# orcamen.add_itens('iPhone 2', 200)
# orcamen.add_itens('iPhone 2', 300)

# igual = IHIT()
# print('Imposto com itens iguais R$',igual.calcula(orcamen))


########################################################################
# orcamen.aplica_desconto_extra()
# print(orcamen.valor)
# orcamen.aprova(orcamen)
# orcamen.aplica_desconto_extra()
# print(orcamen.valor)
# orcamen.finaliza(orcamen)

#########################################################################
# impostoComplexo = ICMS(COFINS(None))
# print('Imposto Total = ',impostoComplexo.calcula_imposto(orcamen))
########################################################################

# orcamen.add_itens('iPhone 1', 100)
# orcamen.add_itens('iPhone 2', 200)
# orcamen.add_itens('iPhone 3', 300)
# orcamen.add_itens('iPhone 4', 400)
# orcamen.add_itens('iPhone 5', 500)
# # orcamen.add_itens('iPhone 6', 600)

# desconto = classCalculaDesconto.calculadesconto.calcula(orcamen)
# print(f"O Desconto é de: {desconto:.2f}")