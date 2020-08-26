
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''code that displays LGBTQIA flags as horizontal bar chart
HEX are from: https://www.schemecolor.com/international-bear-brotherhood-flag-colors.php    
    '''

lgbtColours = pd.Series(('#FF0018', '#FFA52C', '#FFFF41', '#008018', '#0000F9', '#86007D'))
biColours = pd.Series(('#D60270', '#9B4F96', '#0038A8'))
transColours = pd.Series(('#F88BC2', '#FFFFFF', '#47A9FA', '#000000', '#CA93CA'))
asexColours = pd.Series(('#000000', '#A4A4A4', '#FFFFFF', '#810081'))
intersexColours = pd.Series(('#FFDA00', '#7A00AC'))
polysexColours = pd.Series(('#F714BA', '#01D66A', '#1594F6'))
intBBColours = pd.Series(('#633800', '#D76300', '#FFDE58', '#FFE7B5', '#FFFFFF', '#555555', '#000000'))

barWidth = 1.0
lefts = 0
x = 7

if x == 1:
    colours = lgbtColours
    xvar = np.array([len(colours)])
    yvar = np.array([len(colours)])

    for Colours in zip(lgbtColours):
        ax = plt.barh(yvar, xvar, color=Colours, height=barWidth, left=lefts)
        yvar -= 1

elif x == 2:
    colours = biColours
    xvar = np.array([len(colours)])
    yvar = np.array([len(colours)])
    for colours in zip(biColours):
        ax = plt.barh(yvar, xvar, color=colours, height=barWidth, left=lefts)
        yvar -= 1

elif x == 3:
    colours = transColours
    xvar = np.array([len(colours)])
    yvar = np.array([len(colours)])
    for colours in zip(transColours):
        ax = plt.barh(yvar, xvar, color=colours, height=barWidth, left=lefts)
        yvar -= 1

elif x == 4:
    colours = asexColours
    xvar = np.array([len(colours)])
    yvar = np.array([len(colours)])
    for colours in zip(asexColours):
        ax = plt.barh(yvar, xvar, color=colours, height=barWidth, left=lefts)
        yvar -= 1

elif x == 5:
    colours = intersexColours
    xvar = np.array([len(colours)])
    yvar = np.array([len(colours)])
    for colours in zip(intersexColours):
        ax = plt.barh(yvar, xvar, color=colours, height=barWidth, left=lefts)
        yvar -= 1

elif x == 6:
    colours = polysexColours
    xvar = np.array([len(colours)])
    yvar = np.array([len(colours)])
    for colours in zip(polysexColours):
        ax = plt.barh(yvar, xvar, color=colours, height=barWidth, left=lefts)
        yvar -= 1

elif x == 7:
    colours = intBBColours
    xvar = np.array([len(colours)])
    yvar = np.array([len(colours)])
    for colours in zip(intBBColours):
        ax = plt.barh(yvar, xvar, color=colours, height=barWidth, left=lefts)
        yvar -= 1

else:
    print('Invalid Number: No corresponding charts')

plt.show()
