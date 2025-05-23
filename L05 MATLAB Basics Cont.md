# **Lesson 5: MATLAB Basics Continued**

This lesson continues the introduction of basics of MATLAB programming for scientific computing. 
  
## **Instructional Videos**
* [Learning MATLAB Functions](http://www.learningmatlab.com/videos/IndividualPages/10-Functions/FunctionsIntro.html)
* [Publishing MATLAB Code from the Editor](https://www.youtube.com/watch?v=CWgl5Ylltxk&feature=emb_title&ab_channel=MATLAB)

[![](http://img.youtube.com/vi/CWgl5Ylltxk/0.jpg)](http://www.youtube.com/watch?v=CWgl5Ylltxk "")

## **Reflection**
Fill in the blanks.
* Input parameters to MATLAB functions are passed by _________.
* Variables created inside the function are ____________ variables.
* The ___________ feature in MATLAB allows you to create html, pdf, doc, etc. external documentation of your MATLAB code file and output values, plots, and/or error messages for sharing. 

## **Activity**
### **Part One**
* Start with this [.m file](/CHEclassFa20/In%20Class%20Problem%20Activities/MATLAB/MATLABBasicsStart.m) or [MATLAB live script](https://github.com/ashleefv/ApplNumComp/blob/master/CHEclassFa20/In%20Class%20Problem%20Activities/MATLAB/MATLABBasicsStart.mlx)

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
![Expected Graph](/Lesson_images/figure_L05.jpg)

* Next, edit the code to do the following things
  1. Calculate a second expression g(x)=x
  2. Suppress printing of this new expression
  3. Plot g(x) on the same figure as f(x)
  4. Label both f(x) and g(x) using a legend
  
### **Part Two**
* Copy and paste the code from Part 1, make it into a new function named MATLABBasics.m
* Allow the three parameters xmin, xmax, and Nx to be inputs to the funciton in this order. No output is required. 
* Confirm the new function works and accepts input by typing in the command window
```MATLAB
MATLABBasics(0,10,200)
```
This should work; however the following should not:
```MATLAB
MATLABBasics()
```
This should fail, because we've defined a function that must have three inputs. Without three inputs, the function doesn't know what to do for the missing values.
* Now modify the function MATLABBasics to accept a variable number of arguments using keyword **varargin**
* Set the default values to 
```MATLAB
xmin=0; xmax=3; Nx=200;
```
* For example, use the following snippet to check if xmin is given, and either use varargin{1} where 1 denotes the 1st input or use the default if the value is not given:

```MATLAB
if nargin < 1
xmin=0;
else
xmin=varargin{1};
end
```
* Test the new function by running
```MATLAB
MATLABBasics(0,3,200)
MATLABasics()
```
* You should get the same plot for both commands.
* If it doesn't work, did you make an if statement for each input? 

### **Solution**
* [Solution .m file](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/MATLABBasics.m), [solution MATLAB live script](https://github.com/ashleefv/ApplNumComp/blob/master/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/MATLABBasics.mlx), and solution output [pdf file](https://github.com/ashleefv/ApplNumComp/blob/master/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/MATLABBasicsSoln.pdf) generated by the Publish feature
```MATLAB
%% MATLABBasics.m
%   make a very simple plot of one function.
function MATLABBasics(varargin)

% Uses user-defined input if 1, 2, or 3 inputs are provided
% Uses defaults otherwise
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
%% MATLABBasics.m
%   make a very simple plot of one function.
function MATLABBasics(varargin)
% Uses user-defined input if exactly 3 inputs are provided
% Uses defaults otherwise

if nargin < 3
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

## **References for Further Exploration**
* C. S. Lent. Ch. 7 Writing your own MATLAB functions in Learning to Program with MATLAB: Building GUI Tools. Wiley, Hoboken, NJ, 2013. ISBN: 978-0-470-93644-3. https://www.wiley.com/en-us/Learning+to+Program+with+MATLAB%3A+Building+GUI+Tools-p-9780470936443
* [Publish and Share MATLAB Code](https://www.mathworks.com/help/matlab/matlab_prog/publishing-matlab-code.html)

## **Previous Lesson**
 * [L04 MATLAB Basics](/L04%20MATLAB%20Basics.md)

## **Next Lesson**
 * [L06 Python Basics](/L06%20Python%20Basics.md)
