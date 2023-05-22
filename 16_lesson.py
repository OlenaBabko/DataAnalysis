import matplotlib.pyplot as pl
import numpy as np


x = np.linspace(0, 10, 101)
y1 = np.sin(x)
y2 = np.sin(x) + x**2


'''pl.plot(x, y1)
pl.plot(x, y2)'''

fig, ax1 = pl.subplots()
ax1.plot(x, y1, lw = 3, color = 'red')
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y1')

# 2nd axes on same x axis:
ax2 = ax1.twinx()
ax2.plot(x, y2, lw = 3, color = 'blue')
ax2.set_ylabel('y2')



pl.show()
