import numpy as np
from capitalizacao import Indicadores

k = 10/100 # 10% a.a

cf_A = np.array([-5000.00, 4500.00, 0.00, 500.00, 200.00, 100.00])
cf_B = np.array([-5000.00, 0.00, 1000.00, 3000.00, 4000.00, 7000.00])

i = Indicadores()


pb_A = i.payback(cf_A)
print("PayBack(A) =  {} anos.".format(pb_A))


pb_B = i.payback((cf_B))
print("PayBack(B) =  {} anos.".format(pb_B))

'''
Dados dois projetos A e B com o fluxo de caixa descrito na tabela abaixo, 
calcule o período de Payback para ambos os projetos. Por esse método qual 
seria o projeto escolhido?
'''

k = 10/100 # 10% a.a

cf_A = np.array([-200, 70, 85, 76])
cf_B = np.array([-150, 50, 110, 30])

i = Indicadores()


pb_A = i.payback(cf_A)
print("PayBack(A) =  {} anos.".format(pb_A))


pb_B = i.payback((cf_B))
print("PayBack(B) =  {} anos.".format(pb_B))


