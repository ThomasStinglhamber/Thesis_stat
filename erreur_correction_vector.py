#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:34:53 2023

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

def boucle():
    #boucle :
    l=0
    #["Energy == 70","Energy == 100","Energy == 150","Energy == 200","Energy == 226"]
    #[0.015,0.1,0.5,1,2,5]
    #plt.figure(figsize=(10, 5))
    #[70,100,150,200,226]
    #for i in [70,226]:#,"Energy == 100","Energy == 150","Energy == 200","Energy == 226"]:
        #for j in [0,45,90,180,270]:
        
    #df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Erreur_setupTEST.xlsx', header=0)
    df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Erreurexp_1_Rot.xlsx', header=0)
    df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Erreurexp_2_Rot.xlsx', header=0)
    df3 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Erreurexp_3_Rot.xlsx', header=0)

    
    
# =============================================================================
#         df1= df1.query('Angle=='+str(i))#.query('Energy == 100').query("Angle == 0")
#         df2= df2.query('Angle=='+str(i))#.query('Energy == 100').query("Angle == 0")
#         df3= df3.query('Angle=='+str(i))#.query('Energy == 100').query("Angle == 0")
# =============================================================================
    
# =============================================================================
#     df1= df1.query('Energy==200')#.query('Energy == 100').query("Angle == 0")
#     df2= df2.query('Energy==200')#.query('Energy == 100').query("Angle == 0")
#     df3= df3.query('Energy==200')#.query('Energy == 100').query("Angle == 0")
#     
# =============================================================================
    #df3=-df3

    for j in range(2):
        if j==0:
            Wanted = 'Moyenne_X'
        if j==1:
            Wanted = 'Moyenne_Y'
        #print(i)
        #print(df_value)
        data_min = min(min(df1[Wanted]), min(df2[Wanted]), min(df3[Wanted]))
        data_max = max(max(df1[Wanted]), max(df2[Wanted]), max(df3[Wanted]))
        
        # Set the bin edges
        bin_edges = np.linspace(data_min, data_max, num=40)
        # concatenate the dataframes into one
        #df = pd.concat([df1, df2, df3], axis=1)
        #plt.figure()
        plt.subplot(1, 2, l+1)
        l=l+1
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
    
    
        print(round(mean1,2))
        print(round(mean2,2))
        print(round(mean3,2))
    #     
    
    
    # =============================================================================
    #     print(round(std1,2))
    #     print(round(std2,2))
    #     print(round(std3,2))
    # =============================================================================
    
        #print(round(std1,2),round(std2,2),round(std2,2))
        # plot a line representing the mean of each distribution
        plt.axvline(mean1, color='red', linestyle='dashed', linewidth=1)
        plt.axvline(mean2, color='green', linestyle='dashed', linewidth=1)
        plt.axvline(mean3, color='blue', linestyle='dashed', linewidth=1)
        
        # add a legend
        #plt.title('Averaged spot position error for a Mu of '+str(i))
        #plt.title('Map-averaged spot position error for an Energy of '+str(i)+' MeV')
        plt.legend([' Setup1 : '+'$\Sigma$ ='+str(round(mean1,2))+' mm ''$\sigma$ ='+str(round(std1,2))+' mm', ' Setup2 : '+'$\Sigma$ ='+str(round(mean2,2))+' mm ' '$\sigma$ ='+str(round(std2,2))+' mm', ' Setup3 : '+'$\Sigma$ ='+str(round(mean3,2))+' mm ''$\sigma$ ='+str(round(std3,2))+' mm'],title='Phoenix-Plan',fontsize=10)
        plt.xlabel('Average spot position error in ' +str(Wanted[-1])+'-coordinate [mm]',fontsize=13)
        plt.ylabel('Normalized (area=1)',fontsize=13)
    
        # display the plot
    
        plt.suptitle('Average spot position error for an Angle of 0°, '+ 'Energy of [100,200] MeV and MU of [1,2]',fontsize=13 )
    #plt.title('  test' )
        plt.tight_layout()  
    #plt.show()
    
    

    
