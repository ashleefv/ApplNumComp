# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 08:25:49 2020
@author: Ashlee
ODE Example 1
$\frac{dx}{dt} = b1-b2*x
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Data for example 1
xaxisData = np.array( [0.0, 0.5, 1.0, 5.0, 30.0] ) # time, independent variable
yaxisData = np.array( [0.0, 0.5, 1.2, 2.5, 2.7] ) # x, dependent variable

# guesses for parameters
b1guess = 1.0
b2guess = 1.0
parameterguesses = np.array([b1guess, b2guess])

# Need two functions for our model
# 1. to define the system of ODE(s)
# 2. to solve the ODE(s) and return ypredicted values in same shape as yaxisData

# 1. define ODE
def system_of_ODEs(x,t,parameters): # yvar, xvar, args
    # unpack the parameters
    b1 = parameters[0]
    b2 = parameters[1]
    dxdt = b1-b2*x
    return dxdt
# end of function

# 2. Solve ODEs at xaxisData points
    # and return calculated yaxisCalculated
    # using current values of the parameters
def model(xaxisData,*params):
    # initial condition(s) for the ODE(s)
    yaxis0 = 0.0 # should include a decimal
    yaxisCalc = np.zeros(xaxisData.size) 
    for i in np.arange(0,len(xaxisData)):
        if xaxisData[i] == 0.0: # should include a decimal
            yaxisCalc[i] = yaxis0
        else:
            xaxisSpan = np.linspace(0,xaxisData[i],101)
            ySoln = odeint(system_of_ODEs,yaxis0,xaxisSpan,args = (params,)) # soln for entire xaxisSpan
            yaxisCalc[i] = ySoln[-1] # calculated y at the end of the xaxisSpan
    return yaxisCalc
    # end of for loop
# end of model function 

# Estimate the parameters
parametersoln, pcov = curve_fit(model,xaxisData,yaxisData,p0=parameterguesses)
print(parametersoln)
plt.plot(xaxisData,yaxisData,'o',label='data')
yaxis0 = 0.0
xaxisForPlotting = np.linspace(0,xaxisData[-1],101)
yaxisCalcFromGuesses = odeint(system_of_ODEs,yaxis0,xaxisForPlotting,args = (parameterguesses,))
yaxisCalc = odeint(system_of_ODEs,yaxis0,xaxisForPlotting,args = (parametersoln,))
plt.plot(xaxisForPlotting,yaxisCalcFromGuesses,'r-',label='output with parameter guesses') # before fitting
plt.plot(xaxisForPlotting,yaxisCalc, 'g--', label='output with estimated parameters') # at soln parameters
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.show()