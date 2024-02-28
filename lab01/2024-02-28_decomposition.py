# Esercizio mostrato mercoledì 2024-02-28
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

plt.rcParams['figure.figsize'] = (10.0, 6.0)
df = pd.read_csv('../csv-files/lab-BoxJenkins.csv', usecols=["Passengers"])
ds = df[df.columns[0]]  # converts to series
result = seasonal_decompose(ds, model='multiplicative', period=12)
result.plot()
plt.show()
