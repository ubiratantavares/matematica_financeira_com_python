from capitalizacao import TaxasDeMercado

'''
Exemplo 01
'''

# Exemplo: DI 9% a.a.
# Calcule o equivalente de 105% DI

taxa_anual = 9/100 # 9% a.a
percentual_di = 105/100 # 105% DI
periodo_dias = 252
tm = TaxasDeMercado()

taxa_anual = tm.percentual_DI_ano(taxa_anual, percentual_di)
print(taxa_anual)
print("Taxa base ao ano: {:.5f} %".format(taxa_anual*100))


'''
Exemplo 02: uma empresa emitiu R$ 150 milhoes em debentures ao custo de 104,1 %
CDI. Considerando que, no primeiro ano, o CDI medio foi r de 15 % a.a., determine
o saldo da dÃ­vida apos 156 dias uteis.
'''

from capitalizacao import TaxasDeMercado, Composto

taxa_anual = 15/100  # 15% a.a CDI mÃ©dio
percentual_di = 104.1/100 # 104.1% CDI

tm = TaxasDeMercado()
c = Composto()

taxa_dia = tm.percentual_DI_dia(taxa_anual, percentual_di)
periodo_dias_uteis = 156
capital = 150_000_000

montante = c.montante(capital, taxa_dia, periodo_dias_uteis)

print("Saldo da dÃ­vida {:.2f}".format(montante))



