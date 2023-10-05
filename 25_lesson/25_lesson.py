import matplotlib.pyplot as pl
import numpy as np
from matplotlib import rcParams


def z_fun(x, y):
    return (1 - (x * 4 + y ** 4)) * np.exp(- (x ** 4 + y ** 4) / 2)

x = np.arange( 0, 2, 0.01)
y = np.arange( 0, 2, 0.01)
X, Y = np.meshgrid(x, y)

pl.rcParams['font.sans-serif'] = 'Arial'
pl.rcParams['font.size'] = '16'

# EVALUATE func z:
Z = z_fun(X, Y)
fig = pl.figure()
ax = fig.add_subplot()
#im = ax.pcolormesh(X, Y, Z, cmap = 'RdBu_r', shading = 'gouraud')
im = ax.pcolormesh(X, Y, Z, cmap = 'seismic', shading = 'gouraud')

#pl.colorbar(im)
pl.title('$\sigma$(mS)')
pl.xlabel('V$_{g}$ (V)')
pl.ylabel('V$_{t}$ (V)')
pl.xticks([0, 0.5, 1, 1.5, 2])
pl.yticks([0, 0.5, 1, 1.5, 2])

cbaxes = fig.add_axes([0.65, 0.9, 0.25, 0.04])
cb = pl.colorbar(im, cax = cbaxes, orientation = 'horizontal', ticks = [-1, 0, 1])
cbaxes.xaxis.tick_top()

pl.show()

# return (1 - (x * 4 + y ** 4)) * np.exp( - (x ** 4 + y ** 4) / 2)