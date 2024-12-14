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

I0Sin = PasoAIntensidad(12.15)
I30Sin = PasoAIntensidad(10.6)
I60Sin = PasoAIntensidad(7)

I0N = I0/I0Sin
I30N = I30/I0Sin
I60N = I60/I60Sin

errI0N = np.ones(len(I0N)) * np.sqrt((errI/I0N)**2 + (errI/I0Sin)**2) * I0N
errI30N = np.ones(len(I0N)) * np.sqrt((errI/I30N)**2 + (errI/I30Sin)**2) *I30N 
errI60N = np.ones(len(I0N)) * np.sqrt((errI/I60N)**2 + (errI/I60Sin)**2) * I60N

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

fig4,ax4 = herr.BasicCanvas("Superposición de los tres ángulos",r"$\alpha$ (grados)", "I (mA)")
ax4.scatter(A0,I0, s = 8, label = r"$\alpha = 0$")
ax4.scatter(A30,I30, s = 8, label = r"$\alpha = 30^\circ$")
ax4.scatter(A60,I60, s = 8, label = r"$\alpha = 60^\circ$")
ax4.legend()
fig4.show()


f5,ax5 = herr.BasicCanvas(r"$\alpha = 0 ^\circ$ (normalizado)", r"$\alpha$ (grados)", r"$I /I_{P1}$")
f6,ax6 = herr.BasicCanvas(r"$\alpha = 30 ^\circ$ (normalizado)", r"$\alpha$ (grados)", r"$I /I_{P1}$")
f7,ax7 = herr.BasicCanvas(r"$\alpha = 60 ^\circ$ (normalizado)", r"$\alpha$ (grados)", r"$I /I_{P1}$")
f8,ax8 = herr.BasicCanvas("Superposición de los tres ángulos (normalizado)",r"$\alpha$ (grados)", r"$I /I_{P1}$")

ax5.scatter(A0,I0N, s = 8)
ax6.scatter(A30,I30N, s = 8)
ax7.scatter(A60,I60N, s = 8)

ax8.scatter(A0,I0N, s = 8, label = r"$\alpha = 0$")
ax8.scatter(A30,I30N, s = 8, label = r"$\alpha = 30^\circ$")
ax8.scatter(A60,I60N, s = 8, label = r"$\alpha = 60^\circ$")

ax5.errorbar(A0,I0N,errI0N, fmt = "none", capsize = 5) # Quito los errores de Alfa porque solo emborronan
ax6.errorbar(A30,I30N,errI30N, fmt = "none", capsize = 5)
ax7.errorbar(A60,I60N,errI60N, fmt = "none", capsize = 5)

ax8.errorbar(A0,I0N,errI0N, fmt = "none", capsize = 3, color = "blue") # Quito los errores de Alfa porque solo emborronan
ax8.errorbar(A30,I30N,errI30N, fmt = "none", capsize = 3, color = "orange")
ax8.errorbar(A60,I60N,errI60N, fmt = "none", capsize = 3, color = "green")
ax8.legend()

f5.show()
f6.show()
f7.show()
f8.show()