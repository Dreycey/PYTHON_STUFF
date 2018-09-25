# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 06:04:55 2018

@author: Dreycey
"""




def make_mirna (sequence):
    
    #make input uppercase
    sequence = sequence.upper()
    
    #Make mutated strand with needed CC and GGG
    seq_mut = list(sequence)
    seq_mut.insert(0,'GGG-')
    #seq_mut.append('CC')
    seq_mut = ''.join(seq_mut)
    
    #make complement to construct
    compliment = []
    for i in seq_mut:
        if i == 'U':
            compliment.append('A')
        if i == 'A':
            compliment.append('U')
        if i == 'G':
            compliment.append('C')
        if i == 'C':
            compliment.append('G')
    compliment = ''.join(compliment)
    
    #making reverse
    const = compliment[::-1]
    const = list(const)
    const.append('-TATAGTGAGTCGTATTA')
    const.insert(0,'mGmG-')
    const = ''.join(const)
    
    #adding identifying ends 
    sequence = "5'- " + sequence + " -3'"
    seq_mut = "5'- " + seq_mut + " -3'"
    compliment = "3'- " + compliment + " -5'"
    const = "5'- " + const + " -3'"
    
    #Printing different sequences
    print ('loop sequence: %s' % (sequence))
    print ('loop sequence w/ mutations: %s' % (seq_mut))
    print ('loop mutations compliment: %s' % (compliment))
    print ('construct to order: %s' % (const))
    
input = 'cgaugcuagcuagcgcugaucguguagucguaguuugcuagcugaucg'
make_mirna (input)