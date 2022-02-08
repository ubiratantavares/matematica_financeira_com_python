'''
Exemplo 01: Dados dois projetos A e B com o fluxo de caixa descrito na tabela 
abaixo, com custo de oportunidade de 10 % a.a, determine o melhor projeto
'''

import numpy as np
from capitalizacao import Indicadores

k = 10/100 # 10% a.a

cf_A = np.array([-100, 80, 50, 10])
cf_B = np.array([-100, 10, 10, 130])


i = Indicadores()

print('VPL determina o valor em dinheiro, hoje, do ganho ou perda do projeto.')

vpl_A = i.valor_presente_liquido(cf_A, k)
print("VPL = R$ {:.2f}".format(vpl_A))


vpl_B = i.valor_presente_liquido(cf_B, k)
print("VPL = R$ {:.2f}".format(vpl_B))


if (vpl_A > 0 and vpl_B > 0):
    print('Os projetos são lucrativos.')
    if (vpl_A > vpl_B):
        print("O projeto A é o melhor projeto e deve ser implementado.")
    else:
        print("O projeto B é o melhor projeto e deve ser implementado.")
        
elif (vpl_A > 0 and vpl_B < 0):
    print("O projeto A é lucrativo e deve ser implementado.")
    
elif (vpl_A < 0 and vpl_B > 0):
    print("O projeto B é lucrativo e deve ser implementado.")   
    
        
cf_AB = cf_A + cf_B


vpl_AB = i.valor_presente_liquido(cf_AB, k)
print("VPL = R$ {:.2f}".format(vpl_AB))


if (vpl_AB > 0):
    print('o projeto é lucrativo e deve ser implementado.')
else:
    print("O projeto gera prejuízo e deve ser descartado.")
    

'''
Exemplo 02: Sejam dois projetos A e B com o fluxo de caixa descrito na tabela abaixo. 
Dado que o custo de oportunidade para investir nos projetos seja de 10% aa, 
determine o VPL para cada projeto e escolha o melhor.
'''


k = 10/100 # 10% a.a

cf_A = np.array([-200, 70, 85, 76])
cf_B = np.array([-150, 50, 110, 30])


i = Indicadores()


vpl_A = i.valor_presente_liquido(cf_A, k)
print("VPL = R$ {:.2f}".format(vpl_A))


vpl_B = i.valor_presente_liquido(cf_B, k)
print("VPL = R$ {:.2f}".format(vpl_B))


if (vpl_A > 0 and vpl_B > 0):
    print('Os projetos são lucrativos.')
    if (vpl_A > vpl_B):
        print("O projeto A é o melhor projeto e deve ser implementado.")
    else:
        print("O projeto B é o melhor projeto e deve ser implementado.")
        
elif (vpl_A > 0 and vpl_B < 0):
    print("O projeto A é lucrativo e deve ser implementado.")
    
elif (vpl_A < 0 and vpl_B > 0):
    print("O projeto B é lucrativo e deve ser implementado.")   
    
'''
Exemplo 03: Um projeto preve um investimento inicial de R$ 70.000,00 e, a partir do 
primeiro ano, possui entradas anuais de caixa no valor de R$ 9.000,00.
Admitindo que o projeto teha uma vida util de 20 anos e um custo de oportunidade
de 11% a.a., faça o DFC do projeto e escreva o cálculo do VPL
'''

k = 11/100 # 11% a.a

cf_inicial = np.array([-70_000])
cf_outros = np.ones(20) * 9000

cf = np.concatenate((cf_inicial, cf_outros))

i = Indicadores()

print('VPL determina o valor em dinheiro, hoje, do ganho ou perda do projeto.')

vpl = i.valor_presente_liquido(cf, k)
print("VPL = R$ {:.2f}".format(vpl))

if (vpl > 0):
    print('o projeto é lucrativo e deve ser implementado.')
else:
    print("O projeto gera prejuízo e deve ser descartado.")
    
'''
Exemplo 04: Um projeto prevê um investimento inicial de R$ 150.000,00 e a partir do 
primeiro ano possui entradas anuais de caixa no valor de R$ 20.000,00. 
Admitindo que o projeto tenha uma vida útil de 20 anos e um custo de 
oportunidade de 10% aa, qual o VPL?
'''

k = 10/100 # 10% a.a

cf_inicial = np.array([-150_000])
cf_outros = np.ones(20) * 20_000

cf = np.concatenate((cf_inicial, cf_outros))

i = Indicadores()

print('VPL determina o valor em dinheiro, hoje, do ganho ou perda do projeto.')

vpl = i.valor_presente_liquido(cf, k)
print("VPL = R$ {:.2f}".format(vpl))

if (vpl > 0):
    print('o projeto é lucrativo e deve ser implementado.')
else:
    print("O projeto gera prejuízo e deve ser descartado.")

