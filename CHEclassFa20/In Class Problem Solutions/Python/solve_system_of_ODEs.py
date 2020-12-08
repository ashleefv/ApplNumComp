# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:33:44 2020

@author: Ashlee
"""

import numpy as np

from scipy.integrate import odeint
import matplotlib.pyplot as plt

def system_of_ODEs(numerators=[6.25,0],denominator=0, parameters=[0.15,0.6,0.1,0.2]):
    # numerators are the dependent variables
    # denominator is the independent variable
    CA = numerators[0]
    CB = numerators[1]
    t = denominator
    k1 = parameters[0]
    k2 = parameters[1]
    k3 = parameters[2]
    k4 = parameters[3]
    
    dCAdt = -k1*CA-k2*CA
    dCBdt = k1*CA-k3-k4*CB
    
#    return np.array([[dCAdt],[dCBdt]]) # column vector
    return [dCAdt,dCBdt]

tspan = np.linspace(0,10,101)
CA0 = 6.25
CB0 = 0
C0 = CA0,CB0

k1 = 0.15
k2 = 0.6
k3 = 0.1
k4 = 0.2
parameters = (k1,k2,k3,k4)

output = odeint(system_of_ODEs, C0,tspan, args = (parameters,))
print(output)
plt.plot(output)