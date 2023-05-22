import matplotlib.pyplot as pl
import numpy as np


x = np.linspace(0, 10, 101)
y = np.sin(x)
y1 = np.cos(x)

fig, ax = pl.subplots(nrows = 2)
#fig, ax = pl.subplots(ncols = 2)
#fig, ax = pl.subplots(nrows = 2, ncols = 2)

ax[0].plot(x, y, color = 'red', label = 'sin(x)')
ax[0].legend()
ax[1].plot(x, y1, color = 'blue', label = 'cos(x)')
ax[1].legend()

pl.tight_layout()


pl.show()
