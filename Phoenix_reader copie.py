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
# =============================================================================
# path = '/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Mesure/Phoenix'
# dir_list = os.listdir(path)
#  
# for x in dir_list:
#     if x.endswith(".xlsx"):
#         # Prints only text file present in My Folder
#         print(x)
# 
# =============================================================================


    
df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Mesure/Phoenix/Analyse_myQA.xlsx', header=6)

name=[]
for i in range(0,len(df.iloc[:, [0]])):
    if df.iloc[i, [0]].to_string(index=False) not in name:
        name.append(df.iloc[i, [0]].to_string(index=False))


merge=[]
grouped = df.groupby(df['Image Name'])
for k in name:
    df_new = grouped.get_group(k)
    merge.append(df_new)


for i in range(0,len(merge)):

    merge[i].sort_values(['Y 2D Fit (mm)','X 2D Fit (mm)'], 
               ascending=[False,False], inplace=True,kind='mergesort')


for i in range(0,len(merge)):
    for j in [0,1,2,3,4]:
        merge[i].iloc[0+5*j:5+5*j, [1,2]]= merge[i].iloc[0+5*j:5+5*j, [1,2]].sort_values(['X 2D Fit (mm)'], 
                   ascending=[False])
    #print(merge[i]) 
    merge[i]=merge[i].reset_index(drop = True)
      
    #print(merge[i])   

df_stat_X= pd.DataFrame(merge[0].iloc[:, [1]])
df_stat_X['tab1']=merge[1].iloc[:, [1]]
df_stat_X['tab2']=merge[2].iloc[:, [1]]

df_stat_Y= pd.DataFrame(merge[0].iloc[:, [2]])
df_stat_Y['tab1']=merge[1].iloc[:, [2]]
df_stat_Y['tab2']=merge[2].iloc[:, [2]]
#print(df_stat_X)

print(df_stat_X.mean(axis=1))
print(df_stat_Y.mean(axis=1))


print(df_stat_X.std(axis=1))
print(df_stat_Y.std(axis=1))

# =============================================================================
# df_stat_X['Moyenne_X']= df_stat_X.mean(axis=1)
# df_stat_Y['Moyenne_Y']= df_stat_Y.mean(axis=1)
# 
# df_stat_X['Std_X']= df_stat_X.std(axis=1)
# df_stat_Y['Std_Y']= df_stat_Y.std(axis=1)
# 
# =============================================================================

plt.figure()
plt.scatter(df_stat_X.mean(axis=1),df_stat_Y.mean(axis=1),c='red',marker='x')
#plt.scatter(df['X 2D Fit (mm)'],df['Y 2D Fit (mm)'],marker='.')
for l in range(0,len(merge)):
    plt.scatter(merge[l]['X 2D Fit (mm)'],merge[l]['Y 2D Fit (mm)'],marker='.',label=merge[l].iloc[1,[0]].to_string(index=False))
plt.legend()

plt.show()



# scatter plot
# =============================================================================
# for i in merge:
#     i.plot(kind = 'scatter',
#             x = 'X 2D Fit (mm)',
#             y = 'Y 2D Fit (mm)'
#             #color = 'red'
#             )
#       
#     # set the title
#     plt.title('ScatterPlot')
#       
#     # show the plot
#     plt.show()
#     
# =============================================================================
# =============================================================================
# df.plot(kind = 'scatter',
#         x = 'X 2D Fit (mm)',
#         y = 'Y 2D Fit (mm)'
#         #color = 'red'
#         )
#   
# # set the title
# plt.title('ScatterPlot')
#   
# # show the plot
# plt.show()
# 
# 
# =============================================================================


