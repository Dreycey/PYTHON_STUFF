# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:38:34 2017

@author: Dreycey
"""

from random import choice, randint
import numpy as np

def random_dna(n_bases):
    return ''.join(choice(['a','c','g','t']) for i in range(n_bases))
    
# double-strand break at PAM-2
# bases on each side of breakpoint can be deleted and/or bases can be inserted
# original bases lowercase
# inserted bases uppercase
def dsb_indel(guide, del_rate=[.5,.5], ins_rate=[0,1]):
    up = guide[:-2-np.random.choice([0, 1], p=del_rate)]
    dn = guide[-2+np.random.choice([0, 1], p=del_rate):]
    insert = ''.join(choice(['A','C','G','T']) for i in range(np.random.choice([0, 1], p=ins_rate)))
    new_guide = up + insert + dn
    return new_guide

# targeting fails once barcodes degenerate below 17 bases
def barcode_evolver(barcode):
    lineage = [barcode]
    while len(lineage[-1]) >= 17: 
        lineage.append(dsb_indel(lineage[-1]))
    for i in lineage:
        print (i)
    return lineage

barcode_evolver('ATGCTGGAGTGTGTAGCGATGCTAGTCGATGCTAGCATGCTAGCTGA')
'''
#seq = random_dna(50)
seq = 'tttacccagatctatgcaac'
barcode_evolver(seq)
'''
# average number of barcodes of many recordings
x = []
for i in range(1000):
    x.append(len(barcode_evolver(seq)))
print(np.asarray(x).mean())