# -*- coding: utf-8 -*-
import Herramientas as herr
import numpy as np
import matplotlib.pyplot as plt

"""
Estudio para tres polarizadores
"""
def PasoAIntensidad(Voltaje):
    R = 10**4
    Amp = 10**2
    return Voltaje/R/Amp *10**6 # Lo devuelve en microAmperios

plt.close("all")

pth = "Data/Tres/"
Data0 = herr.TTD(pth+ "Alf0.txt")
Data30 = herr.TTD(pth + "Alf30.txt")
Data60 = herr.TTD(pth + "Alf60.txt")



A0 = np.array(Data0[0], dtype = float)
V0 = np.array(Data0[1], dtype = float)
I0 = PasoAIntensidad(V0)

A30 = np.array(Data30[0], dtype = float)
V30 = np.array(Data30[1], dtype = float)
I30 = PasoAIntensidad(V30)

A60 = np.array(Data60[0],dtype = float)
V60 = np.array(Data60[1], dtype = float)
I60 = PasoAIntensidad(V60)

errA = np.ones(len(A0))
errI = np.ones(len(V0)) * 0.01 # MicroAmp

#%% Plots

f1,ax1 = herr.BasicCanvas(r"$\alpha = 0 ^\circ$", r"$\alpha$ (grados)", "I (mA)")
f2,ax2 = herr.BasicCanvas(r"$\alpha = 30 ^\circ$", r"$\alpha$ (grados)", "I (mA)")
f3,ax3 = herr.BasicCanvas(r"$\alpha = 60 ^\circ$", r"$\alpha$ (grados)", "I (mA)")

ax1.scatter(A0,I0, s = 8)
ax2.scatter(A30,I30, s = 8)
ax3.scatter(A60,I60,s = 8)

ax1.errorbar(A0,I0,errI,errA, fmt = "none", capsize = 5)
ax2.errorbar(A30,I30,errI,errA, fmt = "none", capsize = 5)
ax3.errorbar(A60,I60,errI,errA, fmt = "none", capsize = 5)

f1.show()
f2.show()
f3.show()



