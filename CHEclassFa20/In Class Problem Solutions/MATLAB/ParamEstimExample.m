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

% Using lsqnonlin
% parameters = lsqnonlin(@(parameters)(sumExponentials(parameters,xdata)-ydata),parameters0); % in MATLAB documentation x is the parameters, not the xaxis or xdata
% MATLAB help for lsqnonlin: https://www.mathworks.com/help/optim/ug/lsqnonlin.html

% Using lsqcurvefit
[parameters, resnorm, residuals, exitflag, output] = lsqcurvefit(@sumExponentials, parameters0,xdata,ydata); % in MATLAB documentation x is the parameters, not the xaxis or xdata
% MATLAB help for lsqcurvefit: https://www.mathworks.com/help/optim/ug/lsqcurvefit.html

% plot the data
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

parameters
% solution:
% parameters =
% 
%     0.7533   -1.6017   -0.7533   -2.6963
resnorm

% defining the function to fit
function output = sumExponentials(parameters,x)
    a = parameters(1);
    b = parameters(2);
    c = parameters(3);
    d = parameters(4);
    
    y = a*exp(b*x)+c*exp(d*x);
    output = y;
end