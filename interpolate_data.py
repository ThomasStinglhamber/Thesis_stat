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




#df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log.xlsx', header=0)
#df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Nominal_Phoenix.xlsx', header=0)

# =============================================================================
# X_nominal=[150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150]
# Y_nominal =[150,150,150,150,150,150,90,90,90,90,90,90,30,30,30,30,30,30,-30,-30,-30,-30,-30,-30,-90,-90,-90,-90,-90,-90,-150,-150,-150,-150,-150,-150]
# 
# #["Mu == 0.015","Mu == 0.1","Mu == 0.5","Mu == 1","Mu == 2","Mu == 5"]
# #["Energy == 70","Energy == 100","Energy == 150","Energy == 200","Energy == 226"]
# 
# 
# for i in [0.5,1,5]:
#     for j in [100,200]:
#         df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Erreur_setupTEST.xlsx', header=0)
#     
#         df1= df1.query("Angle == 0").query("Mu =="+str(i)).query("Energy =="+str(j))
#         print(df1)
#         # Generate some sample data
#         x = X_nominal
#         y = Y_nominal
#         z = df1['Moyenne_X']
#         #print(len(x))
#         # Interpolate the data to create a surface
#         xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
#         xi, yi = np.meshgrid(xi, yi)
#         zi = griddata((x, y), z, (xi, yi), method='cubic')
#         
#         # Plot the surface
#         fig = plt.figure()
#         ax = fig.add_subplot(111, projection='3d')
#         ax.scatter(x,y,z,marker='x',color='r')
#         ax.plot_surface(xi, yi, zi, cmap='viridis')
#         plt.title('systematic error for Mu = '+str(i)+', Energy = '+str(j))
#         
#         ax.set_xlabel('X-coordinate [mm]')
#         ax.set_ylabel('Y-coordinate [mm]')
#         ax.set_zlabel('systematic shift in X-coordinate [mm]')
#         plt.show()
# =============================================================================
        
    
# Define the nominal values of x and y
X_nominal=[150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150]
Y_nominal=[150,150,150,150,150,150,90,90,90,90,90,90,30,30,30,30,30,30,-30,-30,-30,-30,-30,-30,-90,-90,-90,-90,-90,-90,-150,-150,-150,-150,-150,-150]

# Read the data from the excel file into a dataframe
df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Erreur_setupTEST.xlsx', header=0)

# Group the dataframe by angle, mu, energy, x, and y and calculate the means of the Moyenne_X column
df_grouped = df.groupby(['Angle', 'Mu', 'Energy', 'Nominal_X', 'Nominal_Y']).mean().reset_index()

# Loop over the different values of mu and energy
for i in [0.5,1,5]:
    for j in [100,200]:
        # Select the subset of the grouped dataframe corresponding to the current values of mu and energy
        df_subset = df_grouped.loc[(df_grouped['Mu'] == i) & (df_grouped['Energy'] == j)]

        # Extract the values of x, y, and z from the dataframe
        x = df_subset['Nominal_X'].values
        y = df_subset['Nominal_Y'].values
        z = df_subset['Moyenne_X'].values

        # Interpolate the data to create a surface
        xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
        xi, yi = np.meshgrid(xi, yi)
        zi = griddata((x, y), z, (xi, yi), method='cubic')

        # Plot the surface
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x,y,z,marker='x',color='r')
        ax.plot_surface(xi, yi, zi, cmap='viridis')
        plt.title('systematic error for Mu = '+str(i)+', Energy = '+str(j))

        ax.set_xlabel('X-coordinate [mm]')
        ax.set_ylabel('Y-coordinate [mm]')
        ax.set_zlabel('systematic shift in X-coordinate [mm]')
        plt.show()








