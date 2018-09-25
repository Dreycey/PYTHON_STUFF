# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:22:36 2018

@author: Dreycey
"""

import numpy as np
import matplotlib.pyplot as plt

#############################################
#
# Pseudocode for writing algorithm to plot LARMORD
# Chemical shift data with secondary plots. The goal of
# this is to aid in identifying peaks in NMR data for 
# RNA. 
#
# This will be used to predict 2D NMR spectra based on
# preidicted models of RNA. 
#
# Author: Dreycey Albin
# Date created: 6/13/2018
# 
#############################################


print('hello')

####################
#
####################
'''
file = open(fileLocaiton)
'''

file = open('zika_LarmorD.txt', "r")
lines = file.readlines()

print (lines[1])


#########################
#Making relevent vectors
#########################
'''
pseudocode:
For row in file:
 	if row had G or U:
		split row into 9 strings using the space inbetween
		add these strings to a temporary list
		if (index 4 == GUA and index 3 in temporary_list == H1) or (index 4 == URA and index 3 in temporary_list == H3):
			take 3rd, add to 1D vector residue_number
			take 4th, add to 1D vector residue_name
			take 5th, add to 1D vector hydrogen_number
			take 6th, add to 1D vector H_shifts_1
			take 8th, add to 1D vector H_shifts_2
'''

residue_number = []
residue_name = []
hydrogen_number = []
H_shifts_1 = []
H_shifts_2 = []

for x in lines:
    print ('CALCULATING_1')
    residue_number.append(x.split(' ')[2])
    residue_name.append(x.split(' ')[3])
    hydrogen_number.append(x.split(' ')[4])
    H_shifts_1.append(x.split(' ')[5])
    H_shifts_2.append(x.split(' ')[7])
file.close()

print (residue_name)
residue_number_2 = []
residue_name_2 = []
hydrogen_number_2 = []
H_shifts_1_2 = []
H_shifts_2_2 = []
residue_number_3 = []
H_shifts_1_3 = []
H_shifts_2_3 = []

for i in range(0, len(lines)): #residue_name:

    if residue_name[i] == 'URA'and hydrogen_number[i] == 'H3':
        residue_number_2.append(residue_number[i])
        residue_name_2.append(residue_name[i])
        hydrogen_number_2.append(hydrogen_number[i])
        H_shifts_1_2.append(H_shifts_1[i])
        H_shifts_2_2.append(H_shifts_2[i])
    
    if residue_name[i] == 'GUA'and hydrogen_number[i] == 'H1':
        residue_number_3.append(residue_number[i])
        residue_name_2.append(residue_name[i])
        hydrogen_number_2.append(hydrogen_number[i])
        H_shifts_1_3.append(H_shifts_1[i])
        H_shifts_2_3.append(H_shifts_2[i])
        
#res_identity = residue_name_2 + '_' + residue_number_2

##############################
# Using distances to identify 2D peaks
##############################

############################################################
#Using dot-parenthesis notation to predict off-diagnol NOESY interacitons
############################################################
'''
PSEUDOCODE:
#open the file
secondary_structure = open(file)

#interaction matrix dictated from dot-parenths notation


number_of_residues = len(secondary_structure)

#make dicitonary with residue number as key and ., ), and ( as the value
dictionary_1 = {} 
for i range(1, number_of_residues):
	dictionary_1(i, secondary_structure)

for i range(1, number_of_residues):
	if dicitonary_1(i) == (
		put i in list left_strand
	if dictionary_1(i) == )
		put i in list right_strand 
sort lists in growing numbers
reverse right list (so indexes correspond to based nucleotides)

#make matrix of interacting hydrogen that would appear in noesy walk
#IF G OR U:
#this will be index i of left interacting with index i+1 or i-1 of right (&vice versa)
# OR index I of left interacting with i+1 or i-1 of left (or vice versa) 
#only if G or U though
'''
	




#######################
# Graphing 2 spectra
#######################
'''
pseudocode:
y = vector H_shifts_1
x = vector H_shifts_1 #mabye use 2?
scatter plot (y, x)

plot.show()
save.. 

y = vector H_shifts_2
x = vector H_shifts_2 #mabye use 1?
scatter plot (y, x)

plot.show()
save.. 
'''
x_move = -0.2
y_move = 0.2
circle_size = 200

fig, ax = plt.subplots()
ax.scatter(H_shifts_1_2,H_shifts_1_2, facecolors='none', edgecolors='r', s = circle_size, label='chemical shift for UH3')
ax.scatter(H_shifts_1_3,H_shifts_1_3, facecolors='none', edgecolors='g', s = circle_size, label='chemical shift for GH1')
plt.title('Predicted NOESY for ZIKV1 (U only)', size = 20)
plt.ylabel('H ppm', size = 12)
plt.xlabel('H ppm', size = 12)
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.legend(loc=2)


for i in range(0,len(residue_number_2)):
    ax.annotate(residue_number_2[i], ((float(H_shifts_1_2[i]) + x_move) ,(float(H_shifts_1_2[i])) + y_move ), size = 10)
for i in range(0,len(residue_number_2)):
    ax.annotate(residue_number_3[i], ((float(H_shifts_1_3[i]) + x_move) ,(float(H_shifts_1_3[i])) + y_move ), size = 10)

plt.show()

