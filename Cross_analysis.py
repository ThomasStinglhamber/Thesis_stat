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



#X_nominal=[150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150]
#Y_nominal =[150,150,150,150,150,150,90,90,90,90,90,90,30,30,30,30,30,30,-30,-30,-30,-30,-30,-30,-90,-90,-90,-90,-90,-90,-150,-150,-150,-150,-150,-150]
plt.rcParams.update({'font.size': 13})

def boucle():
    #boucle :
    j=1
    #["Energy == 70","Energy == 100","Energy == 150","Energy == 200","Energy == 226"]
    #[0.015,0.1,0.5,1,2,5]
    plt.figure(figsize=(10, 5))
    plt.tight_layout()
    #[70,100,150,200,226]
    for i in [45,270]:#,"Energy == 100","Energy == 150","Energy == 200","Energy == 226"]:
        #for j in [0,45,90,180,270]:
            
        #df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Erreur_setupTEST.xlsx', header=0)
        df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Plan_Log.xlsx', header=0)
        df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Phoenix_Log_Rot.xlsx', header=0)
        df3 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Phoenix_Plan_Rot.xlsx', header=0)
    
        
        
# =============================================================================
#         df1= df1.query('Angle=='+str(i))#.query('Energy == 100').query("Angle == 0")
#         df2= df2.query('Angle=='+str(i))#.query('Energy == 100').query("Angle == 0")
#         df3= df3.query('Angle=='+str(i))#.query('Energy == 100').query("Angle == 0")
# =============================================================================
        
        df1= df1.query('Angle=='+str(i))#.query('Energy == 100').query("Angle == 0")
        df2= df2.query('Angle=='+str(i))#.query('Energy == 100').query("Angle == 0")
        df3= df3.query('Angle=='+str(i))#.query('Energy == 100').query("Angle == 0")
        
        #df3=-df3

        
        Wanted = 'Moyenne_Y'
    
        #print(i)
        #print(df_value)
        data_min = min(min(df1[Wanted]), min(df2[Wanted]), min(df3[Wanted]))
        data_max = max(max(df1[Wanted]), max(df2[Wanted]), max(df3[Wanted]))
        
        # Set the bin edges
        bin_edges = np.linspace(data_min, data_max, num=70)
        # concatenate the dataframes into one
        #df = pd.concat([df1, df2, df3], axis=1)
        #plt.figure()
        plt.subplot(1, 2, j)
        j=j+1
        # plot the histograms
        df1[Wanted].hist(bins=bin_edges, color='red',alpha=0.6,density=True)
        df2[Wanted].hist(bins=bin_edges, color='green',alpha=0.6,density=True)
        df3[Wanted].hist(bins=bin_edges, color='blue',alpha=0.6,density=True)
        # calculate the mean of each distribution
        mean1 = df1[Wanted].mean()
        mean2 = df2[Wanted].mean()
        mean3 = df3[Wanted].mean()
        
        std1 = df1[Wanted].std()
        std2 = df2[Wanted].std()
        std3 = df3[Wanted].std()
        
    # =============================================================================
    #     print('Plan-Log :' ,':', round(mean1,2),'+-',round(std1,2))
    #     print('Plan-Phoenix :' ,':', round(mean3,2),'+-',round(std3,2))
    #     print('Phoenix-Log :' ,':', round(mean2,2),'+-',round(std2,2))
    #     #print(round(mean1,2),round(mean2,2),round(mean3,2))
    # =============================================================================

        print(i)
        print(round(mean1,2))
        print(round(mean2,2))
        print(round(mean3,2))
        print('---')
    #     


