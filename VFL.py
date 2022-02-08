import numpy as np
from capitalizacao import Indicadores

k = 10/100 # 10% a.a
t = 3

cf_A = np.array([-100, 80, 50, 10])
cf_B = np.array([-100, 10, 10, 130])

i = Indicadores()

print('VFL determina o valor em dinheiro, futuro, do ganho ou perda do projeto.')


vfl_A = i.valor_futuro_liquido(cf_A, k, t)
print("VFL(A) = R$ {:.2f}".format(vfl_A))


vfl_B = i.valor_futuro_liquido(cf_B, k, t)
print("VFL(B) = R$ {:.2f}".format(vfl_B))


if (vfl_A > 0 and vfl_B > 0):
    print('Os projetos são lucrativos.')
    if (vfl_A > vfl_B):
        print("O projeto A é o melhor projeto e deve ser implementado.")
    else:
        print("O projeto B é o melhor projeto e deve ser implementado.")
        
elif (vfl_A > 0 and vfl_B < 0):
    print("O projeto A é lucrativo e deve ser implementado.")
    
elif (vfl_A < 0 and vfl_B > 0):
    print("O projeto B é lucrativo e deve ser implementado.")   
    
cf_AB = cf_A + cf_B

vfl_AB = i.valor_futuro_liquido(cf_AB, k, t)
print("VPL = R$ {:.2f}".format(vfl_AB))


if (vfl_AB > 0):
    print('o projeto é lucrativo e deve ser implementado.')
else:
    print("O projeto gera prejuízo e deve ser descartado.")


k = 5/100 # 5% a.a.


vfl_A = i.valor_futuro_liquido(cf_A, k, t)
print("VFL(A) = R$ {:.2f}".format(vfl_A))


vfl_B = i.valor_futuro_liquido(cf_B, k, t)
print("VFL(B) = R$ {:.2f}".format(vfl_B))


if (vfl_A > 0 and vfl_B > 0):
    print('Os projetos são lucrativos.')
    if (vfl_A > vfl_B):
        print("O projeto A é o melhor projeto e deve ser implementado.")
    else:
        print("O projeto B é o melhor projeto e deve ser implementado.")
        
elif (vfl_A > 0 and vfl_B < 0):
    print("O projeto A é lucrativo e deve ser implementado.")
    
elif (vfl_A < 0 and vfl_B > 0):
    print("O projeto B é lucrativo e deve ser implementado.")   
    
cf_AB = cf_A + cf_B

vfl_AB = i.valor_futuro_liquido(cf_AB, k, t)
print("VPL = R$ {:.2f}".format(vfl_AB))


if (vfl_AB > 0):
    print('o projeto é lucrativo e deve ser implementado.')
else:
    print("O projeto gera prejuízo e deve ser descartado.")
   
    
k = 10/100 # 10% a.a
t = 2

cf_A = np.array([-100, 80, 50, 10])
cf_B = np.array([-100, 10, 10, 130])

i = Indicadores()

print('VFL determina o valor em dinheiro, futuro, do ganho ou perda do projeto.')


vfl_A = i.valor_futuro_liquido(cf_A, k, t)
print("VFL(A) = R$ {:.2f}".format(vfl_A))


vfl_B = i.valor_futuro_liquido(cf_B, k, t)
print("VFL(B) = R$ {:.2f}".format(vfl_B))


if (vfl_A > 0 and vfl_B > 0):
    print('Os projetos são lucrativos.')
    if (vfl_A > vfl_B):
        print("O projeto A é o melhor projeto e deve ser implementado.")
    else:
        print("O projeto B é o melhor projeto e deve ser implementado.")
        
elif (vfl_A > 0 and vfl_B < 0):
    print("O projeto A é lucrativo e deve ser implementado.")
    
elif (vfl_A < 0 and vfl_B > 0):
    print("O projeto B é lucrativo e deve ser implementado.")   
    
cf_AB = cf_A + cf_B

vfl_AB = i.valor_futuro_liquido(cf_AB, k, t)
print("VPL = R$ {:.2f}".format(vfl_AB))


if (vfl_AB > 0):
    print('o projeto é lucrativo e deve ser implementado.')
else:
    print("O projeto gera prejuízo e deve ser descartado.")
    
    
'''
Sejam dois projetos A e B com o fluxo de caixa descrito na tabela abaixo. 
Dado que o custo de oportunidade para investir nos projetos seja de 10% aa, 
determine o VFL em t = 3 para cada projeto e escolha o melhor.
'''

k = 10/100 # 10% a.a
t = 3

cf_A = np.array([-200, 70, 85, 76])
cf_B = np.array([-150, 50, 110, 30])

i = Indicadores()

print('VFL determina o valor em dinheiro, futuro, do ganho ou perda do projeto.')


vfl_A = i.valor_futuro_liquido(cf_A, k, t)
print("VFL(A) = R$ {:.2f}".format(vfl_A))


vfl_B = i.valor_futuro_liquido(cf_B, k, t)
print("VFL(B) = R$ {:.2f}".format(vfl_B))


if (vfl_A > 0 and vfl_B > 0):
    print('Os projetos são lucrativos.')
    if (vfl_A > vfl_B):
        print("O projeto A é o melhor projeto e deve ser implementado.")
    else:
        print("O projeto B é o melhor projeto e deve ser implementado.")
        
elif (vfl_A > 0 and vfl_B < 0):
    print("O projeto A é lucrativo e deve ser implementado.")
    
elif (vfl_A < 0 and vfl_B > 0):
    print("O projeto B é lucrativo e deve ser implementado.")   
