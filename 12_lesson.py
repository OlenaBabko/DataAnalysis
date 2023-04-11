import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-3, 3, 20)
y = np.exp(x)

fig = pl.figure()
pl.plot(x, y, color = 'magenta', linestyle = 'dashed')




pl.xlabel('x-label', fontsize = 14)
pl.ylabel('y-label', fontsize = 14)

pl.title('exponential function', fontsize = 14)
pl.legend(fontsize = 14, frameon = False)

pl.show()

# Create a plot of the exponential function for x in the range -3,3.
# Change the colour to magenta and the line to be dashed