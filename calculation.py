import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

camara1 = pd.read_csv("TEST-COMBO-FAR.csv",delimiter=',')
camara2 = pd.read_csv("TEST-COMBO-CLOSE.csv",delimiter=',')

pk1 = (camara1['PEAK AMPL']).values
pk2 = (camara2['PEAK AMPL']).values

qp1 = (camara1['QPD AMPL']).values
qp2 = (camara2['QPD AMPL']).values

avg1 = (camara1['EAVG AMPL']).values
avg2 = (camara2['EAVG AMPL']).values

frq1 = camara1['FREQ']/1000000
frq2 = camara2['FREQ']/1000000

x1 = frq1.values
x2 = frq2.values

xp = np.linspace(30, 300, 2700)

interpol1 = interp1d(x1, pk1)
interpol2 = interp1d(x2, pk2)

bs = interpol1(xp) - interpol2(xp)
sb = interpol2(xp) - interpol1(xp)
#para calcular las compensaciónes reales
compensacionBS = interp1d(xp, bs)
compensacionSB = interp1d(xp, sb)

datosAevaluar = [30, 79, 98, 133, 189, 205, 256, 279, 284]
valores = [15, 14, 13, 12, 13, 16, 17, 12, 14]
datosAevaluar = np.array(datosAevaluar)
valores = np.array(valores)
#BS=(compensacionBS(datosAevaluar)).tolist()
BS = compensacionBS(datosAevaluar)
