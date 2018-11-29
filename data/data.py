import pandas as pd

camaraSemiFar = pd.read_csv("TEST-COMBO-FAR.csv", delimiter=',')
camara2 = pd.read_csv("TEST-COMBO-CLOSE.csv", delimiter=',')
pk1 = (camaraSemiFar['PEAK AMPL']).values
pk2 = (camara2['PEAK AMPL']).values
qp1 = (camaraSemiFar['QPD AMPL']).values
qp2 = (camara2['QPD AMPL']).values
avg1 = (camaraSemiFar['EAVG AMPL']).values
avg2 = (camara2['EAVG AMPL']).values
frq1 = (camaraSemiFar['FREQ']/1000000).values
frq2 = (camara2['FREQ']/1000000).values
