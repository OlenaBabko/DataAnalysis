import matplotlib.pyplot as pl
import numpy as np


x = np.linspace(0, 2 * np.pi, 10)
y = np.linspace(0, 2 * np.pi, 10)

x, y = np.meshgrid(x, y)
fx, fy = np.sin(x), np.cos(x)

#pl.quiver(x, y, fx, fy, color = 'blue')
pl.streamplot(x, y, fx, fy, color = 'blue', density = 2)


pl.show()
