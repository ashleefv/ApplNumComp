# **MATLAB to Python Conversions**
Work through of converting a code from MATLAB into python, using system of odes.

### **Walkthrough**
#### **Starting file**
[Raw MATLAB code](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/system_of_ODEs.m)
 ```MATLAB
 function output = system_of_ODEs(varargin)
%% Documentation for System_of_ODEs.m
% This function defines a system of ordinary differential equations
% $\frac{dC_A}{dt} &= -k_1 C_A-k_2 C_A$
%and
% $\frac{dC_B}{dt} &= k_1 C_A-k_3-k_4 C_B$ 
%that describe the mass concentration of species A and B subject to the following chemical reactions at constant total volume:
%$\mathrm{A}\rightarrow \mathrm{B}$

%$\mathrm{A}\rightarrow \mathrm{C}$
%$\mathrm{B}\rightarrow \mathrm{D}$
%$\mathrm{B}\rightarrow \mathrm{E}$

% Input: 
%   t   time, h
%   C   mass concentration: row vector [C_A, C_B], mg/L
%   k1  rate constant, 1/h
%   k2  rate constant, 1/h
%   k3  rate constant, mg/L/h
%   k4  rate constant, 1/h
%   nargin == 0 all input set to default values
%   nargin > 1  t, C defined by varargin{1} and varargin{2} and rate constants
%       set to default values
%   nargin > 5 all input defined by function call

% Output:
%   output time derivatives of mass concentrations, column vector [dC_A_dt, dCB_dt]', mg/L/h 

% Author:
%   Professor Ashlee N. Ford Versypt, Ph.D.
%   Oklahoma State University, School of Chemical Engineering
%   ashleefv@okstate.edu

%% Two if loops to avoid redundant definition of variables as in a single if loop
% Values for t and C
if nargin>1
    % read input values
    t = varargin{1}; 
    C = varargin{2}; 
else
    % default values
    t = 0; 
    C = [6.25, 0]; 
end
% Values for k1, k2, k3, and k4
if nargin==6 
    % read input values
    k1 = varargin{3}; 
    k2 = varargin{4}; 
    k3 = varargin{5}; 
    k4 = varargin{6}; 
else
    % default values
    k1 = 0.15; 
    k2 = 0.6; 
    k3 = 0.1;
    k4 = 0.2; 
end     

%% optional
% % error message or assertion to handle cases outside the expected use
% if nargin == 1 || nargin == 3 || nargin == 4 || nargin == 5 || nargin > 6
%     'Expected behavior is that there will be 0, 2, or 6 input parameters. Default values used.'
% end
% assert(nargin == 0 || nargin == 2 || nargin == 6, 'Number of inputs should be 0, 2, or 6.')

%% Unpack concentration vector into descriptive variable names
C_A = C(1);
C_B = C(2);

%% Define derivatives using descriptive names
dC_A_dt=-k1*C_A-k2*C_A;
dC_B_dt=k1*C_A-k3-k4*C_B;

%% Pack the derivatives into the output vector
output = [dC_A_dt; dC_B_dt]; 
 ```
#### **Final Python code**
[Raw Python Code](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/ConvertFromMATLABtoPythonSoln.py)
```python
# -*- coding: utf-8 -*-
"""
ICPL7python

Used for comparison to MATLAB function executing the same method.

Example: ax = b 
Equation 1: $3x_1-0.1x_2-0.2x_3=7.85$.                
Equation 2: $0.1x_1+7x_2-0.3x_3=-19.3$. 
Equation 3: $0.3x_1-0.2x_2+10x_3=71.4$.
Soln x = [3; -2.5; 7]

Created on Tue Aug 30 12:30:54 2016

@author: Ashlee N. Ford Versypt
"""

import numpy as np

# Initialize a matrix and b vector as numpy arrays
a = np.array( [ [3.0, -.1, -.2], [0.1, 7.0, -0.3],[ 0.3, -.2, 10.0] ] )
b = np.array( [ [7.85], [-19.3], [71.4] ] )

# Define Gaussian elimination function
def gaussElimin(a,b):
    n = len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

# Solve for x
x = gaussElimin(a,b)

# Print x
print("x =",x)
```

### **Previous Lesson**
 * [Lesson 8: Python Functions](/L08:%20Python%20Functions.md)
### **Next Lesson**
 * [Lesson 10: MATLAB and Python Plotting](/L10:%20Python%20and%20MATLAB%20Plotting.md)
