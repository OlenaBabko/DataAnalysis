import matplotlib.pyplot as pl
import numpy as np
import os


current_folder = os.getcwd()
os.chdir(r"C:\Users\viver\OneDrive\RENDER.UA\12_Lambda\13_IT\UDEMY\GraphPlotting\22_lesson\data")

for i in [0, 1, 2, 3, 4, 6]:
    filename = 'data' +str(i) + '.csv'
    A = np.loadtxt(filename, delimiter = None)
    x = A[:, 0]
    y = A[:, 1]
    pl.plot(x, y)


pl.show()
