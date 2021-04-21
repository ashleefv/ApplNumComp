# **Lesson 9: MATLAB to Python Conversion**
This lesson focuses on an example of converting a code from MATLAB into Python to solve a system of ODEs.

## **Activity**
* Start from this [.m file](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/system_of_ODEs.m)
* Convert the MATLAB code to Python
 ```MATLAB
 function output = system_of_ODEs(varargin)
%% Documentation for system_of_ODEs.m
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
* Solution [.py file](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/system_of_ODEs.py)
* Note the short length of the executed Python code, emphasizing that different languages excel at different tasks.
* Note that to convert, first copy the comment section and change the symbol from % to #
* Then all that needs converting is the executed component, which in Python is less than 10 lines.
```Python
import numpy as np
# python equivalent

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
```

## **Previous Lesson**
 * [L08 Python Functions](/L08%20Python%20Functions.md)

## **Next Lesson**
 * [L10 Python and MATLAB Plotting](/L10%20Python%20and%20MATLAB%20Plotting.md)
