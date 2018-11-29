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
frq1 = (camara1['FREQ']/1000000).values
frq2 = (camara2['FREQ']/1000000).values

xp = np.linspace(30, 300, 2700)

interpolPk1 = interp1d(frq1, pk1)
interpolPk2 = interp1d(frq2, pk2)

bsPk = interpolPk1(xp) - interpolPk2(xp)
sbPk = interpolPk2(xp) - interpolPk1(xp)
#para calcular las compensaciónes reales
compensacionBSPk = interp1d(xp, bsPk)
compensacionSBPk = interp1d(xp, sbPk)

# datosAevaluar = [30, 79, 98, 133, 189, 205, 256, 279, 284]
# valores = [15, 14, 13, 12, 13, 16, 17, 12, 14]
# datosAevaluar = np.array(datosAevaluar)
# valores = np.array(valores)
# #BS=(compensacionBS(datosAevaluar)).tolist()
# BS = compensacionBS(datosAevaluar)

def EvaluarBS(Freq=[],Pk=[],Qp=[],Av=[]):
    freq = np.array(Freq)
    pk = np.array(Pk)
    qp = np.array(Qp)
    av=np.array(Av)
    # compensacion = (compensacionBS(freq)).tolist()
    compensacionPk = (compensacionBSPk(freq)).tolist()
    return compensacionPk

