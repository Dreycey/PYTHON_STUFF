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

##################################
#SETTING UP NUMERICAL INTEGRATOR
##################################

stepsize=0.1
starting=0
ending=100

b = 0.25
c = 5.0

def derivative (omega):
    f1=omega
    return f1

def derivative2 (omega,theta):
    f2=(-b*omega - c*np.sin(theta))    
    return f2

while i <= ending:
    f=derivative(i)*stepsize+b
    f2=derivative2(f, i)*stepsize+b2
    y.append(f)
    x.append(i)
    y2.append(f2)
    b=f
    b2=f2
    i += stepsize
    
plt.plot(x, y, label='[A]')
plt.plot(x, y2, label='[R]')
plt.legend()
plt.show()