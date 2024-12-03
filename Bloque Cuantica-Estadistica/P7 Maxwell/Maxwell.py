# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scis
import Herramientas as herr
import scipy.integrate as scint
def Maxwell(v,C1,C2):
    return  C1*v**2*np.exp(-C2*v**2)

plt.close("all")
y = 0.08 # m
g = 9.81 # m/s^2
d = 0.01 # m. Abertura de las celdas
kT = 6.5313E-4 # Obtenido de vm = sqrt(2kT/m)

N = 508
x = np.arange(0.01,0.24,d)
v = x*np.sqrt(g/(2*y))
vm = 0.313
m = 0.6/45
DN  = 90
Dvm = np.sqrt(g/(2*y)) * 0.01 # 0.01 es el delta x  

C1 = 4*np.pi*(m/(2*np.pi*kT))**(3/2)
C2 = m/(2*kT)

C1exp = 4/np.sqrt(np.pi)*N/vm**3 # La que hace que coincida el maximo
C1exp2 =  DN* np.exp(1)/(vm**2*Dvm)
C2exp = 1/vm**2

fig, ax = herr.BasicCanvas("Distribucion Maxwell kT = {} J; m = {} g".format(kT, round(m,4)), "v (m/s)", "P(v)")
ax.plot(v, Maxwell(v,C1,C2), color = "red", linestyle = "dashed")
#ax.plot(v, Maxwell(v,C1exp2,C2exp))
fig.show()


#%% Calculando al integral con C1exp y viendo que no da Ne
Int, err = scint.quad(Maxwell,0,np.inf,args= (C1exp2,C2exp))

