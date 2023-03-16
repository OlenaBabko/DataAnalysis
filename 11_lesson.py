import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(0, 10, 101)
y = np.sin(x)
y1 = np.cos(x)

fig = pl.figure(figsize = (6, 4))
pl.plot(x, y, lw = 4, color = 'red', label ='data')
pl.plot(x, y1, lw = 4, color = 'blue', label ='data1')

pl.xlabel(r'$\theta$', fontsize = 14)
pl.ylabel('y-label', fontsize = 14)

pl.xticks(fontsize = 14)
pl.yticks(fontsize = 14)

pl.xlim(0, 8)
#pl.ylim(0, 1)

pl.xticks([0, 2, 4, 6, 8])

pl.title('test figure', fontsize = 14)
pl.legend(fontsize = 14, frameon = False)

pl.show()
