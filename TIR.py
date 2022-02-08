import numpy as np
from capitalizacao import Indicadores

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
print(tir_A)

tir_B = i.taxa_interna_de_retorno(cf_B)
print(tir_B)