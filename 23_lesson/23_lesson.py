import matplotlib.pyplot as pl
import numpy as np
import pandas as pnd

df = pnd.read_csv('data1.csv')
print(df)

x = df['data_x']
y = df['data_y']

pl.plot(x, y)


pl.show()
