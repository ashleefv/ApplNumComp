# **Matlab Basics**

This lecture focuses on basic Matlab functionality, an overview of the versatility and functions Matlab can do. 

## **Uses of Matlab**
  * Calculator
  * Scripts
  * Built in Plotting
  * Built in Functions
  * User defined functions
  * Publication tool
  * Loops
  
### **Before Class**
* Matlab installation- activate a code through [Mathworks](https://www.mathworks.com/academia.html), some institutions have access 
* If you can get access, download and install. If not, once you purchase an access code or activate one through an institution, you can use [Matlab online](https://matlab.mathworks.com/)  
* [Matlab Coding Best Practices](https://www.youtube.com/watch?v=ThDNl4m7GsI&feature=emb_title&ab_channel=AshleeN.FordVersypt)
[![](http://img.youtube.com/vi/ThDNl4m7GsI/0.jpg)](http://www.youtube.com/watch?v=ThDNl4m7GsI "")

### **Walkthrough and Tutorial**
Walk through real time coding of the following examples to show how to debug and the uses.
* Calculator- do some basic calculations
```matlab
2+2
3*4
```
* Scripts
```matlab

%% calculate function values
f = 3*x.^2;
g=x;
```
* Built in Plotting
```matlab
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
* Built in Functions
```matlab
 xmin = 0; 
 xmax = 3;
 Nx = 200;
x=linspace(xmin,xmax,Nx);
* User Defined functions
```matlab
%% set parameters
xmin=0;
xmax=3;
Nx=200;

%% set independent variable
x=linspace(xmin,xmax,Nx);

%% calculate function values
f = 3*x.^2;
```
* Publication Tool
```matlab
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
saveas(matlabbasics.jpg)
```
* Loops
```matlab
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
``` 
  
### **Additional Resources**
* [Mathworks Website](https://www.mathworks.com/help/matlab/)
* [Matlab Central](https://www.mathworks.com/matlabcentral/)
* [Video Tutorials for Matlab GUI Tools](http://learningmatlab.com/videos/index.html)
