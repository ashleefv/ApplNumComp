# **Lesson 11: Parameter Estimation in MATLAB**
Parameter estimation or curve fitting is the process of finding the coefficients or parameters to fit some model or curve to a set of data.
This lesson covers how to use MATLAB tools for this process.

## **Related Readings**
[Reading 6](https://github.com/ashleefv/ApplNumComp/blob/master/RecommendedReading.md#reading-6)

## **Instructional Videos**
* [Estimating parameters using measured data in Simulink](https://www.mathworks.com/videos/estimating-parameters-of-a-dc-motor-68856.html). Note: these lessons do not cover using Simulink to build models in MATLAB, so the parameter estimation procedures described in the lessons differ from those in this video. However, the visualization of the overall parameter estimation process and how the differences between the model predictions and the measured values are minimized is really helpful for seeing what we aim to accomplish with parameter estimation. 
* [What is curve fitting toolbox](https://www.mathworks.com/videos/curve-fitting-toolbox-overview-61198.html)
* [Using curve fitting toolbox for polynomial functions](https://www.youtube.com/watch?v=dc7YdW_3wGs&feature=emb_title&ab_channel=AnselmGriffin)

[![](http://img.youtube.com/vi/dc7YdW_3wGs/0.jpg)](http://www.youtube.com/watch?v=dc7YdW_3wGs "")

* [Using polyfit and curve fitting toolbox](https://www.youtube.com/watch?v=NsT5BAofRN0&feature=emb_title&ab_channel=LearnChemE)

[![](http://img.youtube.com/vi/NsT5BAofRN0/0.jpg)](http://www.youtube.com/watch?v=NsT5BAofRN0 "")

* [Using lsqcurvefit for simple functions](https://www.youtube.com/watch?v=kXAtvLHJAus&feature=emb_title&ab_channel=FreeSource)

[![](http://img.youtube.com/vi/kXAtvLHJAus/0.jpg)](http://www.youtube.com/watch?v=kXAtvLHJAus "")

## **Relfection Questions**
Based on your understanding of the videos, what are some of the advantages and disadvantages of using the following for parameter estimation, which is also known as curve fitting?
* polyfit
* curve fitting toolbox
* lsqcurvefit

## **Activity**
* Compare the procedures for curve fitting/parameter estimation in MATLAB using the following techniques with [data](https://bitbucket.org/ashleefv/checlassfa20/src/master/In%20Class%20Problem%20Activities/MATLAB/ParamEstimData.m)
   * lsqnonlin
   * lsqcurvefit
   * cftool
* Define the function to fit
```MATLAB
function output = sumExponentials(parameters,x)
    a = parameters(1);
    b = parameters(2);
    c = parameters(3);
    d = parameters(4);
    
    y = a*exp(b*x)+c*exp(d*x);
    output = y;
end
```
* Read in the data file and set up the guesses for the parameters
```MATLAB
%% Parameter Estimation Example
% ParamEstimExample.m

% fitting to a curve of this form:
% y = a*exp(b*x)+c*exp(d*x);

% read in the xdata, ydata
ParamEstimData
% output is xdata and ydata 

% define initial parameters guesses
a0 = 1;
b0 = -1;
c0 = -1;
d0 = -2;

% guesses for where to start parameter estimation
parameters0 = [a0, b0, c0, d0];
```
* Estimate parameters using lsqnonlin https://www.mathworks.com/help/optim/ug/lsqnonlin.html
```MATLAB
parameters = lsqnonlin(@(parameters)(sumExponentials(parameters,xdata)-ydata),parameters0); % in MATLAB documentation x is the parameters, not the xaxis or xdata
```
* Estimate parameters using lsqcurvefit https://www.mathworks.com/help/optim/ug/lsqcurvefit.html
```MATLAB
[parameters, resnorm, residuals, exitflag, output] = lsqcurvefit(@sumExponentials, parameters0,xdata,ydata); % in MATLAB documentation x is the parameters, not the xaxis or xdata
```
* Output
```MATLAB
parameters =

    0.7533   -1.6017   -0.7533   -2.6963


resnorm =

   5.7655e-06
```
* Plot the results
```MATLAB
figure(1)
plot(xdata,ydata,'o')

xforplotting = linspace(xdata(1),xdata(end),100);
yforplotting = sumExponentials(parameters,xforplotting);
hold on
plot(xforplotting,yforplotting)

yAtInitialGuess = sumExponentials(parameters0,xforplotting);
plot(xforplotting,yAtInitialGuess,'g')
hold off
legend('data', 'model with fitted parameters','initial guesses in the model')
```
![Expected Graph 1](/Lesson_images/Figure1_L11.jpg)
* Solution using lsqnonlin and lsqcurvefit in an [.m file](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/ParamEstimExample.m)
* Curve fitting toolbox solution [cftool output .sfit file](https://bitbucket.org/ashleefv/checlassfa20/src/master/In%20Class%20Problem%20Solutions/MATLAB/CurveFit1Example.sfit)

## **Previous Lesson**
 * [L10 Python and MATLAB Plotting](/L10%20Python%20and%20MATLAB%20Plotting.md)

## **Next Lesson**
 * [L12 Advanced Parameter Estimation in MATLAB](/L12%20Advanced%20Parameter%20Estimation%20in%20MATLAB.md)
