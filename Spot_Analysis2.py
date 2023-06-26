#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:16:05 2023

@author: thomasstinglhamber
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:14:24 2023

@author: thomasstinglhamber
"""
from scipy.interpolate import RegularGridInterpolator
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import pandas as pd
from matplotlib.animation import FuncAnimation
import matplotlib

from ipywidgets import interact, fixed

matplotlib.use('Agg')
plt.rcParams.update({'font.size': 12})

X_nominal=[150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150,150,90,30,-30,-90,-150]
Y_nominal =[150,150,150,150,150,150,90,90,90,90,90,90,30,30,30,30,30,30,-30,-30,-30,-30,-30,-30,-90,-90,-90,-90,-90,-90,-150,-150,-150,-150,-150,-150]


def interpolate_Moyenne_X(wanted):
    # read excel file into a pandas dataframe
    # Phoenix_Plan
    # Plan_Log
    df = pd.read_excel('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/Groningen/New2/Phoenix_Log_Rot.xlsx', header=0)
    df.sort_values(['Angle','Mu','Energy','Nominal_Y','Nominal_X'],ascending=[True,True,True,False,False], inplace=True,kind='mergesort')
    
    #df.to_excel('/Users/thomasstinglhamber/Desktop/Test_interp.xlsx',index=False)
    
    #print(df)
    # create 5D grid of input values
    angles = df['Angle'].sort_values().unique()
    #angles=[0,45,90,180,270,360] 
    #angles = np.mod(angles, 360)
    
    
    mus = df['Mu'].sort_values().unique()
    energies = df['Energy'].sort_values().unique()
    nominal_xs = df['Nominal_X'].unique()
    nominal_ys = df['Nominal_Y'].unique()
    
    #print(nominal_xs)
    # sort the arrays to ensure the order is the same as the dataframe
    angles.sort()
    mus.sort()
    energies.sort()
    nominal_ys.sort()
    nominal_xs.sort()
    

    # define the interpolation function
    def interpolated_Moyenne_X(angle, mu,energy, nominal_x, nominal_y):
        
        # create arrays of the values
            
        values = df[wanted].values.reshape(len(angles), len(mus), len(energies), len(nominal_xs), len(nominal_ys))
        angle = np.mod(angle, 360)
        # create interpolation function
        interpolator = RegularGridInterpolator((angles, mus,energies,nominal_xs,nominal_ys), values, method='linear', bounds_error=False, fill_value=None)
        
        return interpolator((angle, mu,energy, nominal_x, nominal_y))
    
    
    return interpolated_Moyenne_X


def valeur_particuliere(x,y,angle,mu,energy):
        # create interpolation function
    for i in ['Moyenne_X','Moyenne_Y','Std_X','Std_Y']:
        
        interpolated_Moyenne_X = interpolate_Moyenne_X(i)
    
        result = interpolated_Moyenne_X(angle,  mu ,energy, -y, -x)
            
        print(i,':',result)
        
    return

fig = plt.figure(figsize=(15, 15))
#@interact(angle=(0, 360), mu=(0, 5, 0.05), energy=(0, 250, 10))       
def plan(x,y,angle,mu,energy,o,p):
    # create interpolation function
    for i in ['Moyenne_X']:#,'Moyenne_Y','Std_X','Std_Y']:
        interpolated_Moyenne_X = interpolate_Moyenne_X(i)
        
        result_tot=[]
        for k,j in zip(X_nominal,Y_nominal):
            #print(i,j)
            result = interpolated_Moyenne_X(angle,  mu ,energy, -j, -k)
            result_tot.append(result.item())
        z=result_tot
        #print(result_tot)
        # Interpolate the data to create a surface
        xi, yi = np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100)
        xi, yi = np.meshgrid(xi, yi)
        zi = griddata((x, y), z, (xi, yi), method='cubic')
        
        # Plot the surface
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x,y,z,marker='x',color='r')
        ax.plot_surface(xi, yi, zi, cmap='viridis')
        plt.title('Systematic shift for : Angle = '+str(angle)+'°'+', Mu = '+str(round(mu,3))+', Energy = '+str(energy)+' MeV')
        plt.tight_layout()
        #ax.set_ylim(-0.5, 1.5)
        ax.set_zlim(-0.2, 1.5)
        ax.set_xlabel('X-coordinate [mm]')
        ax.set_ylabel('Y-coordinate [mm]')
        if i[0]=='M':
            ax.set_zlabel('systematic shift in '+str(i[-1])+'-coordinate [mm]')
        
        else : ax.set_zlabel('random shift in '+str(i[-1])+'-coordinate [mm]')
        
# =============================================================================
#         # Plot the surface
#         
#         ax = fig.add_subplot(3, 3, o*3+p+1, projection='3d')
#         ax.scatter(x,y,z,marker='x',color='r')
#         ax.plot_surface(xi, yi, zi, cmap='viridis')
#         # Plan-Log
#         # Phoenix-Plan
#         plt.suptitle('Systematic error of Plan-Log for : ',fontsize=17)
#         plt.title('Angle = '+str(angle)+'°'+', Mu = '+str(round(mu,3))+', Energy = '+str(energy)+ ' MeV',fontsize=13)
# 
#         ax.set_xlabel('X-coordinate [mm]',fontsize=11)
#         ax.set_ylabel('Y-coordinate [mm]',fontsize=11)
#         if i[0]=='M':
#             ax.set_zlabel('systematic shift in '+str(i[-1])+'-coordinate [mm]',fontsize=11)
#         
#         else : ax.set_zlabel('random shift in '+str(i[-1])+'-coordinate [mm]',fontsize=11)
# =============================================================================
        
    #plt.show()
    plt.savefig('/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/film/NEW3/Angle/'+str(angle)+'.png')
    pass 




#valeur_particuliere(90,30,270,1,100)
#plan(X_nominal,Y_nominal,180,0.015,226,1,1)
# energy = np.arange(50,250,2)
# angle =np.arange(0,360,5)
#mu =np.arange(0.05,6,0.05)

#angle = np.arange(0,360,40)
# mu = np.arange(0.015,5,0.555)
#energy =np.arange(50,230,22)

o=0
p=0
#plan(X_nominal,Y_nominal,45,1,150,o,p)
for l in np.arange(0,360,5):
    plan(X_nominal,Y_nominal,l,1,200,o,p)
# =============================================================================
#     p=p+1
#     if p==3:
#         o=o+1
#         p=0
#     if p==3 and o==3:
#     #s=l/10
#         plt.savefig('/Users/thomasstinglhamber/Desktop/PHYS22M/evolmu2.pdf')
#         #plt.savefig('/Users/thomasstinglhamber/Desktop/test'+'.pdf')
# 
#         plt.tight_layout()
#         plt.show()
# =============================================================================

