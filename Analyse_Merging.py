#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 10:55:56 2023

@author: thomasstinglhamber
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook
import matplotlib.colors as mcolors


df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Erreur_setup.xlsx', header=0)
#df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Nominal_Log.xlsx', header=0)
#df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log.xlsx', header=0)

Titre = 'Nominal_Log'
#Titre = 'Nominal-Phoenix'

df= df.query("Mu != 0.015")#.query("Angle == 270")
#print(df_value)

Nombre_bin = 50
#------------ Histogram ----------------------------------
plt.figure()
# group the dataframe by column 'Energy'
groups = df.groupby('Mu')

# create a histogram of column 'Moyenne_X' for each group
groups['Moyenne_X'].hist(bins=Nombre_bin)

# calculate the mean and standard deviation of each group
means = groups['Moyenne_X'].mean()
stds = groups['Moyenne_X'].std()

# create a dictionary containing the energy values as keys and the mean and standard deviation as values
energy_data = {energy: f"{energy} Mean: {mean:.4f}, Std: {std:.4f}" for energy, mean, std in zip(means.index, means, stds)}

# add the energy values, mean and standard deviation to the legend
plt.legend([energy_data[energy] for energy in means.index])
plt.title(Titre + ' : Moyenne X')
plt.xlabel(r' $\Sigma_x$')

plt.show()

print(groups['Moyenne_X'].describe())


# Same for Moyenne_Y
plt.figure()
# create a histogram of column 'Moyenne_X' for each group
groups['Moyenne_Y'].hist(bins=Nombre_bin)

# calculate the mean and standard deviation of each group
means = groups['Moyenne_Y'].mean()
stds = groups['Moyenne_Y'].std()

# create a dictionary containing the energy values as keys and the mean and standard deviation as values
energy_data = {energy: f"{energy} Mean: {mean:.4f}, Std: {std:.4f}" for energy, mean, std in zip(means.index, means, stds)}

# add the energy values, mean and standard deviation to the legend
plt.legend([energy_data[energy] for energy in means.index])
plt.title(Titre + ' : Moyenne Y')
plt.xlabel(r' $\Sigma_y$')
plt.show()

print(groups['Moyenne_Y'].describe())



plt.figure()
# create a histogram of column 'Moyenne_X' for each group
groups['Std_X'].hist(bins=Nombre_bin)

# calculate the mean and standard deviation of each group
means = groups['Std_X'].mean()
stds = groups['Std_X'].std()

# create a dictionary containing the energy values as keys and the mean and standard deviation as values
energy_data = {energy: f"{energy} Mean: {mean:.4f}, Std: {std:.4f}" for energy, mean, std in zip(means.index, means, stds)}

# add the energy values, mean and standard deviation to the legend
plt.legend([energy_data[energy] for energy in means.index])
plt.title(Titre + ' : Std X')
plt.xlabel(r' $\sigma_x$')

plt.show()

print(groups['Std_X'].describe())


# Same for Moyenne_Y
plt.figure()
# create a histogram of column 'Moyenne_X' for each group
groups['Std_Y'].hist(bins=Nombre_bin)

# calculate the mean and standard deviation of each group
means = groups['Std_Y'].mean()
stds = groups['Std_Y'].std()

# create a dictionary containing the energy values as keys and the mean and standard deviation as values
energy_data = {energy: f"{energy} Mean: {mean:.4f}, Std: {std:.4f}" for energy, mean, std in zip(means.index, means, stds)}

# add the energy values, mean and standard deviation to the legend
plt.legend([energy_data[energy] for energy in means.index])
plt.title(Titre +  '  : Std Y')
plt.xlabel(r' $\sigma_y$')

plt.show()

print(groups['Std_Y'].describe())



fig, ax = plt.subplots()
scatter = ax.scatter(df['Std_X'], df['Std_Y'], marker='.', c=df['Energy'],cmap='viridis')
legend = ax.legend(*scatter.legend_elements(), title="Map Energy")
ax.add_artist(legend)
ax.set_title(Titre + ': Std')
ax.set_xlabel(r' $\sigma_x$')
ax.set_ylabel(r'$\sigma_y$')

fig, ax = plt.subplots()
scatter = ax.scatter(df['Std_X'], df['Std_Y'], marker='.', c=df['Mu'],cmap='viridis')
legend = ax.legend(*scatter.legend_elements(), title="Map Mu")
ax.add_artist(legend)
ax.set_title(Titre + ': Std')
ax.set_xlabel(r' $\sigma_x$')
ax.set_ylabel(r'$\sigma_y$')

fig, ax = plt.subplots()
scatter = ax.scatter(df['Std_X'], df['Std_Y'], marker='.', c=df['Angle'],cmap='viridis')
legend = ax.legend(*scatter.legend_elements(), title="Map Angle")
ax.add_artist(legend)
ax.set_title(Titre + ': Std')
ax.set_xlabel(r' $\sigma_x$')
ax.set_ylabel(r'$\sigma_y$')


fig, ax = plt.subplots()
scatter = ax.scatter(df['Moyenne_X'], df['Moyenne_Y'], marker='.', c=df['Energy'],cmap='viridis')
legend = ax.legend(*scatter.legend_elements(), title="Map Energy")
ax.add_artist(legend)
ax.set_title(Titre + ': Moyenne')
ax.set_xlabel(r' $\Sigma_x$')
ax.set_ylabel(r'$\Sigma_y$')

fig, ax = plt.subplots()
scatter = ax.scatter(df['Moyenne_X'], df['Moyenne_Y'], marker='.', c=df['Mu'],cmap='viridis')
legend = ax.legend(*scatter.legend_elements(), title="Map Mu")
ax.add_artist(legend)
ax.set_title(Titre + ': Moyenne')
ax.set_xlabel(r' $\Sigma_x$')
ax.set_ylabel(r'$\Sigma_y$')

fig, ax = plt.subplots()
scatter = ax.scatter(df['Moyenne_X'], df['Moyenne_Y'], marker='.', c=df['Angle'],cmap='viridis')
legend = ax.legend(*scatter.legend_elements(), title="Map Angle")
ax.add_artist(legend)
ax.set_title(Titre + ': Moyenne')
ax.set_xlabel(r' $\Sigma_x$')
ax.set_ylabel(r'$\Sigma_y$')


