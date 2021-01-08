# **Lesson 5: MATLAB Basics continued**

This lesson continues the introduction of basics of MATLAB programming for scientific computing. 
  
### **Introductory Videos**
* [Learning MATLAB Functions](http://www.learningmatlab.com/videos/IndividualPages/10-Functions/FunctionsIntro.html)
* [Publishing MATLAB Code from the Editor](https://www.youtube.com/watch?v=CWgl5Ylltxk&feature=emb_title&ab_channel=MATLAB)
[![](http://img.youtube.com/vi/CWgl5Ylltxk/0.jpg)](http://www.youtube.com/watch?v=CWgl5Ylltxk "")

#### **Comprehension Check**
* Fill in the blank. Input parameters to MATLAB functions are passed by _________.
* Fill in the blank. Variables created inside the function are ____________ variables.
* The ___________ feature in MATLAB allows you to create html, pdf, doc, etc. external documentation of your MATLAB code file and   output values, plots, and/or error messages for sharing. 

### **Two Part guided problem**
### **Walkthrough and Tutorial**
#### **Part One**
* Provided the code below (which can be downloaded from [here](https://bitbucket.org/ashleefv/checlassfa20/src/master/In%20Class%20Problem%20Activities/MATLAB/MATLABBasicsStart.m))
```MATLAB
%% MATLABBasicsStart.m
%   make a very simple plot of one function.

%% set parameters
xmin=0;
xmax=3;
Nx=200;

%% set independent variable
x=linspace(xmin,xmax,Nx);

%% calculate function values
f = 3*x.^2;

%% plot results
plot(x,f)
xlabel('x')
ylabel('functions of x')
legend('f(x) = 3x^2','Location','Best');
title('A simple plot')
grid on
```
* Next, edit the code to do the following things
  * Calculate a second expression g(x)=x
  * Suppress printing of this new expression
  * Plot g(x) on the same figure as f(x)
  * Label both f(x) and g(x) using a legend
  
Below is that code
```MATLAB
%% MATLABBasicsStart.m
%   make a very simple plot of one function.

%% set parameters
xmin=0;
xmax=3;
Nx=200;

%% set independent variable
x=linspace(xmin,xmax,Nx);

%% calculate function values
f = 3*x.^2;
g=x;
%% plot results
plot(x,f)
hold on
plot(x,g)
hold off
xlabel('x')
ylabel('functions of x')
legend('f(x) = 3x^2','g(x)= x','Location','Best');
title('A simple plot')
grid on
```
#### **Part Two**
* Copy and paste the code from problem 1, make it into a new function named MATLABBasics.m
* Allow the three parameters xmin, xmax, and Nx to be inputs to the funciton in this order. No output required

* Confirm the new function works and accepts input by typing in the command window

```MATLAB
MATLABBasics(0,10,200)
```
This should work; however the below should not
```MATLAB
MATLABBasics()
```
This is due to the lack of inputs

* Now modify the function MATLABBasics to accpet a variable number ofa rguments using keyword **varargin**
* Set the default values to 
```MATLAB
xmin=0; xmax=3; Nx=200;
```
* For example, use the following snippet to check if xmin is given, and either use varargin{1} [1 for first input] or use the default value

```MATLAB
if nargin < 1
xmin=0;
else
xmin=varargin{1};
end
```

* Test the new function by retyping in the command window
```MATLAB
MATLABasics()
```
* This should now recreate the same graph as the first command

#### **Solution to Part 2**
```MATLAB
%% MATLABBasics.m
%   make a very simple plot of one function.
function MATLABBasics(varargin)

if nargin < 1
    xmin=0;
else 
    xmin = varargin{1};
end

if nargin < 2
    xmax=3; 
else 
    xmax = varargin{2};
end

if nargin < 3
    Nx=200;
else 
    Nx = varargin{3};
end

%% set independent variable
x=linspace(xmin,xmax,Nx);

%% calculate function values
f = 3*x.^2;
g=x;
%% plot results
plot(x,f)
hold on
plot(x,g)
hold off
xlabel('x')
ylabel('functions of x')
legend('f(x) = 3x^2','g(x) = x','Location','Best');
title('A simple plot')
grid on
end
```
Or
```MATLAB
% Uses user-defined input if 3 inputs are provided
% Uses defaults otherwise

% if nargin < 3
     % default values
     xmin = 0; 
     xmax = 3;
     Nx = 200;
 else
     xmin = varargin{1};
     xmax = varargin{2};
     Nx = varargin{3};
end

%% set independent variable
x=linspace(xmin,xmax,Nx);

%% calculate function values
f = 3*x.^2;
g=x;
%% plot results
plot(x,f)
hold on
plot(x,g)
hold off
xlabel('x')
ylabel('functions of x')
legend('f(x) = 3x^2','g(x) = x','Location','Best');
title('A simple plot')
grid on
end
```
### **Additional Resources**
* [Mathworks Website](https://www.mathworks.com/help/matlab/)
* [MATLAB Central](https://www.mathworks.com/matlabcentral/)
* [Publish and Share MATLAB Code](https://www.mathworks.com/help/matlab/matlab_prog/publishing-matlab-code.html)

### **Previous Lesson**
 * [L04 MATLAB Basics](/L04%20MATLAB%20Basics.md)
### **Next Lesson**
 * [L06 Python Basics](/L06%20Python%20Basics.md)
