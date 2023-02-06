#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:32:04 2023

@author: thomasstinglhamber
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import pandas as pd
import os
from openpyxl import load_workbook
import matplotlib.colors as mcolors




df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Nominal_Log.xlsx', header=0)
X_nominal=[150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150]
Y_nominal =[150,150,150,150,150,150,90,90,90,90,90,90,30,30,30,30,30,30,-30,-30,-30,-30,-30,-30,-90,-90,-90,-90,-90,-90,-150,-150,-150,-150,-150,-150]

df1= df1.query("Angle == 270").query("Energy == 200").query("Mu == 0.015")
# Generate some sample data
x = X_nominal
y = Y_nominal
z = df1['Std_Y']
print(len(x))
# Interpolate the data to create a surface
xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((x, y), z, (xi, yi), method='cubic')

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z,marker='x',color='r')
ax.plot_surface(xi, yi, zi, cmap='viridis')
plt.title('Random error')

ax.set_xlabel('X-coordinate [mm]')
ax.set_ylabel('Y-coordinate [mm]')
ax.set_zlabel('random shift in Y-coordinate [mm]')
plt.show()