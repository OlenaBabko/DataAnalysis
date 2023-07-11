import matplotlib.pyplot as pl
import numpy as np
import h5py as h5


filename = 'data0.h5'
f = h5.File(filename, 'r')

print(list(f))

xdata = f['x_array'][:]
ydata = f['R2x'][:]

pl.plot(xdata, ydata)

pl.show()
