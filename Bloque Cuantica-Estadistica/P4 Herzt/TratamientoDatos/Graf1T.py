# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import os as os
import scipy as sci
plt.rcParams.update({'font.size': 22})
"""
Parte A: HG VARIANDO T
"""
plt.close("all")
#%% Llamada a los datos
pth = "P1/T/"
ListP2U = np.array(os.listdir(pth))

DataList = []
minList = []
minPos = []
minDiff = []
for i in range(len(ListP2U)):
    DataList.append( herr.TTD(pth  + ListP2U[i]))
    # Suavizamos las 
    window_length = 100
    polyorder = 1
    DataList[i][1] = herr.savgol_filter(DataList[i][1], window_length, polyorder) # Para imprecisiones
    # Buscando minimos
    auxMin, auxPosMin, aux = herr.BuscadorMinimos(DataList[i], 200, -50, minimun_height=(-45,-0.5)) #-45 y -1 para controlar las rectas inciales y finales
    minList.append(auxMin)
    minPos.append(auxPosMin)
    minDiff.append(aux)


#%% Diferencia de minimos
"""
minDiff = []
for i in range(len(ListP2U)):
    aux = []
    for j in range(1,len(minList[i])): # Voy por cada diferencia
        aux.append(minPos[i][j]-minPos[i][j-1])
    minDiff.append(aux)
"""
#%% Graficas

for i in range(len(ListP2U)):
    fig1,ax1 = herr.BasicCanvas(ListP2U[i],"U1 (V)", "I (nA)")
    ax1.plot(DataList[i][0],DataList[i][1])
    ax1.scatter(minPos[i],minList[i], s = 8, color = "red")
    fig1.show()
"""
for i in range(len(ListP2U)):        # lo mismo para diferencias 
    fig1,ax1 = herr.BasicCanvas(ListP2U[i] + r": $\Delta U_{min}$","\Delta U_{min} (V)", "")
    ax1.scatter(np.arange(0,len(minDiff[i][1:]),1),minDiff[i][1:]) # Me cargo siempre la primera diferencia
    fig1.show()
"""

toInforme = True
t = 0
start= 1
end = 0
n = np.arange(start,len(minDiff[t]))
minDiff[t] = minDiff[t][start:]
p, cov = np.polyfit(n, minDiff[t], 1, cov = True)
covDiag = np.sqrt(np.diag(cov))
errm = covDiag[1]
errn = covDiag[0]
minDiffMean = np.mean(minDiff[t])
minDiffstd = np.std(minDiff[t])
print (minDiffMean,minDiffstd)
# chi = np.sum((np.polyval(p, n) - minDiff[t])**2) # Esto por alguna razon no va
chi = sci.stats.chisquare(np.polyval(p,n), minDiff[t]) [1] # Esto es chi cuadrado
if toInforme:
    fig1,ax1 = herr.BasicCanvas(r"$\Delta U_1{_{min}}(n), T = 145^\circ$", "n",r"$\Delta U_{min}$ (eV)") ##
else:
    fig1,ax1 = herr.BasicCanvas(ListP2U[t], "n",r"$\Delta U_{min}$ (eV)") ##r"$\Delta U (n)$ para $ T = 145^\circ$"
ax1.scatter(n,minDiff[t], s = 8)
ax1.plot(n, np.polyval(p, n), linestyle = "dashed", color = "red", label = r"$\Delta U = ({} \pm {}) n + ({} \pm {}) $".format(round(p[1],3), round(errm,3),round(p[0],3), round(errn,3)))
ax1.plot(n[0],minDiff[t][0], label = r"R^2 = {}".format(round(chi,10)))
ax1.errorbar(n,minDiff[t],np.ones(len(minDiff[t]))*0.01,fmt = "none", capsize = 5)
ax1.legend()
fig1.show()

"""
T = np.arange(145,180,5)
Eajuste = np.array([2.44,2.435,2.445, 2.4695,2.43, 2.445,2.41])
epsiEa = np.array([0.13,0.10,0.03,0.012,0.13,0.03,0.04])
fig2, ax2 = herr.BasicCanvas(r"$\Delta U (1/2)$ para distintas temperaturas", "T (grados)", r"$\Delta U$")
ax2.plot(T, np.ones(len(T))*37644.978 * 1.24 * 10**(-4), color = "red", linestyle = "dashed", label = r"$E_t = 4.668\ eV$") # del handbook de 
ax2.scatter(T,Eajuste, s = 8)
ax2.errorbar(T,Eajuste,epsiEa, fmt = "none", capsize = 5)
fig2.legend()
fig2.show()
"""
T = np.arange(145,180,5)
"""
# Finalmente, grafica de U3-U2(T)
secMinT = np.array([4.73,4.76,4.76,4.75,4.72,4.79,4.67]) # Se calculan a mano porque es mas trabajoso el codigo con deteccion de minimos (nos ayudamos con el visualmente)
# media = np.mean(secMinT)
fig2, ax2 = herr.BasicCanvas(r"$\Delta U_{3,2} (T)$","T (grados)",r"$\Delta U_{3,2}\ (eV)$")

ax2.scatter(T, secMinT, s = 8)
ax2.errorbar(T,secMinT, np.ones(len(secMinT))*0.04, fmt = "none", capsize = 3 )
ax2.set_ylim(4.5,5)
"""
#Calculado U3-U2 numericamente (mejorado por svgol)
DeltaU32 = np.zeros(len(T))

for i in range(len(T)):
    DeltaU32[i] = minDiff[i][1]
    
f4, ax4 = herr.BasicCanvas(r"$\Delta U_{3,2} (T) (Automatico)$","T (grados)",r"$\Delta U_{3,2}\ (eV)$")
ax4.scatter(T, DeltaU32, s = 8)
ax4.errorbar(T,DeltaU32, np.ones(len(T))*0.02, fmt = "none", capsize = 3 )
#ax4.set_ylim(4.5,5)
f4.show()    

# Vamos a obtener l(T)

Ea = 4.668 # eV
l = (DeltaU32-Ea)/(3*Ea)
errsecMin = np.ones(len(DeltaU32))*0.02
fig3, ax3 = herr.BasicCanvas(r"Cálculo de $\frac{l}{L}$",r"$\Delta U_{3,2}$", "l/L" )
ax3.scatter(T, l, s = 18)
ax3.errorbar(T, l, errsecMin/(3*Ea), fmt = "none", capsize = 2 )  # Error calculado por propagacion de errores
# ax3.set_ylim(4.5,5)
