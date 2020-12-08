# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 08:36:12 2018

@author: Ashlee
"""

import numpy as np
# computational assignment 2 python equivalent

def system_of_ODEs(t=0, C=[6.25,0], k1=0.15, k2=0.6, k3=0.1, k4=0.2):
    '''
This function defines a system of ordinary differential equations
$ \ frac{dC_A}{dt} &= -k_1 C_A-k_2 C_A$
and
$ \ frac{dC_B}{dt} &= k_1 C_A-k_3-k_4 C_B$ 
that describe the mass concentration of species A and B subject to the following chemical reactions at constant total volume:
A-->B
A-->C
B-->D
B-->E


Input: 
    t   time, h
    C   mass concentration: row vector [C_A, C_B], mg/L
    k1  rate constant, 1/h
    k2  rate constant, 1/h
    k3  rate constant, mg/L/h
    k4  rate constant, 1/h

Output:
    output time derivatives of mass concentrations, array [dC_A_dt, dCB_dt], mg/L/h 

Author:
    Professor Ashlee N. Ford Versypt, Ph.D.
    Oklahoma State University, School of Chemical Engineering
    ashleefv@okstate.edu
'''
    assert t>=0, "time can only be positive"
    C_A = C[0]
    C_B = C[1]
    dC_A_dt = -k1*C_A-k2*C_A
    dC_B_dt = k1*C_A-k3-k4*C_B
    return [dC_A_dt,dC_B_dt]#could use numpy.array to make column vector output

#C = np.array([6.25,0])
#z = system_of_ODEs(C)
#print(z)
print(system_of_ODEs())
print(system_of_ODEs(1,[1,1],k4=1,k3=1,k2=1,k1=1))