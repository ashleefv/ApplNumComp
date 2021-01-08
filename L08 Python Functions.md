# **Lesson 8: Python Functions**

This lesson introduces built-in Python functions for common classes of numerical methods for solving nonlinear equations, numerical integration, and ordinary differential equations (initial value problems).

### **Introductory videos**
 * [Using Python to solve a system of linear equations](https://www.youtube.com/watch?v=g2aX77LAc0o&feature=emb_title&ab_channel=AshleeN.FordVersypt)
  [![](http://img.youtube.com/vi/g2aX77LAc0o/0.jpg)](http://www.youtube.com/watch?v=g2aX77LAc0o "")
* [Python built-in functions for numerical methods for nonlinear equations](https://www.youtube.com/watch?v=nnCDaHCulAU&feature=emb_title&ab_channel=APMonitor.com)
  [![](http://img.youtube.com/vi/nnCDaHCulAU/0.jpg)](http://www.youtube.com/watch?v=nnCDaHCulAU "")

#### **Comprehension Check**
  * Find the Python documentation for fsolve. Share the link
### **Optimization Functions**
* [Scipy Linalg Solver](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html
* Systems of linear equations: scipy.linalg.solve function
  * backlash equivalent: solve
* [Scipy Linalg optimize](https://docs.scipy.org/doc/scipy-0.13.0/reference/optimize.html)
* Optimization functions: use scipy.optimize package for all of the following functions
  * Solving nonlinear equations
    * fzero equivalents: brenq, brenth, ridder, bisect, newton
    * fsolve equivalent: fsolve
  * Non-linear data-fitting
    * lsqcurvefit equivalent: curve_fit
  * General optimization (minimization)
    * fminsearch equivalents: fmin, fmin_powell, fmin_cg, fmin_bfgs, fmin_ncg
    * fmincon equivalents: fmin_cobyla, fmin_tinc
* [Scipy Integrate](https://docs.scipy.org/doc/scipy/reference/integrate.html)
* Numerical integration: use scipy.integrate package for all of the following functions
  * quad (integral) equivalent: quad
  * trapz equivalent (relies on sampled data, not a function formula): numpy.trapz and scipy.optimize.simps
* Solving ordinary differential equations: use scipy.integrate package for all of the following functions
  * odeint: uses lsoda from FORTRAN library odepack for stiff or non-stiff systems with Adams and BDF algorithms
  * ode: allows for integrator algorithm to be explicitly specified
  * Newer functions for RK23 and RK45
    * ODE Python Example
    * [Core Python File](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/L9_odeint_example.py)
```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Function defines the ODEs and takes initial variable values, parameter 
# constants and the volume
def systems_of_ODEs(numerators, denominator, parameters):
    # Defining variables from numerators input
    A = numerators[0]
    B = numerators[1]
    x = denominator
  
    # Defining parameters from input
    a1 = parameters[0]
    a2 = parameters[1]
    
    # define the derivatives
    dA_dx = A+a1*B
    dB_dx = a2*A+2*B
    return dA_dx, dB_dx

# Defining the x range and granularity
xrange = np.linspace(0, 1, 101)

# Defining initial values
A0 = 100 
B0 = 0   
initial_val = A0, B0

# Defining parameter values
a1 = 1 # [m]
a2 = 1 # [m]
parameters = (a1, a2)
```
* Calling solver subprogram to solve the above defined system, then plotting the output for visual interpretation of results.
```Python
# Calling odeint to solve ODEs
output = odeint(systems_of_ODEs, initial_val, xrange, args = (parameters,)   )

# output vectors of numerators for each value of the denominator in the xrange
Asoln = output[:,0]
Bsoln = output[:,1]

# Plotting
line1 = plt.plot(xrange, Asoln, '-', label='$A$')
line2 = plt.plot(xrange, Bsoln, '--', label='$B$')
plt.legend()
plt.ylabel('$A$ and $B$')
plt.xlabel('$x$')
plt.show()
```
 * [Default values in Python](https://docs.python.org/3.7/tutorial/controlflow.html#more-on-defining-functions)
 * [Python for Loops](https://www.codementor.io/@sheena/python-generators-and-iterators-du1082iua)
  * More capabilities than MATLAB for loops using iterators and iterables
### **Additional Resources**
* [Python Modules](https://docs.python.org/3/tutorial/modules.html)

### **Previous Lesson**
 * [L07 MATLAB Functions](/L07%20MATLAB%20Functions.md)
### **Next Lesson**
 * [L09 MATLAB to Python Conversion](/L09%20MATLAB%20to%20Python%20conversions.md)
