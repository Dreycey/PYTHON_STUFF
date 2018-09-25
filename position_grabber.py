# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 20:39:24 2018

@author: Dreycey
"""
##########################################
# This allows for one to grab residues or
# nucleptides from postions in a string
##########################################
file = open('../LINK-A.fasta',"r")
lines = file.readlines()

name = lines[0]
sequence = lines[1:]

seq_2 = ''.join(sequence) #make into long string

#add placement for start and end of the sequence:
start = 5271
end = start + abs(1100-1117) + 1

#Print out the locations of the sequence:
print (name)
print ('from '+ str(start) + ' ' + 'to ' + str(end) +':')
print(seq_2[(start-1):(end-1)])

start = start - 100
end = end + 100

#########################################################################################
#Print out the locations of the sequence:
print (name)
print ('from '+ str(start) + ' ' + 'to ' + str(end) +':')
print(seq_2[(start-1):(end-1)])
'''
start = start - 10
end = end + 10

#Print out the locations of the sequence:
print (name)
print ('from '+ str(start) + ' ' + 'to ' + str(end) +':')
print(seq_2[(start-1):(end-1)])

start = start - 10
end = end + 10

#Print out the locations of the sequence:
print (name)
print ('from '+ str(start) + ' ' + 'to ' + str(end) +':')
print(seq_2[(start-1):(end-1)])

start = start - 10
end = end + 10

#Print out the locations of the sequence:
print (name)
print ('from '+ str(start) + ' ' + 'to ' + str(end) +':')
print(seq_2[(start-1):(end-1)])

start = start - 10
end = end + 10

#Print out the locations of the sequence:
print (name)
print ('from '+ str(start) + ' ' + 'to ' + str(end) +':')
print(seq_2[(start-1):(end-1)])

start = start - 10
end = end + 10


#Print out the locations of the sequence:
print (name)
print ('from '+ str(start) + ' ' + 'to ' + str(end) +':')
print(seq_2[(start-1):(end-1)])

start = start - 10
end = end + 10

#############################################################################################
'''
##########################################
# This allows for one to find the positions 
# of a particular sequence. 
##########################################
'''
for i in range(0, len (seq_2)): 
    sequence = 'CAGGGTAGACTCGCTCTG'
    new = i+ len(sequence)
    if seq_2[i:new] == sequence:
        print (i+1) # add one because list starts with 0 index
        print (seq_2[i:(new+4)])
'''