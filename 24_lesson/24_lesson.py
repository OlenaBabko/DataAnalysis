import matplotlib.pyplot as pl
import numpy as np


def z_fun(x, y):
    return (1 - (x * 4 + y ** 4)) * np.exp(- (x ** 4 + y ** 4) / 2)

x = np.arange( 0, 2, 0.01)
y = np.arange( 0, 2, 0.01)
X, Y = np.meshgrid(x, y)

# EVALUATE func z:
Z = z_fun(X, Y)
fig = pl.figure()
ax = fig.add_subplot()
im = ax.pcolormesh(X, Y, Z, cmap = 'RdBu_r', shading = 'gouraud')

pl.colorbar(im)

pl.show()

# return (1 - (x * 4 + y ** 4)) * np.exp( - (x ** 4 + y ** 4) / 2)