#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:49:13 2023

@author: thomasstinglhamber
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import math
import pandas as pd



df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Phoenix_Plan.xlsx', header=0)


df1= df.query('Angle ==180')#.query('Mu ==1').query('Energy ==200')


#print(df1)
#df1.sort_values(['Moyenne_Y'],ascending=[False], inplace=True,kind='mergesort')

kV_points = np.array([df1['Nominal_X'],df1['Nominal_Y']])
#print(df1['Moyenne_X'])
#print(phoenix_points)

phoenix_X = df1['Nominal_X']+df1['Moyenne_X']
phoenix_Y = df1['Nominal_Y']+df1['Moyenne_Y']

#phoenix_X=(sorted(phoenix_X, reverse=True))
#phoenix_Y=(sorted(phoenix_Y, reverse=True))
nom_X =df1['Nominal_X']
nom_Y =df1['Nominal_Y']

#nom_X=(sorted(nom_X, reverse=True))

nom_Y=(sorted(nom_Y, reverse=True))

array1=[]
array2=[]

for i,j in zip(phoenix_X,phoenix_Y):
    array1.append([i,j])
    
for l,k in zip(nom_X,nom_Y):
    array2.append([l,k])
    
print(np.array(array2))
print(np.array(array1))
phoenix_points =np.array(array1)
kV_points =np.array(array2)


def apply_translation(translation, points):
    points[:,0] += translation[0]
    points[:,1] += translation[1]

def apply_rotation(angle, points):
    angle = math.radians(angle)
    origin = [0.0, 0.0]
    for point in points:
        point[0] = origin[0] + math.cos(angle) * (point[0]-origin[0]) - math.sin(angle) * (point[1]-origin[1])
        point[1] = origin[1] + math.sin(angle) * (point[0]-origin[0]) + math.cos(angle) * (point[1]-origin[1])

def objective_fun1(translation, moving, reference):
    points = moving.copy()
    apply_translation(translation, points)
    return np.mean(np.linalg.norm(points-reference, axis=1)) # mean of the point distances

def objective_fun2(transformation, moving, reference):
    points = moving.copy()
    translation = transformation[0:2]
    rotation_angle = transformation[2]
    apply_translation(translation, points)
    apply_rotation(rotation_angle, points)
    return np.mean(np.linalg.norm(points-reference, axis=1)) # mean of the point distances


x0 = [0.0, 0.0] # initial translation
res = minimize(objective_fun1, x0, args=(phoenix_points, kV_points))
translated = phoenix_points.copy()
apply_translation(res.x, translated)

x0 = [0.0, 0.0, 0.0] # initial translation and rotation angle
res2 = minimize(objective_fun2, x0, args=(phoenix_points, kV_points))
transformed =  phoenix_points.copy()
apply_translation(res2.x[0:2], transformed)
apply_rotation(res2.x[2], transformed)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.scatter(kV_points[:,0], kV_points[:,1], marker='o', c='r', label="kV coordinates")
ax1.scatter(phoenix_points[:,0], phoenix_points[:,1], marker='x', c='k', label="Phoenix coordinates")
ax1.legend()
ax1.set_title("Before registration")
ax1.set(xlabel="X (mm)", ylabel="Y (mm)")

ax2.scatter(kV_points[:,0], kV_points[:,1], marker='o', c='r', label="kV coordinates")
ax2.scatter(translated[:,0], translated[:,1], marker='x', c='k', label="Phoenix coordinates")
ax2.legend()
ax2.set_title("Translation: " + str(res.x.round(2)) + " mm")
ax2.set(xlabel="X (mm)", ylabel="Y (mm)")

ax3.scatter(kV_points[:,0], kV_points[:,1], marker='o', c='r', label="kV coordinates")
ax3.scatter(transformed[:,0], transformed[:,1], marker='x', c='k', label="Phoenix coordinates")
ax3.legend()
ax3.set_title("Translation: " + str(res2.x[0:2].round(2)) + " mm" + "\n Rotation: " + str(res2.x[2].round(2)) + " deg")
ax3.set(xlabel="X (mm)", ylabel="Y (mm)")

fig.suptitle("Detector alignment for GTR0 setup")
fig.tight_layout()
plt.show()