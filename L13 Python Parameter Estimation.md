# **Lesson 13: Parameter Estimation in Python**
Parameter estimation or curve fitting is the process of finding the coefficients or parameters to fit some model or curve to a set of data.
This lesson covers how to use Python tools for this process.

### **Introductory videos**
 * None for this lesson

#### **Comprehension Check**
   * None for this lesson
### **Python Plotting Example**
* Working [example](https://github.com/ashleefv/ApplNumComp/blob/master/Lecture%2014%20Examples.pdf) together
    * This is the same example from [lecture 14](https://github.com/ashleefv/ApplNumComp/blob/master/L12:%20Parameter%20Estimation%20for%20Matlab.md) , but now in Python.

* [Sample code for Example 1](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/ODEParamEstimExample1.py)
* Note the 2 datasets and imported packages
```Python
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
```
* Note the separate ODE systems
* Note the loops for the separate datapoints
```Python
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
```
* Note the graphs below, estimating and checking the parameters
```Python
# Estimate the parameters
parametersoln, pcov = curve_fit(model,xaxisData,yaxisData,p0=parameterguesses)
print(parametersoln)
plt.plot(xaxisData,yaxisData,'o')
yaxis0 = 0.0
xaxisForPlotting = np.linspace(0,xaxisData[-1],101)
yaxisCalcFromGuesses = odeint(system_of_ODEs,yaxis0,xaxisForPlotting,args = (parameterguesses,))
yaxisCalc = odeint(system_of_ODEs,yaxis0,xaxisForPlotting,args = (parametersoln,))
plt.plot(xaxisForPlotting,yaxisCalcFromGuesses,'r-') # before fitting
plt.plot(xaxisForPlotting,yaxisCalc, 'g--') # at soln parameters
plt.xlabel('t')
plt.ylabel('x')
plt.show()
 
```
* [Sample code for example 2](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/ODEParamEstimExample2.py)
* Note the new multiple array for dependent variables
```python
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

# Data for example 2
xaxisData = np.array( [0.5, 1.0, 5.0, 20.0] ) # time, independent variable
# new for > 1 dependent variables: for multiple rows, put each row in a [] and surround the whole thing by ([])
yaxisData = np.array( [ [99.0, 98.0, 50.0, 3.0], [2.0, 4.0, 35.0, 7.0] ] ) # x, dependent variable 

# guesses for parameters
b1guess = 0.01
b2guess = 0.2
parameterguesses = np.array([b1guess, b2guess])

# Need two functions for our model
# 1. to define the system of ODE(s)
# 2. to solve the ODE(s) and return ypredicted values in same shape as yaxisData

# 1. define ODEs
def system_of_ODEs(x,t,parameters): # yvar, xvar, args
    # unpack the parameters
    b1 = parameters[0]
    b2 = parameters[1]
    # unpack the dependent variables
    x1 = x[0]
    x2 = x[1]
    dx1dt = -b1*x1*x2
    dx2dt = b1*x1*x1-b2*x2
    return dx1dt, dx2dt
# end of function
```
* Note the definition of ODEs, and now solving for them in a loopwise notion
```Python
# 2. Solve ODEs at xaxisData points
    # and return calculated yaxisCalculated
    # using current values of the parameters
def model(xaxisData,*params):
    # initial condition(s) for the ODE(s)
    yaxis0 = np.array([100.0,1.0]) # should include a decimal
    # new for > 1 dependent variables:
    numYaxisVariables = 2
    yaxisCalc = np.zeros((xaxisData.size,numYaxisVariables))

    for i in np.arange(0,len(xaxisData)):
        if xaxisData[i] == 0.0: # should include a decimal
            # edit for > 1 dependent variables:            
            yaxisCalc[i,:] = yaxis0
        else:
            xaxisSpan = np.linspace(0.0,xaxisData[i],101)
            ySoln = odeint(system_of_ODEs,yaxis0,xaxisSpan,args = (params,)) # soln for entire xaxisSpan
            # edit for > 1 dependent variables:            
            yaxisCalc[i,:] = ySoln[-1,:] # calculated y at the end of the xaxisSpan
            # at this point yaxisCalc is now 2D matrix with the number of columns set as : to include all yvariables
            # curve_fit needs a 1D vector that has the rows in a certain order, which result from the next two commands
    yaxisOutput = np.transpose(yaxisCalc)
    yaxisOutput = np.ravel(yaxisOutput)
    return yaxisOutput
    # end of for loop
# end of model function 
```
* Now setting the code for plotting.
* Note the options for each different plot
```Python
# Estimate the parameters
# new for > 1 dependent variables:
# np.ravel(yaxisData) transforms yaxisData from a 2D vector into the 1D vector that curve_fit expects.

parametersoln, pcov = curve_fit(model,xaxisData,np.ravel(yaxisData),p0=parameterguesses)
print(parametersoln)
# edit for > 1 dependent variables:
plt.plot(xaxisData, yaxisData[0,:],'o') 
plt.plot(xaxisData, yaxisData[1,:],'x') 
# initial condition(s) for the ODE(s)
yaxis0 = np.array([100.0,1.0]) # should include a decimal
numYaxisVariables = 2

xaxisForPlotting = np.linspace(0,xaxisData[-1],101)

# Two options for getting the solution:
# OptionA call the model, which returns a 1D output and reshape into 2D
# OptionB wrap odeint around system_of_ODEs to solve the differential equations directly

# OptionA
yaxisCalc_OptionA = model(xaxisForPlotting,*parametersoln)
# the answer from model is 1D so we need to reshape it into the expected 2D matrix dimensions for plotting
yaxisCalc_OptionA = np.reshape(yaxisCalc_OptionA,(numYaxisVariables,xaxisForPlotting.size))
plt.plot(xaxisForPlotting, yaxisCalc_OptionA[0,:],'b-',label='x1 fitted')
plt.plot(xaxisForPlotting, yaxisCalc_OptionA[1,:],'r-',label='x2 fitted')

## OptionB
yaxisCalc_OptionB = odeint(system_of_ODEs,yaxis0,xaxisForPlotting,args = (parametersoln,))
plt.plot(xaxisForPlotting, yaxisCalc_OptionB[:,0],'g-',label='x1 fitted')
plt.plot(xaxisForPlotting, yaxisCalc_OptionB[:,1],'y-',label='x2 fitted')
# From the plot we see that OptionA and OptionB give exactly the same result, so you can chose either and not have to use both options.

yaxisCalcFromGuesses = odeint(system_of_ODEs,yaxis0,xaxisForPlotting,args = (parameterguesses,))
plt.plot(xaxisForPlotting,yaxisCalcFromGuesses,'k-') # before fitting
plt.xlabel('t')
plt.ylabel('x')
plt.show()
 
```

### **Additional Resources**
* [Python Curve Fitting tools](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)

### **Previous Lesson**
 * [L12 Advanced Parameter Estimation for MATLAB](/L12%20Advanced%20Parameter%20Estimation%20in%20MATLAB.md)
### **Next Lesson**
 * [L14 Introduction to GUIs](/L14%20Introduction%20to%20GUIs.md)
