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
