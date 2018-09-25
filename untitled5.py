# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:38:52 2017

@author: Dreycey
"""

import numpy as np
from scipy.integrate import odeint

#Paramaters for the functions
kA=1
alphaA=250
KA=1
n=2
alphaA0=0
gammaA=1
kR=1
alphaR=0
KR=1
m=4
alphaR0=2
gammaR=1



def pend(y, t):
    A, R = y

    #dR/dt
    f2=((250*np.power(A,n)+alphaA0)/(1+np.power(A,n)+np.power(R,m)))-gammaA*A

    f1=((30*np.power(A,n)+alphaR)/(1+ np.power(A,n))) - gammaR*R

    dydt = [f2, f1]
    
    return dydt


y0 = [1, 1]

t = np.linspace(0, 1000, 200)


sol = odeint(pend, y0, t)

import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='[A]')
plt.plot(t, sol[:, 1], 'g', label='[R]')
plt.legend(loc='best')
plt.xlabel('time (seconds)')
plt.grid()
plt.show()