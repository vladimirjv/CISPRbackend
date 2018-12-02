import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from dataBinding import Data
data=Data()

#Espacio lineal
xp = np.linspace(30, 300, 2700)

#datos camara semianecoica
pkSemiFar, qpSemiFar, avgSemiFar, frqSemiFar = data.SemiFarData()
pkSemiMiddle, qpSemiMiddle, avgSemiMiddle, frqSemiMiddle = data.SemiMiddleData()
pkSemiClose, qpSemiClose, avgSemiClose, frqSemiClose = data.SemiCloseData()
#datos camara blindada
pkBlindFar, qpBlindFar, avgBlindFar, frqBlindFar = data.BlindFarData()

interpolPkSemiFar = interp1d(frqSemiFar, pkSemiFar)
interpolQpSemiFar = interp1d(frqSemiFar, qpSemiFar)
interpolAvgSemiFar = interp1d(frqSemiFar, avgSemiFar)
interpolPkSemiMiddle = interp1d(frqSemiMiddle, pkSemiMiddle)
interpolQpSemiMiddle = interp1d(frqSemiMiddle, qpSemiMiddle)
interpolAvgSemiMiddle = interp1d(frqSemiMiddle, avgSemiMiddle)
interpolPkSemiClose = interp1d(frqSemiClose, pkSemiClose)
interpolQpSemiClose = interp1d(frqSemiClose, qpSemiClose)
interpolAvgSemiClose = interp1d(frqSemiClose, avgSemiClose)

interpolPkBlindFar = interp1d(frqBlindFar, pkBlindFar)
interpolQpBlindFar = interp1d(frqBlindFar, qpBlindFar)
interpolAvgBlindFar = interp1d(frqBlindFar, avgBlindFar)

# bsPk = interpolPkSemiFar(xp) - interpolPkBlindFar(xp)
# sbPk = interpolPkBlindFar(xp) - interpolPkSemiFar(xp)
#para calcular las compensaciónes reales
# compensacionBSPk = interp1d(xp, bsPk)
# compensacionSBPk = interp1d(xp, sbPk)

# def EvaluarBS(Freq=[],Pk=[],Qp=[],Av=[]):
#     freq = np.array(Freq)
#     pk = np.array(Pk)
#     qp = np.array(Qp)
#     av=np.array(Av)
#     # compensacion = (compensacionBS(freq)).tolist()
#     compensacionPk = (compensacionBSPk(freq)).tolist()
#     return compensacionPk

def PromedioSim(Frq=[], Pk=[]):
    total = np.sum(interpolPkSemiFar(Frq))
    val = np.sum(Pk)
    promedio = (100-np.absolute(((total-val)/total)*100))
    return promedio

def ObtenerPkSemiFar(Frq=[]):
    Frq=np.array(Frq)
    return interpolPkSemiFar(Frq)
def ObtenerQpSemiFar(Frq=[]):
    Frq = np.array(Frq)
    return interpolQpSemiFar(Frq)
def ObtenerAvgSemiFar(Frq=[]):
    Frq = np.array(Frq)
    return interpolAvgSemiFar(Frq)
def ObtenerPkSemiMiddle(Frq=[]):
    Frq = np.array(Frq)
    return interpolPkSemiMiddle(Frq)
def ObtenerQpSemiMiddle(Frq=[]):
    Frq = np.array(Frq)
    return interpolQpSemiMiddle(Frq)
def ObtenerAvgSemiMiddle(Frq=[]):
    Frq = np.array(Frq)
    return interpolAvgSemiMiddle(Frq)
def ObtenerPkSemiClose(Frq=[]):
    Frq = np.array(Frq)
    return interpolPkSemiClose(Frq)
def ObtenerQpSemiClose(Frq=[]):
    Frq = np.array(Frq)
    return interpolQpSemiClose(Frq)
def ObtenerAvgSemiClose(Frq=[]):
    Frq = np.array(Frq)
    return interpolAvgSemiClose(Frq)


def ObtenerPkSemiFar(Frq=[]):
    Frq = np.array(Frq)
    return interpolPkSemiFar(Frq)
def ObtenerQpSemiFar(Frq=[]):
    Frq = np.array(Frq)
    return interpolQpSemiFar(Frq)
def ObtenerAvgSemiFar(Frq=[]):
    Frq = np.array(Frq)
    return interpolAvgSemiFar(Frq)

def Test(Frq=[], Pk=[]):
    return 1
