# **Lesson 7: MATLAB Functions**

This lesson introduces built-in MATLAB functions for common classes of numerical methods for solving nonlinear equations, numerical integration, and ordinary differential equations (initial value problems).

## **Instructional Videos**
 * [Numerical methods](https://www.youtube.com/watch?v=430j9WP1uTQ&feature=emb_title&ab_channel=AshleeN.FordVersypt)
 
  [![](http://img.youtube.com/vi/430j9WP1uTQ/0.jpg)](http://www.youtube.com/watch?v=430j9WP1uTQ "")
* [Using MATLAB to solve a system of linear equations](https://www.youtube.com/watch?v=C4Ineu8uqGg&feature=emb_title&ab_channel=AshleeN.FordVersypt)
  
  [![](http://img.youtube.com/vi/C4Ineu8uqGg/0.jpg)](http://www.youtube.com/watch?v=C4Ineu8uqGg "")
* [MATLAB solvers](https://www.youtube.com/watch?v=8g_LB9J0RAQ&feature=emb_title&ab_channel=LearnChemE)
  
  [![](http://img.youtube.com/vi/8g_LB9J0RAQ/0.jpg)](http://www.youtube.com/watch?v=8g_LB9J0RAQ "")

## **Reflection Question**
* Find the MATLAB documentation for one of the built-in functions shown in the videos.

## **Optimization Functions**
* [Optimization Toolbox](https://www.mathworks.com/help/optim/referencelist.html?type=function)
* Solving nonlinear equations
  * fzero
  * fsolve
* Non-linear data-fitting
  * lsqcurvefit
* General optimization (minimization)
  * fminbnd
  * fmincon

## **Numerical Integration Functions**
* [Numerical integration and differentiation](mathworks.com/help/matlab/numerical-integration-and-differentiation.html)
  * quad, quadl, quadv --> integral
  * trapz

## **Solution Python Code**
Note this code is identical to the version in L06, and here can be used to demonstrate relationships between MATLAB functions and their analog in Python, allowing students to make the connection to whichever language is more intrinsic to their understanding.
[Raw code](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/ConvertFromMATLABtoPythonSoln.py)
```Python
"""
ICPL7Python

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
  
## **References for Further Exploration**
* [Algorithms for finding the root of nonlinear equations](https://www.youtube.com/watch?v=ujcZc5sPX4c&ab_channel=LearnChemE)

## **Previous Lesson**
 * [L06 Python Basics](/L06%20Python%20Basics.md)

## **Next Lesson**
 * [L08 Python Functions](/L08%20Python%20Functions.md)
