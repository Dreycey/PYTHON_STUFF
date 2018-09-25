# -*- coding: utf-8 -*-
"""
Created on Tue May  8 01:38:12 2018

@author: Dreycey
"""


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


import numpy as np
import matplotlib.pyplot as plt

print('hello')

####################
#
####################
'''
file = open(‘fileLocaiton’)
'''
'''
#file = open('pdb_to_2D_pseudocode.py', "r")
#lines = file.readlines()

#print lines
'''

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



##############################
# Using distances to identify 2D peaks
##############################

############################################################
#Using dot-parenthesis notation to predict off-diagnol NOESY interacitons
############################################################
'''
PSEUDOCODE:
#open the file
secondary_structure = open(‘file’)

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

