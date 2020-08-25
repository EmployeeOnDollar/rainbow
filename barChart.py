
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcdefaults()
fig, ax = plt.subplots()

# variables 'red', 'orange', 'yellow', 'green', 'blue', 'purple'

colours = pd.Series(('#FF0018', '#FFA52C', '#FFFF41', '#008018', '#0000F9', '#86007D'))
c_Tags = pd.Series(('red', 'orange', 'yellow', 'green', 'blue', 'purple'))

xvar = np.array([len(c_Tags)])
yvar = np.array([len(c_Tags)])

barWidth = 1.0
lefts = 0

for colours, c_Tags in zip(colours, c_Tags):
    ax = plt.barh(yvar, xvar, color=colours, tick_label=c_Tags, height=barWidth, left=lefts)
    yvar -= 1


plt.show()
