# **Lesson 6: Python Basics**

The lesson introduces the basics of Python programming.

### **Introductory Video**
* [Four Ways to Run Python Code](https://www.youtube.com/watch?v=BRQ2DDpByE4&feature=emb_title&ab_channel=AshleeN.FordVersypt)
[![](http://img.youtube.com/vi/BRQ2DDpByE4/0.jpg)](http://www.youtube.com/watch?v=BRQ2DDpByE4 "")

#### **Comprehension Check**
* List the four ways described in the video to run Python codes. 

### **Why Python**
  [Python Motivation](https://towardsdatascience.com/why-python-is-not-the-programming-language-of-the-future-30ddc5339b66)
  
### **Installation and Access**
* Python installation- Install the most recent version of [Anaconda python](https://www.anaconda.com/products/individual)
  * This installs both Spyder and Jupyter notebooks
* If you can't download, use [Python Jupyter Notebooks online](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) 

* [Python code demos](https://bitbucket.org/ashleefv/checlassfa20/src/master/Pre%20Class%20Activities/Python/)

### **MATLAB to Python conversion Tutorial**
Walk through coding of the following examples to show how to debug and the uses.
[Starting MATLAB File](/CHEclassFa20/In%20Class%20Problem%20Activities/Python/ConvertFromMATLABtoPython.m)
* Start from this matlab code
```MATLAB
%% ICPL5matlab
% Used for comparison to Python function executing the same method.

%% Example: ax = b 
% Equation 1: $3x_1-0.1x_2-0.2x_3=7.85$. 
% Equation 2: $0.1x_1+7x_2-0.3x_3=-19.3$. 
% Equation 3: $0.3x_1-0.2x_2+10x_3=71.4$.
% Soln x = [3; -2.5; 7]

%% Initialize a matrix and b vector
a = [3, -.1, -.2; 0.1, 7, -0.3; 0.3, -.2, 10];
b = [7.85; -19.3; 71.4];

%% Solve for x
x = gaussElimin(a,b)
% no semicolon so x will print to the command window

%% Define Gaussian elimination function
function [x] = gaussElimin(a,b)
    %% Algorithm
    n = length(b);
    for k = 1:n-1
        for i = k+1:n
            if a(i,k) ~= 0
                lam = a(i,k)/a(k,k);
                a(i,k+1:n) = a(i,k+1:n) - lam*a(k,k+1:n);
                b(i)= b(i) - lam*b(k);
            end
        end
    end
    for k = n:-1:1
        b(k) = (b(k) - a(k,k+1:n)*b(k+1:n))/a(k,k);
    end
    x = b;
end
```
* Convert piecewise to Python code, debugging. Note the reduction in requisite logic statements; 4 "if" or "for" loops down to only 2 in Python. Also note the distinction between how to create matrices in both languages. 

#### **Solution Python Code**
[Starting Python Code](/CHEclassFa20/In%20Class%20Problem%20Activities/Python/ConverFromMATLABtoPython.ipynb)
```python
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
  
### **Additional Resources**
* [Python Software Carpentry Tutorial](https://swcarpentry.github.io/python-novice-inflammation/)
* [Spyder: the Scientific Python Development Environment](https://fangohr.github.io/blog/spyder-the-scientific-python-development-environment.html)
* [Jupyter Notebooks Tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook)
* [Introduction to Colab and Python](https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l01c01_introduction_to_colab_and_python.ipynb#scrollTo=X9uIpOS2zx7k)

### **Previous Lesson**
 * [L05 MATLAB Basics Continued](/L05%20MATLAB%20Basics%20Cont.md)
### **Next Lesson**
 * [L07 MATLAB Functions](/L07%20MATLAB%20Functions.md)
