import matplotlib.pyplot as plt
import numpy as np

Thetai = [10,14,20,24,30,34,40,44,50,54,60,64,70,74,78]
ThetaiRad = []
for i in Thetai:
    ThetaiRad.append(np.deg2rad(i))
Ir = [126.9,133.8,148.3,156.3,183.9,195.6,257.7,277.1,377,461,633,783,1111,1413,1619]
Ifondo = [8.90e-3,7.14e-3,18e-3,14.8e-3,15e-3,14.6e-3,10.2e-3,9.9e-3,10e-3,10.1e-3,15e-3,17.9e-3,23.4e-3,25e-3,25.8e-3]
Ii = [4200,4200,4200,4200,4090,4090,4090,4050,4050,4050,4050,4050,4050,4070,4070]

IrPrima = []
for i in range(len(Ir)):
    IrPrima.append(Ir[i]-Ifondo[i])
    
Rexp = [] #reflectancia experimental
for i in range(len(IrPrima)):
    Rexp.append(IrPrima[i]/Ii[i])
   
SumaR = 0    
for i in Rexp:
    SumaR += i

print('Rexp = {}'.format(SumaR/15))

Thetat = []
for i in ThetaiRad:
    Thetat.append((1/1.5)*np.sin(i))
    
R = [] #reflectancia teórica
for i in range(len(ThetaiRad)):
    sen1 = np.sin(ThetaiRad[i]-Thetat[i])
    sen2 = np.sin(ThetaiRad[i]+Thetat[i])
    R.append((-sen1/sen2)**2)

#Reflectancia:
plt.figure(figsize=(8, 6))
plt.plot(ThetaiRad, Rexp, marker='o', linestyle='-', color='b', label='Reflectancia experimental')
plt.plot(ThetaiRad, R, marker='o', linestyle='-', color='r', label='Reflectancia teórica')
plt.xlabel('$\Theta$ (rad)')
plt.ylabel('$R_\perp$')
plt.grid(visible=True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.legend(fontsize=12)
plt.show()

Texp = [] #transmitancia experimental
for i in range(len(Rexp)):
    Texp.append(1-Rexp[i])
    
SumaT = 0    
for i in Texp:
    SumaT += i

print('Texp = {}'.format(SumaT/15))

T = [] #transmitancia teórica
for i in range(len(R)):
    T.append(1-R[i])
    
#Transmitancia:
plt.figure(figsize=(8, 6))
plt.plot(ThetaiRad, Texp, marker='o', linestyle='-', color='b', label='Transmitancia experimental')
plt.plot(ThetaiRad, T, marker='o', linestyle='-', color='r', label='Transmitancia teórica')
plt.xlabel('$\Theta$ (rad)')
plt.ylabel('$T_\perp$')
plt.grid(visible=True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.legend(fontsize=12)
plt.show()