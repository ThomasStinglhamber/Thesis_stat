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

df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/MergeLOG2.xlsx')

df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix/Merge2test.xlsx')


df2.sort_values(['Angle','Mu','Energy'],ascending=[True,True,True], inplace=True,kind='mergesort')
df1.sort_values(['Angle','Mu','Energy'],ascending=[True,True,True], inplace=True,kind='mergesort')


df1=df1.reset_index(drop = True)
df2=df2.reset_index(drop = True)

# =============================================================================
# df2.to_excel('/Users/thomasstinglhamber/Desktop/output2.xlsx', index=False)
# df1.to_excel('/Users/thomasstinglhamber/Desktop/output.xlsx', index=False)
# 
# =============================================================================



print(df1)
print(df2)

result = df1.iloc[:,3:7] - df2.iloc[:,3:7]


result.insert(0, 'Angle', df1['Angle'])
result.insert(1, 'Mu', df1['Mu'])
result.insert(2, 'Energy', df1['Energy'])


print(result)

result.to_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log.xlsx', index=False)

