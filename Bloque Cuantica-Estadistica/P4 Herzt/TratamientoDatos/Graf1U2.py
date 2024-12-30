# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import os as os
import scipy as sci
plt.rcParams.update({'font.size': 15})
"""
Parte A: HG VARIANDO UH
"""

def BuscadorMinimos(data, startIndex = 0, required_width = 0):
    
    yCortado = data[1][startIndex:]
    xCortado = data[0][startIndex:]

    indexMinimos = sci.signal.find_peaks(-yCortado,distance = 120,width = required_width)[0]
    minimos = np.zeros(len(indexMinimos))
    minDiff = np.zeros(len(indexMinimos)-1)
    posMinimos = np.zeros(len(indexMinimos))
    for i in range(len(indexMinimos)):
        posMinimos[i] = xCortado[indexMinimos[i]]
        minimos[i] = yCortado[indexMinimos[i]]
        if i != 0: minDiff[i-1] = posMinimos[i]-posMinimos[i-1]
    return minimos,posMinimos        
plt.close("all")
#%% Llamada a los datos
#%%% Parte 1.1: Determinar delta U1 para distintos U2
pth = "P1/U/"
ListP2U = np.array(os.listdir(pth))
U2_15 = herr.TTD(pth  + ListP2U[0])
U2_1 = herr.TTD(pth  + ListP2U[1])
U2_2 = herr.TTD(pth  + ListP2U[2])

errV = 0.01 # V, error de medida
errMin = 0.005 # V, error de determinacion de minimos (se ha visto con un promedio
              # de cuanto se separan algunos minimos numericos de lo que nosotros determinariamos visualmente)
errI = 0.01 # nA
#%% Buscando minimos
# Suavizado
window_length = 50
polyorder = 1
U2_1[1] = herr.savgol_filter(U2_1[1], window_length, polyorder)
U2_15[1] = herr.savgol_filter(U2_15[1], window_length, polyorder)
U2_2[1] = herr.savgol_filter(U2_2[1], window_length, polyorder)

minU21, posMinU21, diffMin1 = herr.BuscadorMinimos(U2_1, minimun_height = (-50,-0.5)) 
minU215, posMinU215,diffMin15 = herr.BuscadorMinimos(U2_15, minimun_height = (-50,-0.5))
minU22, posMinU22,diffMin2 = herr.BuscadorMinimos(U2_2, minimun_height=(-50,-0.5)) 

# Diferencia Minimos para U2 = 2 V
errDiffMin = np.ones(len(diffMin2))*(errV + errMin) * 2 # Prop. errores. se suman y se multiplica por dos por restar dos variables con mismo error
# Obtenemos tambien la diferencia promedio (Ea)
Ea = np.mean(diffMin2[1:-1])
epsiEa = np.sqrt(np.std(diffMin2[1:-1])**2 + np.mean(errDiffMin)**2)
print("Energia de salto promedio: {} +- {}".format(Ea,epsiEa))

#%% Calculo de errores

#%% Graficas
#%%% U265 # r"$U_2 = 1\ V$"
fig1,ax1 = herr.BasicCanvas(r"$U_2 = 1.5\ V$","U1 (V)", "I (nA)")
ax1.plot(U2_15[0],U2_15[1])
ax1.scatter(posMinU215,minU215, s= 8, color = "red")
fig1.show()


#%%% U268
fig2,ax2 = herr.BasicCanvas(r"$U_2 = 1\ V$","U1 (V)", "I (nA)")
ax2.plot(U2_1[0],U2_1[1])
ax2.scatter(posMinU21,minU21, s = 8, color = "red")
fig2.show()

#%%% U271
fig3,ax3 = herr.BasicCanvas(r"$U_2 = 2\ V$","U1 (V)", "Intensidad (nA)")
ax3.plot(U2_2[0],U2_2[1])
ax3.scatter(posMinU22,minU22, s = 8, color = "red")
fig3.show()


#%%% Umin(n)
n = np.arange(1,len(posMinU22)+1, 1)
p, cov = np.polyfit(n,posMinU22, 1,cov = True)
errs = np.sqrt(np.diag(cov))
chi = sci.stats.chisquare(np.polyval(p,n), posMinU22) [1] # Esto es chi cuadrado
fig,ax = herr.BasicCanvas(r"Posición de los mínimos para $U_2 = 2\ V$", "n",r"$U (eV)$")
ax.scatter(n,posMinU22,s = 15)
ax.errorbar(n,posMinU22,errMin, fmt = "none", capsize = 12)
lineName =  r"$U(n) = ({} \pm {})n + ({} \pm {}) $".format(round(p[0],2), round(errs[0],3),round(p[1],2),round(errs[1],2))
ax.plot(n, np.polyval(p, n), c = "red", linestyle = "dashed", label =lineName)
ax.plot(n[0],posMinU22[0], label = r"$R^2 = {}$".format(round(chi,5)))
ax.legend()
fig.show()
#%%% Un -U(n-1)
"""
fig4,ax4 = herr.BasicCanvas("Distancia entre mínimos según el nivel energético", "n", r"$\Delta U(n)$ (eV)")
n = np.arange(0,len(minDiff),1)
e = 1.6 *10 **(-19) # Carga del electron. Para tener la pendiente en julios

minDiffe = minDiff # Si quieres llevarlo a julios, mete aqui un e
errDiffMine = errDiffMin # idem a la linea de arriba


minDiffe = minDiffe[1:-1] # me quito el ultimo punto
errDiffMine = errDiffMine[1:-1]
n = n[1:-1]

ax4.scatter(n,minDiffe, s = 5)
ax4.errorbar(n,minDiffe,errDiffMine,fmt = "none", capsize = 3 )

# Veamos si cuadra con la linealizacion de la eq 1
p,cov = np.polyfit(n, minDiffe, 1, cov = True)
b = p[0]
a = p[1]
errb = np.sqrt(np.diag(cov))[0]
erra = np.sqrt(np.diag(cov))[1]
chi = sci.stats.chisquare(np.polyval(p,n), minDiffe) [1] 
ax4.plot(n, b*n + a, color = "red", linestyle = "dashed", label = r"$\Delta U = n \cdot E_a$")
ax4.plot(0,0,label = r"$\Delta U = n \cdot ({} \pm {}) + ({} \pm {})$".format(round(b,3),round(errb,2),round(a,2),round(erra,2)), c = "red", linestyle = "dashed")
ax4.plot(0,0,label = r"R^2 = " + str(chi))
ax4.legend(loc = "upper left")
print("E_ajuste (J) =",b,"||| Ea promedio (J) =", Ea, "+-", epsiEa)

"""
"""
# Vamos a meter el modelo teorico de Rubenzah
l= # recorrido libre medio
L= # Distancia entre catodo y rejilla
deltaU = (1+l/L(2*n-1))*4.67 # eV
"""