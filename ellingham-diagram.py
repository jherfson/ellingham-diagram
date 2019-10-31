import matplotlib.pyplot as plt
import numpy as np
from thermodynamics import Thermodynamics
import math


MnO2 = -24.462012063
Mn2O3 = -43.265196185
Mn3O4 = -61.663923343
WO3 = -36.50192121
MnWO4 = -55.191026811
O2 = -9.871055838


chempot = Thermodynamics()
#  Reaction

x = np.arange(1351)
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

for i in range(273, 1624):
    # 4MnO2 -> 2Mn2O3 + O2 
    z1 = 2*Mn2O3 + chempot.temperature_to_mu(i) + chempot.kB*i*math.log(1/0.21) - 4*MnO2
    
    # 6Mn2O3 -> 4Mn3O4 + O2 
    z2 = 4*Mn3O4 + chempot.temperature_to_mu(i) + chempot.kB*i*math.log(1/0.21)- 6*Mn2O3
    #print(z1)
    #  2MnO2 + 2WO3 -> 2MnWO4 + O2 
    z3 = 2*MnWO4 + chempot.temperature_to_mu(i) + chempot.kB*i*math.log(1/0.21) - 2*MnO2 - 2*WO3
    
    # 2Mn2O3 + 4WO3 -> 4MnWO4 + O2 
    z4 = 4*MnWO4 + chempot.temperature_to_mu(i) + chempot.kB*i*math.log(1/0.21) - 2*Mn2O3 - 4*WO3
    
    # 2Mn3O4 + 6WO3 -> 6MnWO4 + O2 
    z5 = 6*MnWO4 + chempot.temperature_to_mu(i) + chempot.kB*i*math.log(1/0.21) - 2*Mn3O4 - 6*WO3

    y1.append(z1)
    y2.append(z2)
    y3.append(z3)
    y4.append(z4)
    y5.append(z5)

Xlim, Xman = Xlim = 0, 1350
Ymin, Ymax = Ylim = 0, 3.0

MinorTickSpacing,MajorTickSpacing = 50, 150


TickFontSize = 20

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

XLabel = 'Temperature (°C)'
YLabel = r'$\Delta$G per' + ' O2 '.translate(SUB) +'in Reaction (eV)'


#  pressures ATM

p1 = []
p2 = []
p3 = []
p4 = []
p5 = []


for j in range(273, 1624):
    #  pressure 0.01 atm
    pressure1 = -chempot.kB*j*math.log(1e-2/1)
    p1.append(pressure1)

    #  pressure 0.0001
    pressure2 = -chempot.kB*j*math.log(1e-4/1)
    p2.append(pressure2)

    #  pressure 0.000001
    pressure3 = -chempot.kB*j*math.log(1e-6/1)
    p3.append(pressure3)

    # presssure 0.00000001
    pressure4 = -chempot.kB*j*math.log(1e-8/1)
    p4.append(pressure4)

    pressure5 = -chempot.kB*j*math.log(0.21/1)
    p5.append(pressure5)

#  plot

fig, ax = plt.subplots(figsize=(8, 6), dpi=100)


ax.set(xlim=Xlim, ylim=Ylim, autoscale_on=False)

AxisFontSize = 20
LabelShift = 15
TickFontSize = 15
Transparency = 60


ax.set_xlabel(XLabel, fontsize=AxisFontSize, labelpad = LabelShift)
ax.set_ylabel(YLabel, fontsize=AxisFontSize, labelpad = LabelShift)

ax.xaxis.set_major_locator(plt.MultipleLocator(MajorTickSpacing))
ax.xaxis.set_minor_locator(plt.MultipleLocator(MinorTickSpacing))

ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))


ax.tick_params(axis='both',which='both', direction='in', labelsize=TickFontSize, width=0.8)
ax.tick_params(axis='both',which='minor', length=5, labelsize=TickFontSize)
ax.tick_params(axis='both',which='major', length=5, labelsize=TickFontSize)


X = 25
Y = 16

ax.text(X, y=0.565, s='1', color='blue', fontsize=Y, weight='bold')    # 2Mn3O4 + 6WO3 -> 6MnWO4 + O2
ax.text(X, y=0.92, s='2', color='red', fontsize=Y, weight='bold')  # 4MnO2 -> 2Mn2O3 + O2
ax.text(X, y=1.15, s='3', color='tomato', fontsize=Y, weight='bold')     # 2MnO2 + 2WO3 -> 2MnWO4 + O2
ax.text(X, y=1.38, s='4', color='lightgreen', fontsize=Y, weight='bold') # 2Mn2O3 + 4WO3 -> 4MnWO4 + O2
ax.text(X, y=2.29, s='5', color='orange', fontsize=Y, weight='bold')     # 6Mn2O3 -> 4Mn3O4 + O2


# reaction
lw = 2
ax.plot(x, y1, color='lightblue', lw=lw)  # 4MnO2 -> 2Mn2O3 + O2
ax.plot(x, y2, color='orange', lw=lw)     # 6Mn2O3 -> 4Mn3O4 + O2
ax.plot(x, y3, color='tomato', lw=lw)     # 2MnO2 + 2WO3 -> 2MnWO4 + O2
ax.plot(x, y4, color='lightgreen', lw=lw) # 2Mn2O3 + 4WO3 -> 4MnWO4 + O2
ax.plot(x, y5, color='silver', lw=lw)     # 2Mn3O4 + 6WO3 -> 6MnWO4 + O2 


# pressure
X1 = 1000
Y1 = 18
ax.text(1010, y=0.27 ,  s='0.21 atm',  rotation=5, fontsize=Y1)
ax.text(X1, y=0.65, s='10⁻² atm', rotation=7, fontsize=Y1)
ax.text(X1, y=1.23,  s='10⁻⁴ atm',  rotation=15, fontsize=Y1)
ax.text(X1, y=1.85,  s='10⁻⁶ atm',  rotation=25, fontsize=Y1)
ax.text(X1, y=2.47 ,  s='10⁻⁸ atm',  rotation=30, fontsize=Y1)


lw2 = 0.5
ax.plot(x, p1, '--', color='black', lw=lw2)
ax.plot(x, p2, '--', color='black', lw=lw2)
ax.plot(x, p3, '--', color='black', lw=lw2)
ax.plot(x, p4, '--', color='black', lw=lw2)
ax.plot(x, p5, '--', color='black', lw=lw2)


plt.show()
