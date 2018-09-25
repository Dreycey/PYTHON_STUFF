# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 06:04:55 2018

@author: Dreycey
"""
import sys

def make_mirna (sequence):
    
    #make input uppercase
    sequence = sequence.upper()
    seq_len = len(sequence)
    #Make mutated strand with needed CC and GGG
    seq_mut = list(sequence)
    seq_mut.insert(0,'GGG')
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
    promoter = '-TATAGTGAGTCGTATTA'
    const.append(promoter)
    const.insert(0,'mGmG-')
    const = ''.join(const)
    
    #adding identifying ends 
    sequence = "5'- " + sequence + " -3'"
    seq_mut = "5'- " + seq_mut + " -3'"
    compliment = "3'- " + compliment + " -5'"
    const_ = "5'- " + const + " -3'"
    
    #making length
    promoter_length = len(promoter)-1 #subtract 1 to account for dash
    terminal_cap_length = 2
    sequence_length = seq_len + 3 #add 3 because of added G's
    total_length = promoter_length + terminal_cap_length + sequence_length
    
    #Printing different sequences
    print ("\n")
    print ('loop sequence: %s' % (sequence))
    print ('loop sequence w/ mutations: %s' % (seq_mut))
    print ('loop mutations compliment: %s' % (compliment))
    print ('construct to order: %s' % (const_))
    print ('The construct is %s nt long' % (total_length))
    print ('\n')

make_mirna (sys.argv[1])
