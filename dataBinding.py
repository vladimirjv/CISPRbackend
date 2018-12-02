import numpy as np
import pandas as pd

# camaraSemiFar = pd.read_csv("SemiFar.csv", delimiter=',')
# camaraSemiClose = pd.read_csv("SemiClose.csv", delimiter=',')
# camaraSemiMiddle = pd.read_csv("SemiMiddle.csv", delimiter=',')
# camaraBlindFar = pd.read_csv("SemiFar.csv", delimiter=',')


class Data():
    '''
    Todos los datos están medidos en dBuV

    Los valores de Pico (Pk) medidos estaran en "pk[camara][posición]"
    Los valores de Quasi-Pico (Qp) estarán en las variables "qp[cámara][posición]" 
    Los valores de Average (Avg) estarán en  las variables "avg[cámara][posición]"

    La frecuencia estará dada en MHz y será guardada en las variables "frq[cámara][posición]"
    '''
    camaraSemiFar = pd.read_csv("data/SemiFar.csv", delimiter=',')
    camaraSemiClose = pd.read_csv("data/SemiClose.csv", delimiter=',')
    camaraSemiMiddle = pd.read_csv("data/SemiMiddle.csv", delimiter=',')
    camaraBlindFar = pd.read_csv("data/SemiFar.csv", delimiter=',')
    ##Camara semianecoica
    #Far

    def SemiFarData(self):
        '''
        return Peak, Quasi-Peak, Average, Frequncy
        '''
        pkSemiFar = (self.camaraSemiFar['PEAK AMPL']).values
        qpSemiFar = (self.camaraSemiFar['QPD AMPL']).values
        avgSemiFar = (self.camaraSemiFar['EAVG AMPL']).values
        frqSemiFar = (self.camaraSemiFar['FREQ']/1000000).values
        return pkSemiFar, qpSemiFar, avgSemiFar, frqSemiFar
    #Middle

    def SemiMiddleData(self):
        '''
        return Peak, Quasi-Peak, Average, Frequncy
        '''
        pkSemiMiddle = (self.camaraSemiMiddle['PEAK AMPL']).values
        qpSemiMiddle = (self.camaraSemiMiddle['QPD AMPL']).values
        avgSemiMiddle = (self.camaraSemiMiddle['EAVG AMPL']).values
        frqSemiMiddle = (self.camaraSemiMiddle['FREQ']/1000000).values
        return pkSemiMiddle, qpSemiMiddle, avgSemiMiddle, frqSemiMiddle
    #Close

    def SemiCloseData(self):
        '''
        return Peak, Quasi-Peak, Average, Frequncy
        '''
        pkSemiClose = (self.camaraSemiClose['PEAK AMPL']).values
        qpSemiClose = (self.camaraSemiClose['QPD AMPL']).values
        avgSemiClose = (self.camaraSemiClose['EAVG AMPL']).values
        frqSemiClose = (self.camaraSemiClose['FREQ']/1000000).values
        return pkSemiClose, qpSemiClose, avgSemiClose, frqSemiClose

    ##Camara bindada
    #Far
    def BlindFarData(self):
        '''
        return Peak, Quasi-Peak, Average, Frequncy
        '''
        pkBlindFar = (self.camaraBlindFar['PEAK AMPL']).values
        qpBlindFar = (self.camaraBlindFar['QPD AMPL']).values
        avgBlindFar = (self.camaraBlindFar['EAVG AMPL']).values
        frqBlindFar = (self.camaraBlindFar['FREQ']/1000000).values
        return pkBlindFar, qpBlindFar, avgBlindFar, frqBlindFar
    #Middle
    #Close
