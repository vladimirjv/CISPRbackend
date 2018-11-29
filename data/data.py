import numpy as np
import pandas as pd

camaraSemiFar = pd.read_csv("SemiFar.csv", delimiter=',')
camaraSemiClose = pd.read_csv("SemiClose.csv", delimiter=',')
camaraSemiMiddle = pd.read_csv("SemiMiddle.csv", delimiter=',')

camaraBlindFar = pd.read_csv("SemiFar.csv", delimiter=',')

'''
Todos los datos están medidos en dBuV

Los valores de Pico (Pk) medidos estaran en "pk[camara][posición]"
Los valores de Quasi-Pico (Qp) estarán en las variables "qp[cámara][posición]" 
Los valores de Average (Avg) estarán en  las variables "avg[cámara][posición]"

La frecuencia estará dada en MHz y será guardada en las variables "frq[cámara][posición]"
'''
##Camara semianecoica
#Far
pkSemiFar = (camaraSemiFar['PEAK AMPL']).values
qpSemiFar = (camaraSemiFar['QPD AMPL']).values
avgSemiFar = (camaraSemiFar['EAVG AMPL']).values
frqSemiFar = (camaraSemiFar['FREQ']/1000000).values
#Middle
pkSemiMiddle = (camaraSemiMiddle['PEAK AMPL']).values
qpSemiMiddle = (camaraSemiMiddle['QPD AMPL']).values
avgSemiMiddle = (camaraSemiMiddle['EAVG AMPL']).values
frqSemiMiddle = (camaraSemiMiddle['FREQ']/1000000).values
#Close
pkSemiClose = (camaraSemiClose['PEAK AMPL']).values
qpSemiClose = (camaraSemiClose['QPD AMPL']).values
avgSemiClose = (camaraSemiClose['EAVG AMPL']).values
frqSemiClose = (camaraSemiClose['FREQ']/1000000).values

##Camara bindada
#Far
pkBlindFar = (camaraBlindFar['PEAK AMPL']).values
qpBlindFar = (camaraBlindFar['QPD AMPL']).values
avgBlindFar = (camaraBlindFar['EAVG AMPL']).values
frqBlindFar = (camaraBlindFar['FREQ']/1000000).values
#Middle
#Close
print(pkBlindFar)