#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:15:49 2023

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
#from Spot_Analysis2 import *


df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New/Erreur_setup_1.xlsx', header=0)


def calculate_z(df,angle,mu,energy):
    #df = df[(df['Angle'] == angle) & (df['Mu'] == mu) & (df['Energy'] == energy)]
    # Calculate the distance between each spot and the origin
    df['dx'] = (df['Nominal_X'])
    #df['dy'] = np.sqrt( (df['Nominal_Y'])**2)
    df['dy'] = (df['Nominal_Y'])
    
    
    df['dx2'] = (df['Nominal_X']+ df['Moyenne_X'])
    
    
    df['theta'] = np.arctan2(df['dx'], 420)
    df['phi'] = np.arctan2(df['dy'], 420)
    
    # Calculate the Z coordinate for each spot
    df['Z'] = df['dx2']/ np.tan(df['theta'])
    df['dy2'] = 520 * np.tan(df['phi'])
    #df['Z2'] = (df['dy2']) / np.tan(df['phi'])
    return df






#df = calculate_z(df,0, 0.5, 100)
#print(df['Z'])

#df = df.groupby(['Angle'])

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='r')
#ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z2'],marker='x',color='b')
#ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='g')
scatter=ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Moyenne_X'],marker='.',c=df['Mu'])
legend = ax.legend(*scatter.legend_elements(), title="Map Energy")
ax.add_artist(legend)
plt.title('systematic error')
ax.set_xlabel('X-coordinate [mm]')
ax.set_ylabel('Y-coordinate [mm]')
ax.set_zlabel('systematic shift in X-coordinate [mm]')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# group by Nominal_X and Nominal_Y columns and calculate the mean of Moyenne_Y
mean_df = df.groupby(['Nominal_X', 'Nominal_Y','Mu'])['Moyenne_X'].mean().reset_index()

print(mean_df)
# plot the mean values as a separate scatter plot
# =============================================================================
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(mean_df['Nominal_X'], mean_df['Nominal_Y'], mean_df['Moyenne_Y'], marker='x', color='r')
# plt.show()
# =============================================================================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='r')
#ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z2'],marker='x',color='b')
#ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='g')
scatter=ax.scatter(mean_df['Nominal_X'],mean_df['Nominal_Y'],mean_df['Moyenne_X'],marker='o',alpha=1,c=mean_df['Mu'])
legend = ax.legend(*scatter.legend_elements(), title="Map Energy")
ax.add_artist(legend)
plt.title('systematic error')
ax.set_xlabel('X-coordinate [mm]')
ax.set_ylabel('Y-coordinate [mm]')
ax.set_zlabel('systematic shift in Y-coordinate [mm]')
plt.show()





# plan interpol
# =============================================================================
# x=mean_df['Nominal_X']
# y=mean_df['Nominal_Y']
# z=mean_df['Moyenne_X']
# # Interpolate the data to create a surface
# xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
# xi, yi = np.meshgrid(xi, yi)
# zi = griddata((x, y), z, (xi, yi), method='cubic')
# 
# # Plot the surface
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x,y,z,marker='x',c=mean_df['Angle'])
# ax.plot_surface(xi, yi, zi, cmap='viridis')
# plt.title('Averaged-systematic error in X-coordinate for all Mu,Angle and Energy' )
# 
# ax.set_xlabel('X-coordinate [mm]')
# ax.set_ylabel('Y-coordinate [mm]')
# ax.set_zlabel('systematic shift in Y-coordinate [mm]')
# 
# =============================================================================


# =============================================================================
# plt.figure()
# # Create a scatter plot of the X and Y shifts
# plt.scatter(df['Moyenne_X']+df['Nominal_X'], df['Moyenne_Y']+df['Nominal_Y'])
# plt.scatter(df['Nominal_X'],df['Nominal_Y'],marker='x')
# #plt.title(f'Shifts for Angle={angle}, Mu={mu}, Energy={energy}')
# plt.xlabel('X Shift')
# plt.ylabel('Y Shift')
# plt.show()
# 
# =============================================================================




