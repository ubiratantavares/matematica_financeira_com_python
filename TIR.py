import numpy as np
from capitalizacao import Indicadores

'''
Exemplo 1
'''

k = 10/100 # 10% a.a
t = 3

cf_A = np.array([-100, 80, 50, 10])
cf_B = np.array([-100, 10, 10, 130])

i = Indicadores()

print('VFL determina o valor em dinheiro, futuro, do ganho ou perda do projeto.')


vfl_A = i.valor_futuro_liquido(cf_A, k, t)
print("VFL = R$ {:.2f}".format(vfl_A))


vfl_B = i.valor_futuro_liquido(cf_B, k, t)
print("VFL = R$ {:.2f}".format(vfl_B))


tir_A = i.taxa_interna_de_retorno(cf_A)
print(tir_A*100)

tir_B = i.taxa_interna_de_retorno(cf_B)
print(tir_B*100)


'''
Exemplo 2: Sejam dois investimentos mutuamente excludentes: 
o primeiro, investir hoje R$ 50.000,00 para resgatar R$ 75.000,00 
no próximo período; e o segundo, investir hoje R$ 200.000,00 e 
resgatar R$ 280.000,00 no final do mesmo período. 
Qual o melhor investimento, dado que você só tem essas duas opções 
de investimentos?

'''
cf_A = np.array([-50_000, 75_000])
cf_B = np.array([-200_000, 280_000])

tir_A = i.taxa_interna_de_retorno(cf_A)
print(tir_A*100)

tir_B = i.taxa_interna_de_retorno(cf_B)
print(tir_B*100)
