import numpy as np
from capitalizacao import Indicadores

i = Indicadores()

'''
Exemplo 1:
'''
cf_A = np.array([-5000.00, 4500.00, 0.00, 500.00, 200.00, 100.00])
cf_B = np.array([-5000.00, 0.00, 1000.00, 3000.00, 4000.00, 7000.00])

pb_A = i.payback(cf_A)
print("PayBack(A) =  {} anos.".format(pb_A))

pb_B = i.payback((cf_B))
print("PayBack(B) =  {} anos.".format(pb_B))

'''
Exemplo 2: Dados dois projetos A e B com o fluxo de caixa descrito na tabela abaixo, 
calcule o período de Payback para ambos os projetos. Por esse método qual 
seria o projeto escolhido?
'''
cf_A = np.array([-200, 70, 85, 76])
cf_B = np.array([-150, 50, 110, 30])

pb_A = i.payback(cf_A)
print("PayBack(A) =  {} anos.".format(pb_A))

pb_B = i.payback((cf_B))
print("PayBack(B) =  {} anos.".format(pb_B))

'''
Exemplo 3: Dados dois projetos A e B com o fluxo de caixa descrito na 
tabela abaixo, calcule o período de Payback para ambos os projetos. 
Por esse método, qual seria o projeto escolhido?
'''
print('\n')
cf_A = np.array([-100, 60, 42, 36])
cf_B = np.array([-100, 40, 46, 60])

pb_A = i.payback(cf_A)
print("PayBack(A) =  {} anos.".format(pb_A))

pb_B = i.payback((cf_B))
print("PayBack(B) =  {} anos.".format(pb_B))

