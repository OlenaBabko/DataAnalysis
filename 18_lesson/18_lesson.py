import matplotlib.pyplot as pl
import numpy as np


A = np.loadtxt('data.txt', delimiter = None)            # if needed add: ", skiprows = 1"
x = A[:, 0]
y = A[:, 1]
pl.plot(x, y, lw = 2, color = 'blue')
pl.xlabel('Gate Voltage (V)')
pl.ylabel('Resistance (k$\Omega$)')


pl.show()
