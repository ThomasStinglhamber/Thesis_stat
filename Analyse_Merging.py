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

df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix/Merge.xlsx', header=0)


df_value= df.query("Mu != 0.015")#.query("Angle == 270")
print(df_value)


fig, ax = plt.subplots()
scatter = ax.scatter(df_value['Std_X'], df_value['Std_Y'], marker='x', c=df_value['Mu'],cmap='viridis')
legend = ax.legend(*scatter.legend_elements(), title="Map Energy")
ax.add_artist(legend)
ax.set_xlabel(r' $\sigma_x$')
ax.set_ylabel(r'$\sigma_y$')

# =============================================================================
# plt.figure()
# plt.hist(df_value['Std_X'],bins=100)
# plt.show()
# plt.figure()
# plt.hist(df_value['Std_Y'],bins=100)
# plt.show()
# 
# =============================================================================
# =============================================================================
# fig, ax = plt.subplots()
# scatter = ax.scatter(df['Std_X'], df['Std_Y'], marker='x', c=df['Energy'],cmap='viridis')
# legend = ax.legend(*scatter.legend_elements(), title="Map Energy")
# ax.add_artist(legend)
# ax.set_xlabel(r' $\sigma_x$')
# ax.set_ylabel(r'$\sigma_y$')
# 
# fig, ax = plt.subplots()
# scatter = ax.scatter(df['Std_X'], df['Std_Y'], marker='x', c=df['Mu'],cmap='viridis')
# legend = ax.legend(*scatter.legend_elements(), title="Map Mu")
# ax.add_artist(legend)
# ax.set_xlabel(r' $\sigma_x$')
# ax.set_ylabel(r'$\sigma_y$')
# 
# fig, ax = plt.subplots()
# scatter = ax.scatter(df['Std_X'], df['Std_Y'], marker='x', c=df['Angle'],cmap='viridis')
# legend = ax.legend(*scatter.legend_elements(), title="Map Angle")
# ax.add_artist(legend)
# ax.set_xlabel(r' $\sigma_x$')
# ax.set_ylabel(r'$\sigma_y$')
# 
# 
# fig, ax = plt.subplots()
# scatter = ax.scatter(df['Moyenne_X'], df['Moyenne_Y'], marker='x', c=df['Energy'],cmap='viridis')
# legend = ax.legend(*scatter.legend_elements(), title="Map Energy")
# ax.add_artist(legend)
# ax.set_xlabel(r' $\sigma_x$')
# ax.set_ylabel(r'$\sigma_y$')
# 
# fig, ax = plt.subplots()
# scatter = ax.scatter(df['Moyenne_X'], df['Moyenne_Y'], marker='x', c=df['Mu'],cmap='viridis')
# legend = ax.legend(*scatter.legend_elements(), title="Map Mu")
# ax.add_artist(legend)
# ax.set_xlabel(r' $\sigma_x$')
# ax.set_ylabel(r'$\sigma_y$')
# 
# fig, ax = plt.subplots()
# scatter = ax.scatter(df['Moyenne_X'], df['Moyenne_Y'], marker='x', c=df['Angle'],cmap='viridis')
# legend = ax.legend(*scatter.legend_elements(), title="Map Angle")
# ax.add_artist(legend)
# ax.set_xlabel(r' $\sigma_x$')
# ax.set_ylabel(r'$\sigma_y$')
# 
# =============================================================================


