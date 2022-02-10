from capitalizacao import Simples, Composto


'''
Exemplo 01
'''

s = Simples()


# 1% a.m se capitalizado mês a mês por juros simples é 
# equivalente a qual taxa a.a?

taxa1 = 0.01  # 1% a.m
periodo1 = 12 # 12 meses = 1 ano
periodo2 = 1 # 1 ano
taxa2 = s.taxa_equivalente(taxa1, periodo1, periodo2)
print("{:.4f}% a.a".format(taxa2 * 100))

# qual a taxa mensal equivalente a 9% a.a, 
# considerando capitalização em juros simples?
taxa1 = 9/100 # 9% a.a
periodo1 = 1 # 1 ano
periodo2 = 12 # 12 meses

taxa2 = s.taxa_equivalente(taxa1, periodo1, periodo2)
print("{:.4f}% a.m".format(taxa2 * 100))



'''
Exemplo 02
'''

c = Composto()

# 1% a.m se capitalizado mês a mês por juros compostos é 
# equivalente a qual taxa a.a?

taxa1 = 0.01  # 1% a.m
periodo1 = 12 # 12 meses = 1 ano
periodo2 = 1 # 1 ano
taxa2 = c.taxa_equivalente(taxa1, periodo1, periodo2)
print("{:.4f}% a.a".format(taxa2 * 100))


# qual a taxa mensal equivalente a 9% a.a, 
# considerando capitalização em juros composto?
taxa1 = 9/100 # 9% a.a
periodo1 = 1 # 1 ano
periodo2 = 12 # 12 meses

taxa2 = c.taxa_equivalente(taxa1, periodo1, periodo2)
print("{:.4f}% a.m".format(taxa2 * 100))

'''
Exemplo 03: Quais as taxas diária, mensal, trimestral, semestral, 
anual e a juros compostos que transforma um capital de 
R$ 30.000,00 em R$212.537,21 após dois anos?
'''

capital = 30_000
montante = 212_537.21
periodo_aa = 2 # 2 anos
taxa_aa = c.taxa_pelo_montante(montante, capital, periodo_aa)
print("{:.4f}% a.a".format(taxa_aa * 100))

periodo_aa = 2 
periodo_as = 4 # 2 anos = 4 semestres
taxa_as = c.taxa_equivalente(taxa_aa, periodo_aa, periodo_as)
print("{:.4f}% a.s".format(taxa_as * 100))


periodo_at = 8 # 2 anos = 8 trimestres
taxa_at = c.taxa_equivalente(taxa_aa, periodo_aa, periodo_at)
print("{:.4f}% a.t".format(taxa_at * 100))

periodo_am = 24 # 2 anos = 24 meses
taxa_am = c.taxa_equivalente(taxa_aa, periodo_aa, periodo_am)
print("{:.4f}% a.m".format(taxa_am * 100))

periodo_ad = 2 * 360 # 2 anos = 720 dias
taxa_ad = c.taxa_equivalente(taxa_aa, periodo_aa, periodo_ad)
print("{:.4f}% a.m".format(taxa_ad * 100))

'''
Exemplo 04: Calcule a taxa efetiva anual associada a uma taxa nominal 
de 18% aa com capitalização: mensal, bimestral e semestral. 
'''
taxa = 18/100
periodo_am = 1
periodo_aa = 1/12
tea = c.taxa_equivalente(taxa, periodo_aa, periodo_am)
print("{:.4f}% a.a".format(tea * 100))




