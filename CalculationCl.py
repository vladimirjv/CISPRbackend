import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from dataBinding import Data

#Espacio lineal
class MyMath():

    xp = np.linspace(30, 300, 2700)
    data = Data()
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
