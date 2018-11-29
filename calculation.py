import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from data.data import frqSemiFar, frqSemiFar, frqBlindFar, pkBlindFar
# camara1 = pd.read_csv("TEST-COMBO-FAR.csv",delimiter=',')
# camara2 = pd.read_csv("TEST-COMBO-CLOSE.csv",delimiter=',')
# pk1 = (camara1['PEAK AMPL']).values
# pk2 = (camara2['PEAK AMPL']).values
# qp1 = (camara1['QPD AMPL']).values
# qp2 = (camara2['QPD AMPL']).values
# avg1 = (camara1['EAVG AMPL']).values
# avg2 = (camara2['EAVG AMPL']).values
# frq1 = (camara1['FREQ']/1000000).values
# frq2 = (camara2['FREQ']/1000000).values

#Espacio lineal
xp = np.linspace(30, 300, 2700)
# interpolPk1 = interp1d(frq1, pk1)
# interpolPk2 = interp1d(frq2, pk2)
interpolPk1 = interp1d(frqSemiFar, pkSemiFar)
interpolPk2 = interp1d(frqBlindFar, pkBlindFar)

bsPk = interpolPk1(xp) - interpolPk2(xp)
sbPk = interpolPk2(xp) - interpolPk1(xp)
#para calcular las compensaciónes reales
compensacionBSPk = interp1d(xp, bsPk)
compensacionSBPk = interp1d(xp, sbPk)

def EvaluarBS(Freq=[],Pk=[],Qp=[],Av=[]):
    freq = np.array(Freq)
    pk = np.array(Pk)
    qp = np.array(Qp)
    av=np.array(Av)
    # compensacion = (compensacionBS(freq)).tolist()
    compensacionPk = (compensacionBSPk(freq)).tolist()
    return compensacionPk

def PromedioSim(Frq=[], Pk=[]):
    total = np.sum(interpolPk1(Frq))
    val = np.sum(Pk)
    promedio = (100-np.absolute(((total-val)/total)*100))
    return promedio
