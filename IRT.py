import numpy as np
from capitalizacao import Indicadores

k = 10/100 # 10% a.a

cf_A = np.array([-100, 80, 50, 10])
cf_B = np.array([-100, 10, 10, 130])

i = Indicadores()


irt_A = i.indice_de_rentabilidade(cf_A, k)
print("IRT(A) =  R$ {:.2f}".format(irt_A))


irt_B = i.indice_de_rentabilidade(cf_B, k)
print("IRT(B) =  R$ {:.2f}".format(irt_B))


'''
Sejam dois projetos A e B com o fluxo de caixa descrito na tabela abaixo. 
Dado que o custo de oportunidade para investir nos projetos seja de 10% aa, 
determine o IRT para cada projeto e escolha o melhor
'''

k = 10/100 # 10% a.a

cf_A = np.array([-200, 70, 85, 76])
cf_B = np.array([-150, 50, 110, 30])

i = Indicadores()


irt_A = i.indice_de_rentabilidade(cf_A, k)
print("IRT(A) =  R$ {:.2f}".format(irt_A))


irt_B = i.indice_de_rentabilidade(cf_B, k)
print("IRT(B) =  R$ {:.2f}".format(irt_B))
