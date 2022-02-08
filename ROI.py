import numpy as np
from capitalizacao import Indicadores

k = 10/100 # 10% a.a
t = 3

cf_A = np.array([-100, 80, 50, 10])
cf_B = np.array([-100, 10, 10, 130])

i = Indicadores()


roi_A = i.retorno_sobre_investimento(cf_A)
print("ROI(A) =  {:.2f} %".format(roi_A*100))


roi_B = i.retorno_sobre_investimento(cf_B)
print("ROI(B) =  {:.2f} %".format(roi_B*100))