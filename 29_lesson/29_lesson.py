import matplotlib.pyplot as pl
import numpy as np


x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

Z = x[None, :] * np.exp(-x[None, :] ** 2 - y[:, None] ** 2)

X, Y = np.meshgrid(x, y)
Z = X * np.exp(-X ** 2 - Y ** 2)

'''pl.contour(X, Y, Z, 50, cmap = 'bwr')                   # 20/ 50
pl.colorbar()'''
# or
'''pl.contourf(X, Y, Z, 50, cmap = 'bwr')
pl.colorbar()'''

# 3D view:
ax = pl.axes(projection = '3d')
ax.plot_surface(X, Y, Z, cmap = 'bwr')


pl.show()
