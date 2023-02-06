#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:29:09 2023

@author: thomasstinglhamber
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook


df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix/Mesure/2700700015.xlsx', header=6)
#print(df)
reference = 2
    
# Get the index of the rows where the value in the "sigmax" column is lower than the reference
#to_drop = df[df['Sigma X (mm)' or 'Sigma Y (mm)'] < reference].index #or df[df['Sigma Y (mm)'] < reference].index


to_drop=df.loc['Sigma X (mm)','Sigma Y (mm)'] < reference
#to_drop2 = df[df['Sigma Y (mm)'] < reference].index
# Delete the rows
print(to_drop)
df.drop(to_drop, inplace=True)
#df.drop(to_drop2, inplace=True)
#print(df)