boucle()

#X_nominal=[150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150]
#Y_nominal =[150,150,150,150,150,150,90,90,90,90,90,90,30,30,30,30,30,30,-30,-30,-30,-30,-30,-30,-90,-90,-90,-90,-90,-90,-150,-150,-150,-150,-150,-150]

def boucle2():
    #boucle :
    j=1
    #["Energy == 70","Energy == 100","Energy == 150","Energy == 200","Energy == 226"]
    #[0.015,0.1,0.5,1,2,5]
    #plt.figure(figsize=(10, 5))
    #[70,100,150,200,226]
    for i in [0,45,90,180,270]:#,"Energy == 100","Energy == 150","Energy == 200","Energy == 226"]:
            #for j in [0,45,90,180,270]:
            
        #df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/Erreur_setupTEST.xlsx', header=0)
        df1 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New/Phoenix_Plan.xlsx', header=0)
        df2 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New/Phoenix_Plan_sanscorrecttion.xlsx', header=0)
        df3 = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New/Phoenix_Plan_moinscorrecttion.xlsx', header=0)
    
        
        
        df1= df1.query('Angle=='+str(i))#.query('Energy == 100')#.query("Angle == 0")
        df2= df2.query('Angle=='+str(i))#.query('Energy == 100')#.query("Angle == 0")
        df3= df3.query('Angle=='+str(i))#.query('Energy == 100')#.query("Angle == 0")

        
    # =============================================================================
    #     df1= df1.query('Energy==200')#.query('Angle == 180')#.query("Mu == 2")
    #     df2= df2.query('Energy==200')#.query('Angle == 180')#.query("Mu == 2")
    #     df3= df3.query('Energy==200')#.query('Angle == 180')#.query("Mu == 2")
    #     
    # =============================================================================
        #df3=-df3
    
        
        Wanted = 'Moyenne_Y'
    
        #print(i)
        #print(df_value)
        data_min = min(min(df1[Wanted]), min(df2[Wanted]), min(df3[Wanted]))
        data_max = max(max(df1[Wanted]), max(df2[Wanted]), max(df3[Wanted]))
        
        # Set the bin edges
        bin_edges = np.linspace(data_min, data_max, num=40)
        # concatenate the dataframes into one
        #df = pd.concat([df1, df2, df3], axis=1)
        plt.figure()
        #plt.subplot(1, 2, j)
        #j=j+1
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
    
    
        print(round(mean1,2))
        print(round(mean2,2))
        print(round(mean3,2))
    #     
    
    
    # =============================================================================
    #     print(round(std1,2))
    #     print(round(std2,2))
    #     print(round(std3,2))
    # =============================================================================
    
        #print(round(std1,2),round(std2,2),round(std2,2))
        # plot a line representing the mean of each distribution
        plt.axvline(mean1, color='red', linestyle='dashed', linewidth=1)
        plt.axvline(mean2, color='green', linestyle='dashed', linewidth=1)
        plt.axvline(mean3, color='blue', linestyle='dashed', linewidth=1)
        
        # add a legend
        #plt.title('Averaged spot position error for a Mu of '+str(i))
        plt.title('Average spot position error for an Angle of '+str(i))
        #plt.title('Map-averaged spot position error for an Energy of '+str(i)+' MeV')
        plt.legend([' addition : '+'$\Sigma$ ='+str(round(mean1,2))+' mm ''$\sigma$ ='+str(round(std1,2))+' mm', ' sans : '+'$\Sigma$ ='+str(round(mean2,2))+' mm ' '$\sigma$ ='+str(round(std2,2))+' mm', ' soustraction : '+'$\Sigma$ ='+str(round(mean3,2))+' mm ''$\sigma$ ='+str(round(std3,2))+' mm'])
        plt.xlabel('Average spot position error in ' +str(Wanted[-1])+'-coordinate [mm]')
        plt.ylabel('Normalized (area=1)')
        plt.tight_layout()
        # display the plot
    plt.show()
        
        

    
#boucle2()

