import matplotlib.pyplot as pl
import numpy as np
import matplotlib.image as mpimg


x = np.linspace(0, 10, 101)
y = np.sin(x)

image = mpimg.imread('17_lesson_spiral.jpg')

fig, ax = pl.subplots(ncols = 2, figsize = (6, 3))
ax[0].imshow(image)
ax[0].axis('off')
ax[1].plot(x, y)
pl.tight_layout()




pl.show()
