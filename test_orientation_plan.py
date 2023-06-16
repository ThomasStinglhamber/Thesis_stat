#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:30:34 2023

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


def plot_shifts(angle, mu, energy):
    # Filter the dataframe to include only the relevant combination of Angle, Mu, and Energy
    df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log.xlsx', header=0)
    df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/+20mm.xlsx', header=0)
    df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/-20mm.xlsx', header=0)
    
    df = df[(df['Angle'] == angle)]
    
    # Create a scatter plot of the X and Y shifts
    plt.figure()
    plt.scatter(df['Moyenne_X']+df['Nominal_X'], df['Moyenne_Y']+df['Nominal_Y'],label='420mm')
    plt.scatter(df1['Moyenne_X'], df1['Moyenne_Y'],label='620mm')
    plt.scatter(df2['Moyenne_X'], df2['Moyenne_Y'],label='220mm')
    #plt.scatter(df['Nominal_X'],df['Nominal_Y'],marker='x')
    plt.title(f'Shifts for Angle={angle}, Mu={mu}, Energy={energy}')
    plt.xlabel('X-coordinate [mm]')
    plt.ylabel('Y-coordinate [mm]')
    plt.legend()
    plt.show()





# Plot the shifts for Angle=30, Mu=0.5, Energy=10
#plot_shifts(0, 1, 200)

# =============================================================================
# 
# def plot_shifts3D(angle, mu, energy):
#     # Filter the dataframe to include only the relevant combination of Angle, Mu, and Energy
#     df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log.xlsx', header=0)
#     df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/+20mm.xlsx', header=0)
#     df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/-20mm.xlsx', header=0)
#     
#     df = df[(df['Angle'] == angle) &(df['Mu'] == 1)&(df['Energy'] == 200)]
# 
#     # Plot the surface
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     
#     # Scatter plot for the base plan
#     ax.scatter(df['Moyenne_X']+df['Nominal_X'], df['Moyenne_Y']+df['Nominal_Y'], 420, marker='x', color='r', label='base')
# 
#     # Scatter plot for the +20mm plan
#     ax.scatter(df1['Moyenne_X'], df1['Moyenne_Y'], 620, marker='x', color='b', label='+20')
# 
#     # Scatter plot for the -20mm plan
#     ax.scatter(df2['Moyenne_X'], df2['Moyenne_Y'], 220, marker='x', color='r', label='-20')
#     
#     # Loop over each spot in the base plan
#     for i in range(36):
#         # Get the X and Y coordinates of the current spot in the base plan
#         base_x = df.iloc[i]['Moyenne_X'] + df.iloc[i]['Nominal_X']
#         base_y = df.iloc[i]['Moyenne_Y'] + df.iloc[i]['Nominal_Y']
#         
#         # Get the corresponding spot in the +20mm plan
#         plus_x = df1.iloc[i]['Moyenne_X']
#         plus_y = df1.iloc[i]['Moyenne_Y']
#         
#         # Get the corresponding spot in the -20mm plan
#         minus_x = df2.iloc[i]['Moyenne_X']
#         minus_y = df2.iloc[i]['Moyenne_Y']
#         
#         # Plot a line connecting the current spot in the base plan to the corresponding spots in the other two plans
#         ax.plot([base_x, plus_x], [base_y, plus_y], [420, 620], color='b')
#         ax.plot([base_x, 0], [base_y, 0], [420, 220], color='r')
#     
#     plt.title('systematic error for : Angle = '+str(angle)+'°')
#     ax.set_xlabel('X-coordinate [mm]')
#     ax.set_ylabel('Y-coordinate [mm]')
#     plt.show()
# 
# =============================================================================
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

angle=0
# Load the data for each plan
df_base = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log.xlsx', header=0)
df_plus20 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/+20mm.xlsx', header=0)
df_minus20 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/-20mm.xlsx', header=0)

