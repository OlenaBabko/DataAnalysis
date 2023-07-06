import matplotlib.pyplot as pl
import numpy as np
import scipy.io


A = scipy.io.loadmat('data.mat')
xdata = A['gateVoltages']
ydata = A['scans']

np.shape(xdata)
np.shape(ydata)

pl.plot(np.transpose(xdata), np.transpose(ydata))

pl.show()
