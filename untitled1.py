# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:51:53 2017

@author: Dreycey
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:33:53 2017

@author: Dreycey
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt


#######################################
#Defining differential equations
#######################################

#Paramaters for the functions
kA=1
alphaA=250
KA=1
n=1
alphaA0=1
gammaA=1
kR=1
alphaR=30
KR=1
m=2
alphaR0=1
gammaR=0.5


'''
#Setting up the function1
numerator1=kA*alphaA*((A/KA)**n)+alphaA0
denominator1=(1+(A/KA)**n+(R/KR)**m)
leak=gammaA*A

#dA/dt
f1=(numerator1)/(denominator1)-leak

#Setting up the function2
numerator2=kR*(alphaR*((A/KA)**n)+alphaA0)
denominator2=(1+(A/KA)**n)
leak2=gammaR*R

#dR/dt
f2=(numerator2)/(denominator2)-leak2
'''

##################################
#SETTING UP NUMERICAL INTEGRATOR
##################################

stepsize=0.1
starting=0
ending=100


x=[]
y=[]
y2=[]
b=starting
b2=starting
i=starting


def derivative (A,R):
    #Setting up the function1
    numerator1=kA*(alphaA*((A/KA)**n)+alphaA0)
    denominator1=(1+(A/KA)**n+(R/KR)**m)
    leak=gammaA*A

    #dA/dt
    f1=(numerator1)/(denominator1)-leak
    
    return f1

def derivative2 (A,R):
    #Setting up the function2
    numerator2=kR*(alphaR*((A/KA)**n)+alphaA0)
    denominator2=(1+(A/KA)**n)
    leak2=gammaR*R
    
    #dR/dt
    f2=(numerator2)/(denominator2)-leak2    
    
    return f2

while i <= ending:
    f=derivative(i, b2)*stepsize+b
    f2=derivative2(i, b)*stepsize+b2
    b=f
    b2=f2
    y.append(f)
    x.append(i)
    y2.append(f2)
    i += stepsize
    
plt.plot(x,y, label='[A]')
plt.plot(x,y2, label='[R]')
plt.legend()
plt.show()