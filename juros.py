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

'''
Exemplo 06: Um ano após de ter adquirido um financiamento num banco, 
Paulo pagou R$ 5.250,00. Sabendo que a taxa de juros do financiamento é 
de 5% aa, qual foi o valor financiado e o valor dos juros pagos por Paulo.
'''

montante = 5250.00
taxa = 5/100 
periodo = 1

capital = c.capital_pelo_montante(montante, taxa, periodo)
juros = c.juros(capital, taxa, periodo)
print(juros)
print(capital)


'''
Exemplo 07: Um banco empresta R$1.000,00 a uma empresa que deverá 
quitar a dívida no valor de R$ 1.100,00 ao fim de 6 meses. 
Calcule o valor dos juros e a taxa de juros desse empréstimo.
'''

capital = 1000.00
montante = 1100.00
periodo = 1 # 1 semestre = 6 meses
taxa = c.taxa_pelo_montante(montante, capital, periodo)
juros = c.juros(capital, taxa, periodo)
print(juros)
print(taxa*100)

'''
Exemplo 08: Um capital de R$10.000,00 é aplicado a uma taxa de 10% 
aa por um período de um ano. Calcule o valor dos juros e o montante 
nesta operação.
'''

capital = 10_000
taxa = 10/100
periodo = 1
juros = c.juros(capital, taxa, periodo)
montante = c.montante(capital, taxa, periodo)
print(juros)
print(montante)

'''
Exemplo 09: Quais as taxas diária, mensal, trimestral, semestral, 
anual e a juros compostos que transforma um capital de 
R$ 30.000,00 em R$212.537,21 após dois anos?
'''
capital = 30_000
montante = 212_537.21
periodo = 2 # a.a
taxa_aa = c.taxa_pelo_montante(montante, capital, periodo)
print(taxa_aa*100)


'''
Exemplo 10: Você investiu R$ 4.500,00 em um fundo de ações que, 
nos últimos meses rendeu lhe 4%, 3%, -5%, 7% e 1%. 
Calcule o valor resgatado.
'''

capital = 4_500.00

taxas = np.array([4, 3, -5, 7, 1]) / 100

montante = c.montante_para_taxas_acumuladas(capital, taxas)
print(montante)

print("\n")

'''
Exemplo 11: estimativa de receita líquida anual no primeiro ano igual a 
R$ 1.000,00 e com um crescimento de 20% aa para os próximos 5 anos, quando as receitas irão se estabilizar
'''
periodo = 5
taxa = 20/100
capital = 1_000.00

print(capital)
for i in range(1, periodo+1):
    print(c.montante(capital, taxa, i))
    
