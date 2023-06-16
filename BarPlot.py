
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:01:35 2023

@author: thomasstinglhamber
"""

# Angle ---------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.rcParams.update({'font.size': 18})
# Define the systematic X and Y data
systematic_X = np.array([[0.19, 0.2, 0.15, 0.14, 0.22],
                        [0.6, 0.4, 0.32, 0.3, 0.64],
                        [0.41, 0.2, 0.17, 0.16, 0.42]])
systematic_Y = np.array([[0.28, 0.32, 0.34, 0.24, 0.16],
                        [0.1, 0.03, 0.14, -0.2, -0.26],
                        [-0.19, -0.29, -0.2, -0.44, -0.42]])

# Define the random X and Y data
random_X = np.array([[0.23, 0.23, 0.29, 0.27, 0.24],
                     [0.4, 0.25, 0.3, 0.35, 0.39],
                     [0.27, 0.14, 0.18, 0.27, 0.32]])
random_Y = np.array([[0.23, 0.19, 0.22, 0.24, 0.18],
                     [0.31, 0.25, 0.28, 0.37, 0.27],
                     [0.23, 0.2, 0.23, 0.36, 0.22]])

# Create the barplot for systematic X and Y
angles = [0, 45, 90, 180, 270]
x_pos = np.arange(len(angles))
bar_width = 0.2

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 7))
ax[0].plot(x_pos, systematic_X[0, :], marker='^', markersize=8, linestyle='', color='red', label='Plan-Log')
ax[0].plot(x_pos + bar_width, systematic_X[1, :], marker='^', markersize=8, linestyle='', color='g', label='Phoenix-Log')
ax[0].plot(x_pos + 2 * bar_width, systematic_X[2, :], marker='^', markersize=8, linestyle='', color='b', label='Phoenix-Plan')

# Plot error bars for systematic X
for i in range(systematic_X.shape[0]):
    ax[0].errorbar(x_pos + i * bar_width, systematic_X[i, :], yerr=random_X[i, :], fmt='none', color='black', capsize=5)



ax[0].set_xticks(x_pos + bar_width)
ax[0].set_xticklabels(angles)
ax[0].set_ylim(-0.9,1.3)
ax[0].set_xlabel('Angle [°]')
ax[0].set_ylabel('Average spot position error in X-coordinate [mm]')
ax[0].legend()

ax[0].grid()
#plt.show()

#fig, ax = plt.subplots()
ax[1].plot(x_pos, systematic_Y[0, :], marker='^', markersize=8, linestyle='', color='red', label='Plan-Log')
ax[1].plot(x_pos + bar_width, systematic_Y[1, :], marker='^', markersize=8, linestyle='', color='g', label='Phoenix-Log')
ax[1].plot(x_pos + 2 * bar_width, systematic_Y[2, :], marker='^', markersize=8, linestyle='', color='b', label='Phoenix-Plan')

# Plot error bars for systematic Y
for i in range(systematic_Y.shape[0]):
    ax[1].errorbar(x_pos + i * bar_width, systematic_Y[i, :], yerr=random_Y[i, :], fmt='none', color='black', capsize=5)

ax[1].set_xticks(x_pos + bar_width)
ax[1].set_xticklabels(angles)
ax[1].set_ylim(-0.9,1.3)

ax[1].set_xlabel('Angle [°]')
ax[1].set_ylabel('Average spot position error in Y-coordinate [mm]')
ax[1].legend()

ax[1].grid()
plt.tight_layout()
plt.show()


# Energies ---------------------------------------------------------------


# Define the systematic X data
sys_x_data = np.array([[0.28, 0.21, 0.17, 0.11, 0.13],
                       [0.68, 0.59, 0.53, 0.24, 0.22],
                       [0.4, 0.38, 0.36, 0.12, 0.09]])

# Define the systematic Y data
sys_y_data = np.array([[0.23, 0.26, 0.27, 0.27, 0.32],
                       [-0.03, 0.0, -0.03, -0.1, -0.04],
                       [-0.26, -0.26, -0.29, -0.37, -0.36]])

# Define the random X data
rand_x_data = np.array([[0.24, 0.23, 0.23, 0.26, 0.27],
                        [0.31, 0.31, 0.32, 0.31, 0.33],
                        [0.26, 0.27, 0.24, 0.19, 0.22]])

# Define the random Y data
rand_y_data = np.array([[0.13, 0.17, 0.23, 0.23, 0.3],
                        [0.24, 0.26, 0.33, 0.35, 0.46],
                        [0.24, 0.26, 0.27, 0.29, 0.31]])

# Create the barplot for systematic X and Y
energies = [70, 100, 150, 200, 226]
x_pos = np.arange(len(energies))
bar_width = 0.2

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 7))
# =============================================================================
# bar1 = ax[0].bar(x_pos, sys_x_data[0, :], bar_width, yerr=rand_x_data[0, :], capsize=5, color='red', label='Plan-Log')
# bar2 = ax[0].bar(x_pos + bar_width, sys_x_data[1, :], bar_width, yerr=rand_x_data[1, :], capsize=5, color='g', label='Phoenix-Log')
# bar3 = ax[0].bar(x_pos + 2 * bar_width, sys_x_data[2, :], bar_width, yerr=rand_x_data[2, :], capsize=5, color='b', label='Phoenix-Plan')
# 
# =============================================================================

#ax[0].plot(x_pos, sys_x_data[0, :], marker='^', markersize=8, linestyle='', color='red', label='Plan-Log')
ax[0].plot(x_pos + bar_width, sys_x_data[1, :], marker='^', markersize=8, linestyle='', color='g', label='Phoenix-Log')
#ax[0].plot(x_pos + 2 * bar_width, sys_x_data[2, :], marker='^', markersize=8, linestyle='', color='b', label='Phoenix-Plan')

# Plot error bars for systematic X
for i in [1]:
    ax[0].errorbar(x_pos + i * bar_width, sys_x_data[i, :], yerr=rand_x_data[i, :], fmt='none', color='black', capsize=5)



ax[0].set_xticks(x_pos + bar_width)
ax[0].set_xticklabels(energies)
ax[0].set_ylim(-0.75,1.1)

ax[0].set_xlabel('Energy [MeV]')
ax[0].set_ylabel('Average spot position error in X-coordinate [mm]')
ax[0].legend()

ax[0].grid()
#plt.show()

#fig, ax = plt.subplots()
# =============================================================================
# bar1 = ax[1].bar(x_pos, sys_y_data[0, :], bar_width, yerr=rand_y_data[0, :], capsize=5, color='red', label='Plan-Log')
# bar2 = ax[1].bar(x_pos + bar_width, sys_y_data[1, :], bar_width, yerr=rand_y_data[1, :], capsize=5, color='g', label='Phoenix-Log')
# bar3 = ax[1].bar(x_pos + 2 * bar_width, sys_y_data[2, :], bar_width, yerr=rand_y_data[2, :], capsize=5, color='b', label='Phoenix-Plan')
# 
# =============================================================================

#ax[1].plot(x_pos, sys_y_data[0, :], marker='^', markersize=8, linestyle='', color='red', label='Plan-Log')
ax[1].plot(x_pos + bar_width, sys_y_data[1, :], marker='^', markersize=8, linestyle='', color='g', label='Phoenix-Log')
#ax[1].plot(x_pos + 2 * bar_width, sys_y_data[2, :], marker='^', markersize=8, linestyle='', color='b', label='Phoenix-Plan')

# Plot error bars for systematic Y
for i in [1]:
    ax[1].errorbar(x_pos + i * bar_width, sys_y_data[i, :], yerr=rand_y_data[i, :], fmt='none', color='black', capsize=5)



ax[1].set_xticks(x_pos + bar_width)
ax[1].set_xticklabels(energies)
ax[1].set_ylim(-0.75,1.1)

ax[1].set_xlabel('Energy [MeV]')
ax[1].set_ylabel('Average spot position error in Y-coordinate [mm]')
ax[1].legend()

ax[1].grid()
plt.tight_layout()

plt.show()


# Mu ---------------------------------------------------------------


# Define the systematic shift data in X
systematic_shift_X = np.array([[0.18, 0.19, 0.18, 0.18, 0.18, 0.17],
                              [0.45, 0.46, 0.46, 0.46, 0.45, 0.42],
                              [0.26, 0.27, 0.28, 0.28, 0.27, 0.26]])

# Define the systematic shift data in Y
systematic_shift_Y = np.array([[0.26, 0.27, 0.28, 0.28, 0.27, 0.26],
                              [-0.05, -0.03, -0.03, -0.03, -0.04, -0.06],
                              [-0.31, -0.29, -0.3, -0.31, -0.31, -0.32]])

# Define the random shift data in X
random_shift_X = np.array([[0.3, 0.25, 0.25, 0.24, 0.24, 0.24],
                         [0.44, 0.38, 0.35, 0.35, 0.34, 0.34],
                         [0.35, 0.27, 0.25, 0.25, 0.25, 0.25]])

# Define the random shift data in Y
random_shift_Y = np.array([[0.29, 0.21, 0.21, 0.21, 0.2, 0.2],
                         [0.4, 0.34, 0.33, 0.32, 0.32, 0.33],
                         [0.34, 0.28, 0.27, 0.26, 0.25, 0.24]])

# Define the x-axis labels (mu values)
mu = [0.015, 0.1, 0.5, 1, 2, 5]

x_pos = np.arange(len(mu))
bar_width = 0.2

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 7))
# =============================================================================
# bar1 = ax[0].bar(x_pos, systematic_shift_X[0, :], bar_width, yerr=random_shift_X[0, :], capsize=5, color='red', label='Plan-Log')
# bar2 = ax[0].bar(x_pos + bar_width, systematic_shift_X[1, :], bar_width, yerr=random_shift_X[1, :], capsize=5, color='g', label='Phoenix-Log')
# bar3 = ax[0].bar(x_pos + 2 * bar_width, systematic_shift_X[2, :], bar_width, yerr=random_shift_X[2, :], capsize=5, color='b', label='Phoenix-Plan')
# 
# =============================================================================
ax[0].plot(x_pos, systematic_shift_X[0, :], marker='^', markersize=8, linestyle='', color='red', label='Plan-Log')
ax[0].plot(x_pos + bar_width, systematic_shift_X[1, :], marker='^', markersize=8, linestyle='', color='g', label='Phoenix-Log')
ax[0].plot(x_pos + 2 * bar_width, systematic_shift_X[2, :], marker='^', markersize=8, linestyle='', color='b', label='Phoenix-Plan')

# Plot error bars for systematic X
for i in range(systematic_X.shape[0]):
    ax[0].errorbar(x_pos + i * bar_width, systematic_shift_X[i, :], yerr=random_shift_X[i, :], fmt='none', color='black', capsize=5)


ax[0].set_xticks(x_pos + bar_width)
ax[0].set_xticklabels(mu)
ax[0].set_ylim(-0.75,1)

ax[0].set_xlabel('MU')
ax[0].set_ylabel('Average spot position error in X-coordinate [mm]')
ax[0].legend()
ax[0].grid()

#plt.grid()
#plt.show()

#fig, ax = plt.subplots()
# =============================================================================
# bar1 = ax[1].bar(x_pos, systematic_shift_Y[0, :], bar_width, yerr=random_shift_Y[0, :], capsize=5, color='red', label='Plan-Log')
# bar2 = ax[1].bar(x_pos + bar_width, systematic_shift_Y[1, :], bar_width, yerr=random_shift_Y[1, :], capsize=5, color='g', label='Phoenix-Log')
# bar3 = ax[1].bar(x_pos + 2 * bar_width, systematic_shift_Y[2, :], bar_width, yerr=random_shift_Y[2, :], capsize=5, color='b', label='Phoenix-Plan')
# 
# =============================================================================

ax[1].plot(x_pos, systematic_shift_Y[0, :], marker='^', markersize=8, linestyle='', color='red', label='Plan-Log')
ax[1].plot(x_pos + bar_width, systematic_shift_Y[1, :], marker='^', markersize=8, linestyle='', color='g', label='Phoenix-Log')
ax[1].plot(x_pos + 2 * bar_width, systematic_shift_Y[2, :], marker='^', markersize=8, linestyle='', color='b', label='Phoenix-Plan')

# Plot error bars for systematic Y
for i in range(systematic_Y.shape[0]):
    ax[1].errorbar(x_pos + i * bar_width, systematic_shift_Y[i, :], yerr=random_shift_Y[i, :], fmt='none', color='black', capsize=5)



ax[1].set_xticks(x_pos + bar_width)
ax[1].set_xticklabels(mu)
ax[1].set_ylim(-0.75,1)

ax[1].set_xlabel('MU')
ax[1].set_ylabel('Average spot position error in Y-coordinate [mm]')
ax[1].legend()

plt.grid()
plt.tight_layout()

plt.show()









