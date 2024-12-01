# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scis
import Herramientas as herr
def Maxwell(v,C1,C2):
    return  C1*v**2*np.exp(-C2*v**2)

plt.close("all")
y = 0.08 # m
g = 9.81 # m/s^2
d = 0.01 # m. Abertura de las celdas
kT = 0.005 # No queda claro como determinarla para que coincida el maximo con la de la practica

x = np.arange(0,0.24,d)
v = x*np.sqrt(g/(2*y))
m = 1.8/46


C1 = 4*np.pi*(m/(2*np.pi*kT))**(3/2)
C2 = m/(2*kT)

C1exp = 31891.235 # La que hace que coincida el maximo
C1exp2 = 37386.581 # La que impone normalizacion
C2exp = 10.207

fig, ax = herr.BasicCanvas("Distribucion Maxwell kT = {}".format(kT), "v (m/s)", "P(v)")
ax.plot(v, Maxwell(v,C1,C2), color = "red", linestyle = "dashed")
ax.plot(v, Maxwell(v,C1exp,C2exp))
fig.show()


