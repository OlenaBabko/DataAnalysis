import matplotlib.pyplot as pl
import numpy as np
from matplotlib import rcParams

x = np.linspace(0, 10, 101)
y = np.sin(x)
y1 = np.cos(x)

pl.rcParams['font.sans-serif'] = 'Arial'

pl.plot(x, y, lw = 4, color = 'red', label ='data', alpha = 0.6)
pl.plot(x, y1, lw = 4, color = 'blue', label ='data1', alpha = 0.6)

pl.xlabel(r'$\theta$', fontsize = 14)
pl.ylabel('y-label', fontsize = 14)

pl.xticks(fontsize = 14)
pl.yticks(fontsize = 14)

pl.xlim(0, 8)
pl.ylim(0, 1)

pl.xticks([0, 2, 4, 6, 8])

pl.tick_params(axis = 'x', which = 'major', size = 10, width = 1, direction = 'in')
pl.tick_params(axis = 'y', which = 'major', size = 10, width = 1, direction = 'in')


pl.title('test figure', fontsize = 14)
pl.legend(fontsize = 14, frameon = False)

#pl.savefig('13_lesson.png', bbox_inches = 'tight', transparent = True, dpi = 400)          # or .jpg
pl.savefig('13_lesson.pdf', bbox_inches = 'tight', transparent = True)                      # or .svg
pl.show()
