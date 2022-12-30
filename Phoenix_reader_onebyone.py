#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:59:59 2022

@author: thomasstinglhamber
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# Get the list of all files and directories
path = '/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Mesure/Phoenix/Raw_excel'
dir_list = os.listdir(path)
merge=[]
for x in dir_list:
    if x.endswith(".xlsx"):
        # Prints only text file present in My Folder
        #print(x)
        merge.append(pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Mesure/Phoenix/Raw_excel/'+str(x),header=6))

for i in range(0,len(merge)):

    merge[i].sort_values(['Y 2D Fit (mm)','X 2D Fit (mm)'], 
               ascending=[False,False], inplace=True,kind='mergesort')

for i in range(0,len(merge)):
    for j in [0,1,2,3,4,5]:
        merge[i].iloc[0+6*j:6+6*j, [1,2]]= merge[i].iloc[0+6*j:6+6*j, [1,2]].sort_values(['X 2D Fit (mm)'], 
                   ascending=[False])
        
    merge[i]=merge[i].reset_index(drop = True)
      

correction_vector = [0.03,-1.01]
#je met tout les colonnes X et Y dans un tableau specifique pour calculer les mean et std
df_stat_X= pd.DataFrame(merge[0].iloc[:, [1]])+correction_vector[0]
df_stat_X['tab1']=merge[1].iloc[:, [1]]+correction_vector[0]
df_stat_X['tab2']=merge[2].iloc[:, [1]]+correction_vector[0]
df_stat_X['tab3']=merge[3].iloc[:, [1]]+correction_vector[0]
df_stat_X['tab4']=merge[4].iloc[:, [1]]+correction_vector[0]

print(df_stat_X)

# Ici tableau selon X
df_stat_Y= pd.DataFrame(merge[0].iloc[:, [2]])+correction_vector[1]
df_stat_Y['tab1']=merge[1].iloc[:, [2]]+correction_vector[1]
df_stat_Y['tab2']=merge[2].iloc[:, [2]]+correction_vector[1]
df_stat_Y['tab3']=merge[3].iloc[:, [2]]+correction_vector[1]
df_stat_Y['tab4']=merge[4].iloc[:, [2]]+correction_vector[1]

# =============================================================================
# print("Mean X")
# print(df_stat_X.mean(axis=1))
# 
# print("Mean Y")
# print(df_stat_Y.mean(axis=1))
# 
# print("Std X")
# print(df_stat_X.std(axis=1))
# 
# print("Std Y")
# 
# print(df_stat_Y.std(axis=1))
# 
# =============================================================================
# implementer un moyen de stocker les mean/std dans un fichier externe
# faire attention a la nomenclature !

# =============================================================================
# df_stat_X['Moyenne_X']= df_stat_X.mean(axis=1)
# df_stat_Y['Moyenne_Y']= df_stat_Y.mean(axis=1)
# 
# df_stat_X['Std_X']= df_stat_X.std(axis=1)
# df_stat_Y['Std_Y']= df_stat_Y.std(axis=1)
# 
# =============================================================================


#creation du plot pour vérifier les points et la mean/std
plt.figure()
plt.scatter(df_stat_X.mean(axis=1),df_stat_Y.mean(axis=1),c='red',marker='x')
#plt.scatter(df['X 2D Fit (mm)'],df['Y 2D Fit (mm)'],marker='.')
for l in range(0,len(merge)):
    plt.scatter(merge[l]['X (mm)']+correction_vector[0],merge[l]['Y (mm)']+correction_vector[1],marker='.',label=merge[l].iloc[1,[0]].to_string(index=False))
plt.legend()

plt.show()