# =============================================================================
#         print(round(std1,2))
#         print(round(std2,2))
#         print(round(std3,2))
#         print('---')
# =============================================================================
        #print(round(std1,2),round(std2,2),round(std2,2))
        # plot a line representing the mean of each distribution
        plt.axvline(mean1, color='red', linestyle='dashed', linewidth=1)
        plt.axvline(mean2, color='green', linestyle='dashed', linewidth=1)
        plt.axvline(mean3, color='blue', linestyle='dashed', linewidth=1)
        
        # add a legend
        #plt.title('Average spot position error for a Mu of '+str(i))
        plt.title('Average spot position error for an Angle of '+str(i)+'°')
        #plt.title('Average spot position error for an Energy of '+str(i)+' MeV')
        plt.legend([' Plan-Log : '+'$\Sigma_{ave}$ ='+str(round(mean1,2))+' mm ''$\sigma_{ave}$ ='+str(round(std1,2))+' mm', ' Phoenix-Log: '+'$\Sigma_{ave}$ ='+str(round(mean2,2))+' mm ' '$\sigma_{ave}$ ='+str(round(std2,2))+' mm', ' Phoenix-Plan: '+'$\Sigma_{ave}$ ='+str(round(mean3,2))+' mm ''$\sigma_{ave}$ ='+str(round(std3,2))+' mm'], prop={'size': 14})
        plt.xlabel('Spot position error in ' +str(Wanted[-1])+'-coordinate [mm]')
        plt.ylabel('Normalized (area=1)')
        plt.tight_layout()
        # display the plot
    #plt.show()
        
        

    
boucle()



def stat():
    
    df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Plan_Log2.xlsx', header=0)
    df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log2.xlsx', header=0)
    df3 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Plan_Phoenix.xlsx', header=0)



    df1= df1.query("Angle == 0")
    df2= df2.query("Angle == 0")
    df3= df3.query("Angle == 0")
    
    print(df3['Moyenne_X'].describe())

    plt.hist(df3['Moyenne_X'],bins=50,density=True)
    plt.show()
    return

#stat()
    

def trueMus():
    data=[]
    means=[]
    for i in [0.015,0.1,0.5,1,2,5]:
        df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Phoenix_Log2.xlsx', header=0)
    
        df1= df1.query("Mu =="+str(i))
        data.append(df1['True_Mu'])
        means.append(round(df1['True_Mu'].mean(),6))
        print(round(df1['True_Mu'].mean(),6))
    #data = [set1, set2, set3, set4, set5, set6]
    
    # Create a figure and axis object
    fig, ax = plt.subplots()
    
    # Create the boxplot
    ax.boxplot(data, showmeans=True)
    
    # Add a title and axis labels
    ax.set_title('Difference between planned MU and delivered MU')
    ax.set_xlabel('MU')
    ax.set_ylabel('Difference [MU]')
    ax.set_xticklabels([0.015,0.1,0.5,1,2,5])

    #ax.legend(means)
    # Show the plot
    plt.show()
# =============================================================================
#     print(df1['True_Mu'].describe())
# 
#     plt.boxplot(df1['True_Mu'])#,bins=100,density=True)
#     plt.show()
# 
# =============================================================================
    return 

#trueMus()


def trueEnergy():
    data=[]
    for i in [70,100,150,200,226]:
        df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Plan_Log2.xlsx', header=0)
    
        df1= df1.query("Energy =="+str(i))
        data.append(df1['True_Energy'])
        
    print(data)
# =============================================================================
#     #data = [set1, set2, set3, set4, set5, set6]
#     
#     # Create a figure and axis object
#     fig, ax = plt.subplots()
#     
#     # Create the boxplot
#     ax.boxplot(data,'red')
#     
#     # Add a title and axis labels
#     ax.set_title('Difference between planned MU and delivered MU')
#     ax.set_xlabel('MU')
#     ax.set_ylabel('Difference [MU]')
#     ax.set_xticklabels([0.015,0.1,0.5,1,2,5])
# 
#     #ax.legend([0.015,0.1,0.5,1,2,5])
#     # Show the plot
#     plt.show()
# =============================================================================
# =============================================================================
#     print(df1['True_Mu'].describe())
# 
#     plt.boxplot(df1['True_Mu'])#,bins=100,density=True)
#     plt.show()
# 
# =============================================================================
    return 

#trueEnergy()





