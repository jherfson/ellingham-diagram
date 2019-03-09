import matplotlib.pyplot as plt
import numpy as np
from thermodynamics import Thermodynamics


MnO2 = -24.462012063
Mn2O3 = -43.265196185
Mn3O4 = -61.663923343
WO3 = -36.50192121
MnWO4 = -55.191026811
O2 = -9.871055838


chempot = Thermodynamics()

x = np.arange(1351)
y = []
y1 = []
y2 = []
y3 = []
y4 = []

for i in range(273, 1624):
    # 4MnO2 -> 2Mn2O3 + O2 
    z = 2*Mn2O3 + chempot.temperature_to_mu(i) - 4*MnO2
    
    # 6Mn2O3 -> 4Mn3O4 + O2 
    z1 = 4*Mn3O4 + chempot.temperature_to_mu(i) - 6*Mn2O3
    #print(z1)
    #  2MnO2 + 2WO3 -> 2MnWO4 + O2 
    z2 = 2*MnWO4 + chempot.temperature_to_mu(i) - 2*MnO2 - 2*WO3
    
    # 2Mn2O3 + 4WO3 -> 4MnWO4 + O2 
    z3 = 4*MnWO4 + chempot.temperature_to_mu(i) - 2*Mn2O3 - 4*WO3
    
    # 2Mn3O4 + 6WO3 -> 6MnWO4 + O2 
    z4 = 6*MnWO4 + chempot.temperature_to_mu(i) - 2*Mn3O4 - 6*WO3

    y.append(z)
    y1.append(z1)
    y2.append(z2)
    y3.append(z3)
    y4.append(z4)

Xlim, Xman = Xlim = 0, 1350
Ymin, Ymax = Ylim = 0, 2.6

MinorTickSpacing,MajorTickSpacing = 50, 150


TickFontSize = 11

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

XLabel = 'Temperature (°C)'
YLabel = r'$\Delta$G per' + ' O2 '.translate(SUB) +'in Reaction /eV'


fig, ax = plt.subplots(figsize=(6, 6.5), dpi=100)


ax.set(xlim=Xlim, ylim=Ylim, autoscale_on=False)

AxisFontSize = 16
LabelShift = 10
TickFontSize = 11
Transparency = 60


ax.set_xlabel(XLabel, fontsize=AxisFontSize, labelpad = LabelShift)
ax.set_ylabel(YLabel, fontsize=AxisFontSize, labelpad = LabelShift)

ax.xaxis.set_major_locator(plt.MultipleLocator(MajorTickSpacing))
ax.xaxis.set_minor_locator(plt.MultipleLocator(MinorTickSpacing))

ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))


ax.tick_params(axis='both',which='both', direction='in', labelsize=TickFontSize, width=0.8)
ax.tick_params(axis='both',which='minor', length=5)
ax.tick_params(axis='both',which='major', length=5)

X = 30

ax.text(X, y=0.768, s='1', color='silver' )  # 2MnO2 + 2WO3 -> 2MnWO4 + O2
ax.text(X, y=0.91, s='2', color='lightblue') # 4MnO2 -> 2Mn2O3 + O2
ax.text(X, y=1.15, s='3', color='tomato')  # 2MnO2 + 2WO3 -> 2MnWO4 + O2
ax.text(X, y=1.37, s='4', color='lightgreen')   # 2MnO2 + 2WO3 -> 2MnWO4 + O2
ax.text(X, y=2.52, s='5', color='orange')  # 6Mn2O3 -> 4Mn3O4 + O2

ax.plot(x, y, color='lightblue')  # 4MnO2 -> 2Mn2O3 + O2
ax.plot(x, y1, color='orange')    # 6Mn2O3 -> 4Mn3O4 + O2
ax.plot(x, y2, color='tomato')    # 2MnO2 + 2WO3 -> 2MnWO4 + O2
ax.plot(x, y3, color='lightgreen') # 2MnO2 + 2WO3 -> 2MnWO4 + O2
ax.plot(x, y4, color='silver') # 2MnO2 + 2WO3 -> 2MnWO4 + O2

# ax.grid(axis='x', which='minor', alpha=1-Transparency/100)
# x.grid(axis='y', which='minor', alpha=1-Transparency/100)

plt.show()