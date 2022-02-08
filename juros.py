from capitalizacao import Simples, Composto
import numpy as np

'''
Exemplo 01: juros simples
'''

s = Simples()

capital = 100.0
taxa = 10/100    # 10% a.a
periodo = 5.0    # 5 anos

juros = s.juros(capital, taxa, periodo)
print(juros)

montante = s.montante(capital, taxa, periodo)
print(montante)

taxa = s.taxa_pelo_juros(juros, capital, periodo)
print(taxa * 100)

taxa = s.taxa_pelo_montante(montante, capital, periodo)
print(taxa * 100)

periodo = s.periodo_pelo_juros(juros, capital, taxa)
print(periodo)

periodo = s.periodo_pelo_montante(montante, capital, taxa)
print(periodo)

capital = s.capital_pelo_juros(juros, taxa, periodo)
print(capital)

capital = s.capital_pelo_montante(montante, taxa, periodo)
print(capital)


'''
Exemplo 02: juros composto
'''

c = Composto()



capital = 1000.0
taxa = 10/100    # 10% a.a
periodo = 4.0    # 4 anos

juros = c.juros(capital, taxa, periodo)
print(juros)

montante = c.montante(capital, taxa, periodo)
print(montante)

taxa = c.taxa_pelo_juros(juros, capital, periodo)
print(taxa * 100)

taxa = c.taxa_pelo_montante(montante, capital, periodo)
print(taxa * 100)

periodo = c.periodo_pelo_juros(juros, capital, taxa)
print(periodo)

periodo = c.periodo_pelo_montante(montante, capital, taxa)
print(periodo)

capital = c.capital_pelo_juros(juros, taxa, periodo)
print(capital)

capital = c.capital_pelo_montante(montante, taxa, periodo)
print(capital)


'''
Exemplo 03: juros composto
'''

capital = 100.0
taxa = 10/100    # 10% a.a
periodo = 5.0    # 5 anos

juros = c.juros(capital, taxa, periodo)
print(juros)

montante = c.montante(capital, taxa, periodo)
print(montante)

taxa = c.taxa_pelo_juros(juros, capital, periodo)
print(taxa * 100)

taxa = c.taxa_pelo_montante(montante, capital, periodo)
print(taxa * 100)

periodo = c.periodo_pelo_juros(juros, capital, taxa)
print(periodo)

periodo = c.periodo_pelo_montante(montante, capital, taxa)
print(periodo)

capital = c.capital_pelo_juros(juros, taxa, periodo)
print(capital)

capital = c.capital_pelo_montante(montante, taxa, periodo)
print(capital)

'''
Exemplo 04: juros composto
'''

capital = 1000.0
taxa = 4/100     # 4% a.a
periodo = 3.0    # 3 anos

juros = c.juros(capital, taxa, periodo)
print(juros)

montante = c.montante(capital, taxa, periodo)
print(montante)

taxa = c.taxa_pelo_juros(juros, capital, periodo)
print(taxa * 100)

taxa = c.taxa_pelo_montante(montante, capital, periodo)
print(taxa * 100)

periodo = c.periodo_pelo_juros(juros, capital, taxa)
print(periodo)

periodo = c.periodo_pelo_montante(montante, capital, taxa)
print(periodo)

capital = c.capital_pelo_juros(juros, taxa, periodo)
print(capital)

capital = c.capital_pelo_montante(montante, taxa, periodo)
print(capital)


'''
Exemplo 05: juros composto
'''

capital = 50_000

taxas = np.array([1.25, 0.80, 0.90, 1.70]) / 100

montante = c.montante_para_taxas_acumuladas(capital, taxas)
print(montante)

