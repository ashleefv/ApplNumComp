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