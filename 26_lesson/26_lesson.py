import matplotlib.pyplot as pl
import numpy as np
from matplotlib import rcParams
import matplotlib.colors as colors


rcParams['axes.labelsize'] = '7'
rcParams['axes.titlesize'] = '7'
rcParams['font.size'] = '7'
rcParams['xtick.labelsize'] = '7'
rcParams['ytick.labelsize'] = '7'
rcParams['axes.linewidth'] = '0.5'
rcParams['xtick.major.width'] = '0.5'
rcParams['ytick.major.width'] = '0.5'
rcParams['xtick.major.size'] = '3'
rcParams['ytick.major.size'] = '3'
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'

rcParams['font.sans-serif'] = 'Arial'
rcParams['mathtext.fontset'] = 'custom'
rcParams['mathtext.rm'] = 'serif'

rcParams['pdf.fonttype'] = '42'

fig = pl.figure(figsize = (2, 1.8), dpi = 150)

# DATA:
A = np.loadtxt('data.txt', delimiter = None)
x = A[:, 0]
y = A[:, 1]

pl.plot(x, y, color = 'brown', lw = 1, alpha = 0.7, label = '$T$=20mK')
pl.ylabel('Current (nA)', labelpad = -1)
pl.xlabel('Voltage (V)', labelpad = 0)
pl.axvline(x = -0.83, color = 'gray', lw = 10, alpha = 0.3)
pl.legend(loc = 'upper right', fontsize = 6, frameon = False)

#pl.savefig('26_lesson_figure.pdf', bbox_inches = 'tight', transparent = True)
pl.savefig('26_lesson_figure.tiff', bbox_inches = 'tight', transparent = True, dpi = 600)
pl.show()
