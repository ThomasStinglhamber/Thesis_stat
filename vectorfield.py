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

def multiple():
    #[0,45,90,180,270]
    #[0.015,0.1,0.5,1,2,5]
    #[70,100,150,200,226]
    for k in [0,45,90,180,270]:
        # Load the data
        df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Phoenix_Log.xlsx', header=0)
        
        # Filter the data for a specific angle
        df = df.query('Angle =='+str(k)).query('Mu ==1').query('Energy ==200')
        
        # Group the data by nominal X and Y coordinates and calculate the mean of the mean X and Y shifts for each group
        grouped_df = df.groupby(['Nominal_X', 'Nominal_Y'])[['Moyenne_X', 'Moyenne_Y']].mean()
        plt.figure()
        # Create a scatter plot of the nominal X and Y coordinates
        plt.scatter(df['Nominal_X'], df['Nominal_Y'], marker='x')
        
        # Add an arrow from the nominal point to the mean point for each group
        for i, row in grouped_df.iterrows():
            dx_mean = row['Moyenne_X']
            dy_mean = row['Moyenne_Y']
            #plt.arrow(i[0], i[1], dx_mean, dy_mean, length_includes_head=True, head_width=0.02)
            #plt.quiver(i[0], i[1], dx_mean, dy_mean, scale=5)
            #plt.quiver(i[0], i[1], dx_mean, 0, scale=5)
            plt.quiver(i[0]+dx_mean, i[1], 0, dy_mean, scale=5)
        
        plt.title("Angle of "+str(k)+'°')
        plt.xlabel('X Shift')
        plt.ylabel('Y Shift')
        plt.show()
        


def single():

    # Load the data
    df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Phoenix_Log_Rot.xlsx', header=0)
    # Filter the data for a specific angle
    df = df.query('Angle == 0')
    #df=df1-df2
    # Group the data by nominal X and Y coordinates and calculate the mean of the mean X and Y shifts for each group
    grouped_df = df.groupby(['Nominal_X', 'Nominal_Y'])[['Moyenne_X', 'Moyenne_Y']].mean()
    plt.figure()
    # Create a scatter plot of the nominal X and Y coordinates
    plt.scatter(df['Nominal_X'], df['Nominal_Y'], marker='x')
    
    # Add an arrow from the nominal point to the mean point for each group
    for i, row in grouped_df.iterrows():
        dx_mean = row['Moyenne_X']
        dy_mean = row['Moyenne_Y']
        #plt.arrow(i[0], i[1], dx_mean, dy_mean, length_includes_head=True, head_width=0.02)
        plt.quiver(i[0], i[1], dx_mean, dy_mean, scale=5)
        #plt.quiver(i[0], i[1], dx_mean, 0, scale=5)
        #plt.quiver(i[0]+dx_mean, i[1], 0, dy_mean, scale=5)
    
    plt.title("Pheonix_log")
    plt.xlabel('X-coordinate [mm]')
    plt.ylabel('Y-coordinate [mm]')
    plt.show()
    
    return
    
def two():
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 5))  # create figure and axes for the two subplots
    fig.suptitle('Vector field visualization based on the directions of measured point in Phoenix-Plan Dataset', fontsize=14)
    df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Erreurexp_1_Rot.xlsx', header=0)
    df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Erreurexp_2_Rot.xlsx', header=0)
    df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Erreurexp_3_Rot.xlsx', header=0)
    
    for k, ax in zip([df, df1,df2], [ax1, ax2, ax3]):
        # Load the data
        #df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Plan_Log.xlsx', header=0)
    
        # Filter the data for a specific angle
        df = k
    
        # Group the data by nominal X and Y coordinates and calculate the mean of the mean X and Y shifts for each group
        grouped_df = df.groupby(['Nominal_X', 'Nominal_Y'])[['Moyenne_X', 'Moyenne_Y']].mean()
    
        # Create a scatter plot of the nominal X and Y coordinates
        ax.scatter(df['Nominal_X'], df['Nominal_Y'], marker='x',color='black')
    
        # Add an arrow from the nominal point to the mean point for each group
        for i, row in grouped_df.iterrows():
            dx_mean = row['Moyenne_X']
            dy_mean = row['Moyenne_Y']
            ax.quiver(i[0], i[1], dx_mean, dy_mean, scale=7,color='black')
            ax.quiver(i[0], i[1], dx_mean, 0, scale=7,alpha=0.4,color='g')
            ax.quiver(i[0]+dx_mean, i[1], 0, dy_mean, scale=7,alpha=0.4,color='r')
    
        font = 14
        ax1.set_title("Setup 1",fontsize=font)
        ax2.set_title("Setup 2",fontsize=font)
        ax3.set_title("Setup 3",fontsize=font)
        ax.set_xlabel('X-coordinate [mm]',fontsize=font)
        ax.set_ylabel('Y-coordinate [mm]',fontsize=font)
        ax.invert_xaxis()
        ax.invert_yaxis()
        #ax.legend(['Plan','direction'])
        plt.tight_layout()

    
    plt.show()


two()
#single()
#multiple()


def two2():
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # create figure and axes for the two subplots
    fig.suptitle('Vector field visualization based on the directions of measured point in Phoenix-Plan Dataset', fontsize=14)
    
    for k, ax in zip([0, 45], [ax1, ax2]):
        # Load the data
        df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Plan_Log.xlsx', header=0)
    
        # Filter the data for a specific angle
        df = df.query('Angle=='+str(k))
    
        # Group the data by nominal X and Y coordinates and calculate the mean of the mean X and Y shifts for each group
        grouped_df = df.groupby(['Nominal_X', 'Nominal_Y'])[['Moyenne_X', 'Moyenne_Y']].mean()
    
        # Create a scatter plot of the nominal X and Y coordinates
        ax.scatter(df['Nominal_X'], df['Nominal_Y'], marker='x',color='black')
    
        # Add an arrow from the nominal point to the mean point for each group
        for i, row in grouped_df.iterrows():
            dx_mean = row['Moyenne_X']
            dy_mean = row['Moyenne_Y']
            ax.quiver(i[0], i[1], dx_mean, dy_mean, scale=7,color='black')
            ax.quiver(i[0], i[1], dx_mean, 0, scale=7,alpha=0.4,color='g')
            ax.quiver(i[0]+dx_mean, i[1], 0, dy_mean, scale=7,alpha=0.4,color='r')
    
        
        if ax ==ax1:
            ax1.set_title("Angle of "+str(k)+"°")
        #if ax ==ax3:
        #     ax3.set_title("Angle of "+str(k)+"°")
        else: ax2.set_title("Angle of "+str(k)+"°")
        #print(k)
        #ax3.set_title("Setup 3")
        ax.set_xlabel('X-coordinate [mm]')
        ax.set_ylabel('Y-coordinate [mm]')
        #ax.invert_xaxis()
        #ax.invert_yaxis()
        #ax.legend(['Plan','direction'])
        plt.tight_layout()

    
    plt.show()
    
#two2()

