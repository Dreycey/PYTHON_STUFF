# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 00:03:46 2018

@author: Dreycey
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sympy import * 
import sympy as sp

##################################################
# Importing the file containing the data
##################################################
file = open('function_1.txt', "r")
lines = file.readlines()
ydata=[]
xdata=[]
for x in lines:
    xdata.append(int(float(x.split(' ')[1][0:-2])))
    ydata.append(int(float(x.split(' ')[0])))
file.close()

###################################################
# Algorithm/functions for fitting the data
###################################################
#Below is the equation for plotting the function
def func(x, a, b, c):
    return a*b*((1/np.tanh(x * (a / c) )) - c/(x * a) )


popt, pcov = curve_fit(func, xdata, ydata, bounds=((0, 1., 0.5), (50, 50, 50)))

print('here is the popt')
print(popt)
print(xdata)

yaxis_2=[]
for i in xdata:
    yaxis_2.append(func(i, *popt))

###################################################
# Printing the graphs for these data
###################################################
plt.scatter(xdata, ydata)
plt.plot(xdata, yaxis_2, 'r-')
plt.show()

plt.scatter(ydata, xdata)
plt.plot(yaxis_2, xdata, 'r-')
plt.show()