# Filter the data to include only the relevant combination of Angle, Mu, and Energy
df_base = df_base[(df_base['Angle'] == angle) &(df_base['Mu'] == 1)&(df_base['Energy'] == 200)]
df_plus20 = df_plus20[(df_plus20['Angle'] == angle) &(df_plus20['Mu'] == 1)&(df_plus20['Energy'] == 200)]
df_minus20 = df_minus20[(df_minus20['Angle'] == angle) &(df_minus20['Mu'] == 1)&(df_minus20['Energy'] == 200)]

# Create a new figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the coordinates of the spots for each plan
ax.scatter(df_base['Moyenne_X']+df_base['Nominal_X'], df_base['Moyenne_Y']+df_base['Nominal_Y'], 420, marker='x', color='r', label='420mm')
ax.scatter(df_plus20['Moyenne_X'], df_plus20['Moyenne_Y'], 620, marker='x', color='b', label='620mm')
ax.scatter(df_minus20['Moyenne_X'], df_minus20['Moyenne_Y'], 220, marker='x', color='g', label='220mm')

# Plot a line connecting the spots from the base plan to the plus20 plan
for i in range(len(df_base)):
    x_vals = [df_base.iloc[i]['Moyenne_X']+df_base.iloc[i]['Nominal_X'], df_plus20.iloc[i]['Moyenne_X']]
    y_vals = [df_base.iloc[i]['Moyenne_Y']+df_base.iloc[i]['Nominal_Y'], df_plus20.iloc[i]['Moyenne_Y']]
    z_vals = [420, 620]
    ax.plot(x_vals, y_vals, z_vals, color='black',alpha=0.6)

# Plot a line connecting the spots from the base plan to the minus20 plan
for i in range(len(df_base)):
    x_vals = [df_base.iloc[i]['Moyenne_X']+df_base.iloc[i]['Nominal_X'], df_minus20.iloc[i]['Moyenne_X']]
    y_vals = [df_base.iloc[i]['Moyenne_Y']+df_base.iloc[i]['Nominal_Y'], df_minus20.iloc[i]['Moyenne_Y']]
    z_vals = [420, 220]
    ax.plot(x_vals, y_vals, z_vals, color='black',alpha=0.6)

# Set the title and axis labels
#plt.title('Systematic error for Angle = '+str(angle)+'°')
ax.set_xlabel('X-coordinate [mm]')
ax.set_ylabel('Y-coordinate [mm]')
ax.set_zlabel('Z-coordinate [mm]')
plt.legend()

#plot_shifts3D(0, 1, 200)
# =============================================================================
# def plot_shifts3D(angle, mu, energy):
#     # Filter the dataframe to include only the relevant combination of Angle, Mu, and Energy
#     df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log.xlsx', header=0)
#     df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/+20mm.xlsx', header=0)
#     df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/-20mm.xlsx', header=0)
#     
#     df = df[(df['Angle'] == angle) &(df['Mu'] == 1)&(df['Energy'] == 200)]
#     
#     # Create a scatter plot of the X and Y shifts
#     plt.figure()
#     plt.scatter(df['Moyenne_X']+df['Nominal_X'], df['Moyenne_Y']+df['Nominal_Y'],label='base')
#     plt.scatter(df1['Moyenne_X'], df1['Moyenne_Y'],label='+20')
#     plt.scatter(df2['Moyenne_X'], df2['Moyenne_Y'],label='-20')
#     #plt.scatter(df['Nominal_X'],df['Nominal_Y'],marker='x')
#     plt.title(f'Shifts for Angle={angle}, Mu={mu}, Energy={energy}')
#     plt.xlabel('X Shift')
#     plt.ylabel('Y Shift')
#     plt.legend()
#     plt.show()
# 
#     # Plot the surface
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     
#     ax.scatter(df['Moyenne_X']+df['Nominal_X'], df['Moyenne_Y']+df['Nominal_Y'],420,marker='x',color='r',label='base')
#     ax.scatter(df1['Moyenne_X'], df1['Moyenne_Y'],620,marker='x',color='b',label='+20')
#     ax.scatter(df2['Moyenne_X'], df2['Moyenne_Y'],220,marker='x',color='r',label='-20')
#     
#     plt.title('systematic error for : Angle = '+str(angle)+'°')
#     
#     ax.set_xlabel('X-coordinate [mm]')
#     ax.set_ylabel('Y-coordinate [mm]')
# 
# 
# 
# # Plot the shifts for Angle=30, Mu=0.5, Energy=10
# plot_shifts3D(0, 1, 200)
# =============================================================================



