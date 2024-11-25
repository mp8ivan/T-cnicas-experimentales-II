import matplotlib.pyplot as plt
import numpy as np

Thetai = [10,20,30,40,50,52,54,56,58,60,62,64,66,68,70,74,78]
ThetaiRad = []
for i in Thetai:
    ThetaiRad.append(np.deg2rad(i))
Ir = [34.6,18.47,15.55,9.22,2.418,1.351,0.847,0.697,1.297,2.885,5.90,10.56,17.87,26.8,40.8,90.9,160.6]
Ifondo = [10.7e-3,10.32e-3,8.3e-3,8.7e-3,9.05e-3,10.1e-3,14.3e-3,11e-3,11e-3,11.97e-3,20.6e-3,21.88e-3,24e-3,180e-3,177.2e-3,32.3e-3,10.9e-3]
Ii = [1202,1202,1202,1202,813,813,813,813,813,813,856,856,856,856,856,856,857]

IrPrima = []
for i in range(len(Ir)):
    IrPrima.append(Ir[i]-Ifondo[i])
    
Rexp = [] #reflectancia experimental
for i in range(len(IrPrima)):
    Rexp.append(IrPrima[i]/Ii[i])
   
SumaR = 0    
for i in Rexp:
    SumaR += i

print('Rexp = {}'.format(SumaR/17))

Thetat = []
for i in ThetaiRad:
    Thetat.append((1/1.5)*np.sin(i))
    
R = [] #reflectancia teórica
for i in range(len(ThetaiRad)):
    tan1 = np.tan(ThetaiRad[i]-Thetat[i])
    tan2 = np.tan(ThetaiRad[i]+Thetat[i])
    R.append((-tan1/tan2)**2)

#Reflectancia:
plt.figure(figsize=(8, 6))
plt.plot(ThetaiRad, Rexp, marker='o', linestyle='None', color='b', label='Reflectancia experimental')
plt.plot(ThetaiRad, R, marker='o', linestyle='None', color='r', label='Reflectancia teórica')
plt.xlabel('$\Theta$ (rad)')
plt.ylabel('$R_\parallel$')
plt.grid(visible=True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.legend(fontsize=12)
plt.show()

Texp = [] #transmitancia experimental
for i in range(len(Rexp)):
    Texp.append(1-Rexp[i])
    
SumaT = 0    
for i in Texp:
    SumaT += i

print('Texp = {}'.format(SumaT/17))

T = [] #transmitancia teórica
for i in range(len(R)):
    T.append(1-R[i])
    
#Transmitancia:
plt.figure(figsize=(8, 6))
plt.plot(ThetaiRad, Texp, marker='o', linestyle='None', color='b', label='Transmitancia experimental')
plt.plot(ThetaiRad, T, marker='o', linestyle='None', color='r', label='Transmitancia teórica')
plt.xlabel('$\Theta$ (rad)')
plt.ylabel('$T_\parallel$')
plt.grid(visible=True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.legend(fontsize=12)
plt.show()