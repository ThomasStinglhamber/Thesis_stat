#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:03:51 2023

@author: thomasstinglhamber
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook

df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Log.xlsx')

df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Phoenix_Rot.xlsx')

df3 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Plan_Log.xlsx')

df2.sort_values(['Angle','Mu','Energy'],ascending=[True,True,True], inplace=True,kind='mergesort')
df1.sort_values(['Angle','Mu','Energy'],ascending=[True,True,True], inplace=True,kind='mergesort')
df3.sort_values(['Angle','Mu','Energy'],ascending=[True,True,True], inplace=True,kind='mergesort')

df1=df1.reset_index(drop = True)
df2=df2.reset_index(drop = True)
df3=df3.reset_index(drop = True)

# =============================================================================
# df2.to_excel('/Users/thomasstinglhamber/Desktop/output2.xlsx', index=False)
# df1.to_excel('/Users/thomasstinglhamber/Desktop/output.xlsx', index=False)
# 
# =============================================================================



print(df1)
print(df2)
print(df3)
result = df2.iloc[:,3:5] - df1.iloc[:,3:5]



result.insert(0, 'Angle', df1['Angle'])
result.insert(1, 'Mu', df1['Mu'])
result.insert(2, 'Energy', df1['Energy'])
result.insert(5, 'Std_X', np.sqrt(df1['Std_X']**2+df2['Std_X']**2))
result.insert(6, 'Std_Y', np.sqrt(df1['Std_Y']**2+df2['Std_Y']**2))
result.insert(7, 'Nominal_X', df3['Nominal_X'])
result.insert(8, 'Nominal_Y', df3['Nominal_Y'])
result.insert(9, 'True_Angle', df1['Angle']-df3['True_Angle'])
result.insert(10, 'True_Energy', df1['Energy']-df3['True_Energy'])
result.insert(11, 'True_Mu', df1['Mu']-df3['True_Mu'])


print(result)

result.to_excel('/Users/thomasstinglhamber/Desktop/Phoenix_Log_Rot2.xlsx', index=False)

