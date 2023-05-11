import matplotlib.pyplot as pl
import numpy as np
import math

x = np.linspace(0, 2 * math.pi, 1000)
y = np.sin(x)

fig = pl.figure()
pl.plot(x, y)

pl.xlabel('x-label')
pl.ylabel('y-label')
pl.title('test figure')

pl.show()

# Write a program to visualize sine function f(x)=sin(x) in the domain x = [0, 2π] ?