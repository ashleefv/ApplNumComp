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