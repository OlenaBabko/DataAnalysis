import matplotlib.pyplot as pl
import numpy as np


A = np.loadtxt('data.csv', delimiter = ',', skiprows = 1)            # if needed add: ", skiprows = 1"
x = A[:, 0]
y1 = A[:, 1]
y2 = A[:, 2]
pl.plot(x, y1)
pl.plot(x, y2)


pl.show()
