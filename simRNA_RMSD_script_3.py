# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 11:47:01 2018

@author: Dreycey
Updates:
4/25/18-If statements were added to get rid of outliers in the energy values 
and rmsd values. In addition, 1-dimensional histogram graphs of the both the
rmsd and energy values was added.
"""

import numpy as np
import matplotlib.pyplot as plt

#######################################################FOR ALL
#####################################
#Opening data from simRNA file
#####################################
file = open('cJUN_6_rmsd_2.txt', "r")
lines = file.readlines()

####################################################
#Seperating input values into energy and RMSD values
####################################################
energy=[]
rmsd=[]
rmsd_new=[]
energy_new=[]
for x in lines:
    print ('CALCULATING_1')
    energy.append(x.split(' -')[1])
    rmsd.append(x.split(' -')[0])
file.close()

#####################################
#Fixing input values into floats
#update: if statements added
#####################################
for e in energy:
    if float(e) > 400: 
        print ('CALCULATING_2')
        newe = float('-'+e)
       # print (float(newe))
        energy_new.append(newe)

for r in rmsd:
    if float(r) < 40:
        print ('CALCULATING_3')
        #print (r)
        rmsd_new.append(float(r))


#######################################################FOR CLUSTERS
#####################################
#Opening data from simRNA file
#####################################
file = open('cJUN_6_rmsd_4.txt', "r")
lines2 = file.readlines()

####################################################
#Seperating input values into energy and RMSD values
####################################################
energy2=[]
rmsd2=[]
rmsd_new2=[]
energy_new2=[]
for x in lines2:
    print ('CALCULATING_1')
    energy2.append(x.split(' -')[1])
    rmsd2.append(x.split(' -')[0])
file.close()

#####################################
#Fixing input values into floats
#update: if statements added
#####################################
for e in energy2:
    if float(e) > 400: 
        print ('CALCULATING_2')
        newe = float('-'+e)
       # print (float(newe))
        energy_new2.append(newe)

for r in rmsd2:
    if float(r) < 40:
        print ('CALCULATING_3')
        #print (r)
        rmsd_new2.append(float(r))
        
#######################################################FOR GRAPHING
#####################################
#Plotting the ENERGY vs RMSD
#####################################
plt.scatter(rmsd_new,energy_new, color='b', edgecolor='black', linewidth=1)
plt.scatter(rmsd_new2,energy_new2, color='r', edgecolor='black', linewidth=1)
plt.xlabel('RMSD', size='18')
plt.ylabel('ENERGY', size='18')
plt.title('ENERGY versus RMSD for simRNA cJUN_1 Model', size = '20')
plt.show()

#####################################
#Plotting the ENERGY 
#####################################
plt.hist(energy_new, bins=100, color='b', edgecolor='black', linewidth=0.5)
#plt.hist(energy_new2*10, bins=20, color='r', edgecolor='black', linewidth=0.5)
plt.xlabel('ENERGY', size='18')
plt.ylabel('Counts', size='18')
plt.title('ENERGY versus RMSD for simRNA cJUN_1 Model', size = '20')
plt.show()


#####################################
#Plotting the RMSD
#####################################
plt.hist(rmsd_new, bins=100, color='b', edgecolor='black', linewidth=0.5)
plt.hist(rmsd_new2, bins=20, color='r', edgecolor='black', linewidth=0.5)
plt.xlabel('RMSD', size='18')
plt.ylabel('Counts', size='18')
plt.title('ENERGY versus RMSD for simRNA cJUN_1 Model', size = '20')
plt.show()



