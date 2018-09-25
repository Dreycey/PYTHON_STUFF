# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 11:47:01 2018

@author: Dreycey
"""

import numpy as np
import matplotlib.pyplot as plt

#####################################
#Opening data from simRNA file
#####################################
file = open('RMSD_calc_mir17_old.rmsd_e', "r")
lines=file.readlines()

####################################################
#Seperating input values into energy and RMSD values
####################################################
energy=[]
rmsd=[]
rmsd_new=[]
energy_new=[]
for x in lines:
    energy.append(x.split(' -')[1])
    rmsd.append(x.split(' -')[0])
file.close()

#####################################
#Fixing input values into floats
#####################################
for e in energy:
    newe = float('-'+e)
   # print (float(newe))
    energy_new.append(newe)
for r in rmsd:
    #print (r)
    rmsd_new.append(float(r))

#####################################
#Plotting the ENERGY vs RMSD
#####################################
plt.scatter(rmsd_new,energy_new, color='r')
plt.xlabel('RMSD', size='18')
plt.ylabel('ENERGY', size='18')
plt.title('ENERGY versus RMSD for (Bartel, 2018) Model', size = '22')
plt.show()
