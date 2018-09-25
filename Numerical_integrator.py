# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:33:53 2017

@author: Dreycey
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt


#Paramaters for the functions
kA=1
alphaA=250
KA=1
n=2
alphaA0=1
gammaA=1
kR=1
alphaR=30
KR=1
m=4
alphaR0=1
gammaR=0.5

stepsize=0.1
starting=0
ending=109

b=starting
i=starting
starting_y=9
previous=starting_y
x=[]
y=[]
y2=[]
y.append(starting_y)
x.append(i)

#############################
# Derivative
#############################
'''
def derivative (A):
    
    R=1
        #Setting up the function2
    numerator2=kR*(alphaR*((A/KA)**n)+alphaR0)
    denominator2=(1+(A/KA)**n)
    leak2=gammaR*R
    
    #dR/dt
    f2=(numerator2)/(denominator2)-leak2 
    
    return f2
    #dydx = 1/(x)
   #return dydx
'''

def pend(y, t):
    A, R = y
    
    #Setting up the function2
    numerator2=kR*(alphaR*((A/KA)**n)+alphaR0)
    denominator2=(1+(A/KA)**n)
    leak2=gammaR*R
    
    #dR/dt
    f2=(numerator2)/(denominator2)-leak2 
    
###########################################################
    
    #Setting up the function1
    numerator1=kA*(alphaA*((A/KA)**n)+alphaA0)
    denominator1=(1+(A/KA)**n+(R/KR)**m)
    leak=gammaA*A

    #dA/dt
    f1=(numerator1)/(denominator1)-leak

    dydt = [f1, f2]
    
    return dydt
###################################
#Euler's method of integration
###################################
while i <= ending:
    #This is the euler ethod function:
    area_under_derivative=(derivative(i)*stepsize)
    f=area_under_derivative+previous
    previous=f
    
    print(f)
    #LIST OF VALUES TO PLOT

   # x.append()
    y.append(f)
    x.append(i+1)
    
    #add stepsize each loop
    i += stepsize
    
    

print(y)  
plt.plot(x,y)
plt.show()