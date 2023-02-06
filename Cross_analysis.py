#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:47:42 2023

@author: thomasstinglhamber
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook
import matplotlib.colors as mcolors


#df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Erreur_setup.xlsx', header=0)
df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Nominal_Log.xlsx', header=0)
df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log.xlsx', header=0)
df3 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Nominal_Phoenix.xlsx', header=0)


Titre = 'Nominal_Log'
#Titre = 'Nominal-Phoenix'

df1= df1.query("Mu == 5")#.query("Angle == 0").query("Energy == 100")
df2= df2.query("Mu == 5")#.query("Angle == 0").query("Energy == 100")
df3= df3.query("Mu == 5")#.query("Angle == 0").query("Energy == 100")

#print(df_value)

# concatenate the dataframes into one
#df = pd.concat([df1, df2, df3], axis=1)
plt.figure()
# plot the histograms
df1['Moyenne_X'].hist(bins=40, color='red',alpha=0.6)
df2['Moyenne_X'].hist(bins=40, color='green',alpha=0.6)
df3['Moyenne_X'].hist(bins=40, color='blue',alpha=0.6)
# calculate the mean of each distribution
mean1 = df1['Moyenne_X'].mean()
mean2 = df2['Moyenne_X'].mean()
mean3 = df3['Moyenne_X'].mean()

print(mean1,mean2,mean3)

# plot a line representing the mean of each distribution
plt.axvline(mean1, color='red', linestyle='dashed', linewidth=1)
plt.axvline(mean2, color='green', linestyle='dashed', linewidth=1)
plt.axvline(mean3, color='blue', linestyle='dashed', linewidth=1)

# add a legend
plt.title('Mu=0.015')
plt.legend([' Nominal-Log', ' Phoenix-Log', ' Nominal-Phoenix'])
plt.xlabel('x position error [mm]')
plt.ylabel('count')

# display the plot
plt.show()




