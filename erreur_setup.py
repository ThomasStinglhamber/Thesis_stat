#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:16:05 2023

@author: thomasstinglhamber
"""

import pandas as pd
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import pandas as pd
import os
from openpyxl import load_workbook
import matplotlib.colors as mcolors


df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Erreurexp_1_Rot.xlsx', header=0)
df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Erreurexp_2_Rot.xlsx', header=0)
df3 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Erreurexp_3_Rot.xlsx', header=0)



# =============================================================================
# # Plot the surface
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# #ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='r')
# #ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z2'],marker='x',color='b')
# #ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='g')
# scatter=ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Moyenne_X'],marker='.',c=df['Mu'])
# legend = ax.legend(*scatter.legend_elements(), title="Map Energy")
# ax.add_artist(legend)
# plt.title('systematic error')
# ax.set_xlabel('X-coordinate [mm]')
# ax.set_ylabel('Y-coordinate [mm]')
# ax.set_zlabel('systematic shift in X-coordinate [mm]') 
# plt.show()
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt

wanted ='Moyenne_Y'
# group by Nominal_X and Nominal_Y columns and calculate the mean of Moyenne_Y
mean_df = df.groupby(['Nominal_X', 'Nominal_Y'])[wanted].mean().reset_index()
mean_df2 = df2.groupby(['Nominal_X', 'Nominal_Y'])[wanted].mean().reset_index()
mean_df3 = df3.groupby(['Nominal_X', 'Nominal_Y'])[wanted].mean().reset_index()

print(mean_df)
# plot the mean values as a separate scatter plot
# =============================================================================
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(mean_df['Nominal_X'], mean_df['Nominal_Y'], mean_df['Moyenne_Y'], marker='x', color='r')
# plt.show()
# =============================================================================
x=mean_df['Nominal_X']
y=mean_df['Nominal_Y']
z=mean_df[wanted]
z2=mean_df2[wanted]
z3=mean_df3[wanted]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='r')
#ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z2'],marker='x',color='b')
#ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='g')
scatter=ax.scatter(mean_df['Nominal_X'],mean_df['Nominal_Y'],mean_df[wanted],marker='o',alpha=1,label='Setup1',color='r')#,c=mean_df['Mu'])
scatter2=ax.scatter(mean_df2['Nominal_X'],mean_df2['Nominal_Y'],mean_df2[wanted],marker='o',alpha=1,label='Setup2',color='g')#,c=mean_df['Mu'])
scatter3=ax.scatter(mean_df3['Nominal_X'],mean_df3['Nominal_Y'],mean_df3[wanted],marker='o',alpha=1,label='Setup3',color='b')#,c=mean_df['Mu'])
# Interpolate the data to create a surface
xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((x, y), z, (xi, yi), method='cubic')
ax.plot_surface(xi, yi, zi, cmap='viridis')
zi2 = griddata((x, y), z2, (xi, yi), method='cubic')
ax.plot_surface(xi, yi, zi2, cmap='viridis')
zi3 = griddata((x, y), z3, (xi, yi), method='cubic')
ax.plot_surface(xi, yi, zi3, cmap='viridis')
legend = ax.legend(title="Phoenix-Plan")
ax.add_artist(legend)
plt.title('Average spot position error for an Angle of 0°, '+ 'Energy of [100,200] MeV and MU of [1,2]',fontsize=13)
ax.set_xlabel('X-coordinate [mm]',fontsize=13)
ax.set_ylabel('Y-coordinate [mm]',fontsize=13)
ax.set_zlabel('Average spot position error in Y-coordinate [mm]',fontsize=13)
plt.tight_layout()

plt.show()






