# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:38:52 2017

@author: Dreycey
"""


from scipy.integrate import odeint

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
((250*np.power(A,n)+alphaA0)/(1+np.power(A,n)+np.power(R,m)))-gammaA*A

((30*np.power(A,n))/(1+ np.power(A,n)) - gammaR*R

def pend(y, t):
    A, R = y
    
    #Setting up the function2
    numerator2=kR*(alphaR*((A/KA)**n)+alphaA0)
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


y0 = [1, 1]

t = np.linspace(0, 100, 101)

sol = odeint(pend, y0, t)

import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()