# Import the data
#df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log.xlsx', header=0)

# Calculate the Z coordinate for each spot
for i in [0,90,180,270]:
    df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New/Phoenix_Log.xlsx', header=0)

    
    def calculate_z(df,angle,mu,energy):
        df = df[(df['Angle'] == angle)  ]
        # Calculate the distance between each spot and the origin
        df['dx'] = np.sqrt((df['Nominal_X'])**2+(df['Nominal_Y'])**2)
        #df['dy'] = np.sqrt( (df['Nominal_Y'])**2)
        
        #df['dx2'] = np.sqrt((df['Nominal_X']+df['Moyenne_X'])**2 +(df['Nominal_Y']+df['Moyenne_Y'])**2)
        df['dx2']= df['dx'] +df['Moyenne_Y']+df['Moyenne_X']
        #df['dy2'] = np.sqrt((df['Nominal_Y']+df['Moyenne_Y'])**2)
        df['theta'] = np.arctan2(df['dx'], 420)
        #df['phi'] = np.arctan2(df['dy'], 420)
        
        # Calculate the Z coordinate for each spot
        df['Z'] = (df['dx2']) / np.tan(df['theta'])
        #df['Z2'] = (df['dy2']) / np.tan(df['phi'])
        return df
    
    
    
    df = calculate_z(df,i, 0.5, 100)
    
    # Print the resulting dataframe
    print(df['Z'].mean())
    
    
    # Plot the surface
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='r')
    #ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z2'],marker='x',color='b')
    ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='g')
    
    plt.title('angle'+str(i))
    
    ax.set_xlabel('X-coordinate [mm]')
    ax.set_ylabel('Y-coordinate [mm]')
    ax.set_zlabel('systematic shift in X-coordinate [mm]')
    plt.show()
    
    
    
    
    
    import pandas as pd
    import numpy as np
    from scipy.optimize import least_squares
    
    def fit_plane(df):
        # Fit a plane to the reference points using least squares
        A = np.column_stack((df['Nominal_X'], df['Nominal_Y'], np.ones(len(df))))
        b = df['Z']
        x, res, _, _ = np.linalg.lstsq(A, b, rcond=None)
    
        # Return the coefficients of the plane's equation
        return x
    
    def calculate_z(df, coefficients, distance=420):
        # Calculate the Z shift for each point using the plane's equation
        df['Z2'] =   (coefficients[0] * df['Nominal_X']+ coefficients[1] * df['Nominal_Y'] + coefficients[2])
    
        return df
    
    
    
    
    
    
    
    coefficients = fit_plane(df)
    df = calculate_z(df, coefficients)
    print(coefficients)
    
    print(df['Z2'].mean())
    
# =============================================================================
#     # Plot the surface
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     #ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='r')
#     #ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z2'],marker='x',color='b')
#     ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='g')
#     ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z2'],marker='x',color='r')
#     plt.title('systematic error for Mu ')
#     
#     ax.set_xlabel('X-coordinate [mm]')
#     ax.set_ylabel('Y-coordinate [mm]')
#     ax.set_zlabel('systematic shift in X-coordinate [mm]')
#     plt.show()
# =============================================================================
    
    
    x_range = np.arange(-150, 151, 10)
    y_range = np.arange(-150, 151, 10)
    X, Y = np.meshgrid(x_range, y_range)
    Z = coefficients[0] * X + coefficients[1] * Y + coefficients[2]
    
    # Plot the plane in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.scatter(df['Nominal_X'],df['Nominal_Y'],df['Z'],marker='x',color='g')
    plt.title('angle = '+str(i))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.invert_zaxis()
    plt.show()
    
    
